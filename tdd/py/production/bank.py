from production.money import Money


class Bank:
    def __init__(self):
        self.exchange_rates = {}

    def add_exchange_rate(self, currency_from:str, currency_to: str, rate: float) -> None:
        '''
        환율을 추가합니다.
        '''

        exchange_rates = self.exchange_rates.get(currency_from, None)
        if exchange_rates is None:
            self.exchange_rates[currency_from] = {}
        
        self.exchange_rates[currency_from].update({currency_to: rate})

    def convert(self, money: Money, currency: str) -> 'Money':
        '''
        환전을 한다.
        '''

        # 동일한 통화일 경우
        if money.currency == currency:
            return Money(money.amount, currency)

        try:
            return Money(money.amount * self.exchange_rates[money.currency][currency], currency)
        except KeyError as e:
            raise Exception(f'Missing exchange rates: {e.args[0]}->{currency}')
