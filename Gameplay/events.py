class Event:
    def __init__(
            self,
            positive=False,
            single=False,
            instant_cash=0,
            cash_per_turn=0,
            turns=-1,
            turns_left=-1,
            enable_events=None,
            disable_events=None,
            disable_objects=None,
            count=1,
            *args, **kwargs
    ):
        self.positive = positive
        self.single = single
        self.instant_cash = instant_cash
        self.cash_per_turn = cash_per_turn
        self.turns = turns
        self.turns_left = turns_left
        self.enable_events = enable_events if enable_events is not None else set()
        self.disable_events = disable_events if disable_events is not None else set()
        self.disable_objects = disable_objects if disable_objects is not None else set()
        self.count = count

    def spend_turn(self):
        if self.turns_left == 0:
            self.count -= 1
            self.turns_left = self.turns
        if self.count <= 0:
            return 0
        return self.cash_per_turn * self.count

    def __str__(self):
        return "Ничего не случилось"


class ComplexEvent(Event):
    def __init__(
            self,
            value_base=0,
            value_delta=0,
            value_decay=0,
            value_current=0,
            *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.value_base = value_base
        self.value_delta = value_delta
        self.value_decay = value_decay
        self.value_current = value_current


# Частные реализации:


class Job(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.cash_per_turn = 500
        self.enable_events = {
            Promotion
        }

    def __str__(self):
        return "Вы нашли новую работу, теперь вы получаете +500 рублей каждый ход."


class Promotion(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.cash_per_turn = 250

    def __str__(self):
        return "Вас повысили, теперь вы получаете +250 рублей каждый ход."


class Legacy(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.instant_cash = 500

    def __str__(self):
        return "Вы получили наследство +500 рублей."


class Friend(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.instant_cash = 350

    def __str__(self):
        return "Ваш старый знакомый вернул вам долг +350 рублей."


class RepairTV(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instant_cash = -100

    def __str__(self):
        return "У вас сломался телевизор. Ремонт составил -100 рублей."


class Dentist(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cash_per_turn = -50
        self.turns = self.turns_left = 4

    def __str__(self):
        return "Вам пришлось сходить к стоматологу, стоимость лечения составит в сумме -200 рублей за 4 посещения."


class UnexpectedTaxi(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instant_cash = -150

    def __str__(self):
        return "Вы опоздали на электричку, вам пришлось поехать на такси -150 рублей."


class Birthday(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instant_cash = -200
        self.single = True

    def __str__(self):
        return "У вашей мамы день рождения. Вы сделали ей подарок на -200 рублей."
