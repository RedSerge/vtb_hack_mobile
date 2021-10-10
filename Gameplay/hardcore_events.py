from Gameplay.events import Event, ComplexEvent

#   Independent: Actions, SeriousBusiness, BuyHouse, GoodCompany, EnterHack


class Actions(ComplexEvent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action_type = 2
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

    def history_str(self):
        return "Купил акции"


class AdvancedActions(ComplexEvent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action_type = 2
        self.positive = False
        self.single = True
        self.cash_per_turn = 125
        self.value_base = 500
        self.value_current = 125
        self.value_delta = 50
        self.value_decay = 0.001

    def __str__(self):
        return f'Прогнозы авиакомпании "Солнечные авиалинии" не сбылись. Стоимость акции упала на 25%. \n Текущая цена: {self.value_current} \n Справедливая цена:{self.value_base}'

    def history_str(self):
        return "Продал акции"


class SeriousBusiness(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.instant_cash = -1000
        self.action_type = 1
        self.enable_events = {
            SeriousInsurance,
            SeriousGrowth,
            SeriousFailure,
        }

    def __str__(self):
        return "У вас появилась возможность начать свой бизнес, стоимость 1000."

    def history_str(self):
        return "Начал бизнес"


class SeriousGrowth(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.cash_per_turn = 1500

    def __str__(self):
        return "Ваш бизнес растет, теперь вы получаете 1500 за ход."

    def history_str(self):
        return "Бизнес вырос"


class SeriousInsurance(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.instant_cash = -200
        self.action_type = 1
        self.disable_events = {
            SeriousFailure
        }
        self.enable_events = {
            SeriousSafety
        }

    def __str__(self):
        return "У вас есть возможность застраховать свой бизнес за 200 рублей."

    def history_str(self):
        return "Застраховал бизнес"


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

    def history_str(self):
        return "Потерял бизнес со страховкой"


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

    def history_str(self):
        return "Потерял бизнес"


class BuyHouse(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.action_type = 1
        self.instant_cash = -1100
        self.cash_per_turn = 150
        self.enable_events = {
            SellHouse
        }

    def __str__(self):
        return "Ваш сосед переезжает и продает свой дом. \n - Предложенная цена: 1100р \n - Средняя рыночная цена: 950р \n - Пассивный доход за каждый ход: 150р"

    def history_str(self):
        return "Купил дом"


class SellHouse(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.action_type = 1
        self.instant_cash = 1300
        self.cash_per_turn = -150

    def __str__(self):
        return "Спрос на недвижимость вырос, ваш дом подорожал. Теперь его цена составляет 1300р. Хотите продать его?"

    def history_str(self):
        return "Продал дом"


class GoodCompany(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.action_type = 1
        self.instant_cash = 77
        self.enable_events = {
            BetterCompany
        }

    def __str__(self):
        return 'У вас есть возможность купить акции компании "August Investment" \n - Текущая цена: 77 рублей \n - Справедливая цена: 177 рублей'

    def history_str(self):
        return "Купил акции"


class BetterCompany(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.action_type = 1
        self.instant_cash = 112
        self.enable_events = {
            BetterCompany
        }

    def __str__(self):
        return 'Акции компании "August Investment" выросли на 50% \n - Текущая цена: 112 \n - Справедливая цена: 177'

    def history_str(self):
        return "Продал акции"


class EnterHack(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.action_type = 1
        self.enable_events = {
            WinHack
        }

    def __str__(self):
        return 'Вас позвали поучаствовать в хакатоне [More.tech](http://More.tech) 3.0'

    def history_str(self):
        return "Принял участие в хакатоне"


class WinHack(Event):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positive = True
        self.single = True
        self.instant_cash = 3000

    def __str__(self):
        return 'Вы выиграли хакатон + 3000 рублей!'

    def history_str(self):
        return "Выиграл в хакатоне"
