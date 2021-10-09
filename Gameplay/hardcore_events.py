from events import Event, ComplexEvent


class Actions(ComplexEvent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.cash_per_turn = -500
        self.value_base = 500
        self.value_current = 420
        self.value_delta = 50
        self.value_decay = 0.001
        self.enable_events = {
            AdvancedActions
        }

    def __str__(self):
        return f'Из новостей вы узнали, что количество рейсов авиакомпании "Солнечные авиалинии" в следующем году увеличится в два раза. Выдалась возможность взять кредит, чтобы купить акции этой компании. \n Текущая цена: {self.value_current} \n Справедливая цена:{self.value_base}'


class AdvancedActions(ComplexEvent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = False
        self.single = True
        self.cash_per_turn = 125
        self.value_base = 500
        self.value_current = 125
        self.value_delta = 50
        self.value_decay = 0.001

    def __str__(self):
        return f'Из новостей вы узнали, что количество рейсов авиакомпании "Солнечные авиалинии" в следующем году увеличится в два раза. Выдалась возможность взять кредит, чтобы купить акции этой компании. \n Текущая цена: {self.value_current} \n Справедливая цена:{self.value_base}'


class SeriousBusiness(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.instant_cash = -1000
        self.enable_events = {
            SeriousInsurance,
            SeriousGrowth,
            SeriousFailure,
        }

    def __str__(self):
        return "У вас появилась возможность начать свой бизнес, стоимость 1000."


class SeriousGrowth(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.cash_per_turn = 1500


    def __str__(self):
        return "Ваш бизнес растет, теперь вы получаете 1500 за ход."


class SeriousInsurance(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.instant_cash = -200
        self.disable_events = {
            SeriousFailure
        }
        self.enable_events = {
            SeriousSafety
        }

    def __str__(self):
        return "У вас есть возможность застраховать свой бизнес за 200 рублей."


class SeriousSafety(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = False
        self.single = True
        self.instant_cash = 1000
        self.disable_events = {
            SeriousFailure
        }

    def __str__(self):
        return "Ваш бизнес пришлось закрыть. Страховая компания выплатила вам 1000 рублей."


class SeriousFailure(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = False
        self.single = True
        self.disable_events = {
            SeriousSafety
        }

    def __str__(self):
        return "Ваш бизнес пришлось закрыть."
