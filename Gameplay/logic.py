from Gameplay.support import *
from Gameplay.events import *
from Gameplay.hardcore_events import *

from random import choice

EVENT_THRESHOLD = 0.2
EVENT_THRESHOLD_DECAY = 0.0001
EVENT_CATCHUP_STEPS = 5
MAX_TURNS = 20
START_CASH = 1000


class Player:

    def __init__(self):
        self.restful = {}
        self.negative_history = []
        self.current_threshold = EVENT_THRESHOLD
        self.current_turn = 0
        self.cash = START_CASH
        self.available_events = {
            Job,
            Legacy,
            Friend,
            RepairTV,
            Dentist,
            UnexpectedTaxi,
            Birthday,
        }
        self.object_events = set()
        self.default_event = Event

    def get_collection_events(self, is_positive):
        collection_events = set()
        for event_cls in self.available_events:
            event = event_cls()
            if event.positive == is_positive:
                if (not event.single) or (
                        event.single and event_cls not in [type(t) for t in self.object_events]
                ):
                    collection_events.add(event_cls)
        return collection_events

    def get_next_event(self, is_positive):
        collection_events = self.get_collection_events(is_positive)
        return choice(list(collection_events if len(collection_events) else self.available_events))

    def clean_objects(self):
        self.object_events = {i for i in self.object_events if i.count > 0}

    def disable_objects(self, disabled_classes):
        for i in self.object_events:
            if type(i) in disabled_classes:
                i.count -= 1
        self.clean_objects()

    def apply_event(self, ev_cls):
        ev = ev_cls()
        self.restful['text'] = str(ev)
        if hasattr(ev, 'input'):    # DEBUG: rebuild the logic for REST API
            if not ev.input():
                return
        self.cash += ev.instant_cash
        if ev.cash_per_turn or ev.single:
            x = [i for i in self.object_events if type(i) is type(ev)]
            if x:
                x[0].count += 1
            else:
                self.object_events.add(ev)
        self.available_events = (self.available_events | ev.enable_events) - ev.disable_events
        self.disable_objects(ev.disable_objects)

    def apply_events_per_turn(self):
        sum_per_turn = sum([i.spend_turn() for i in self.object_events])
        self.cash += sum_per_turn
        self.restful['income'] = sum_per_turn  # DEBUG: just demo
        self.clean_objects()
        return sum_per_turn

    def average_negativity(self):
        return avg(self.negative_history)

    def choose_simple_event(self):
        if self.current_turn < EVENT_CATCHUP_STEPS:
            negativity = 1
        else:
            average_negativity = self.average_negativity()
            negativity = -sign_pos(average_negativity) if abs(
                average_negativity) > self.current_threshold else random_sign()
            self.current_threshold += EVENT_THRESHOLD_DECAY if self.current_threshold < 1.0 else 0
        event = self.get_next_event(bool(negativity > 0))
        self.negative_history.append(1 if event().positive else -1)
        return event

    def run(self):
        self.restful = {}
        if self.current_turn > MAX_TURNS or self.cash <= 0:
            return False
        event_cls = self.choose_simple_event()
        if event_cls is None:
            event_cls = self.default_event
        self.apply_events_per_turn()
        self.apply_event(event_cls)
        self.current_turn += 1

        self.restful['cash'] = self.cash    # DEBUG: just demo

        return True

    def simple_events_count(self, negative=True):
        return self.negative_history.count(-1 if negative else 1)


class Gameplay:
    active_player = Player()

    @classmethod
    def reset(cls):
        cls.active_player = Player()
