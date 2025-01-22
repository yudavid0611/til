from production.money import Money
from production.bank import Bank


class Portfolio:
    def __init__(self):
        self.money_list = []
    
    def add(self, *money: Money) -> None:
        '''
        새로운 돈을 더한다.
        '''

        self.money_list.extend(money)

    def evaluate(self, bank: Bank, currency: str | None = 'Dollar') -> Money:
        '''
        currency 기준으로 포트폴리오를 평가한다.
        '''

        total = 0
        failures = []
        for money in self.money_list:
            try:
                total += bank.convert(money, currency).amount
            except KeyError as e:
                failures.append(f'{e.args[0]}->{currency}')
        
        if not failures:
            return Money(total, currency)
        
        else:
            failure_message = ', '.join(failures)
            raise Exception(f'Missing exchange rates: {failure_message}')







