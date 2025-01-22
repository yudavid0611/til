import unittest

from production.money import Money
from production.portfolio import Portfolio
from production.bank import Bank


class TestMoney(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank()
        self.bank.add_exchange_rate('Euro', 'Dollar', 1.2)
        self.bank.add_exchange_rate('Dollar', 'Euro', 1100)

    def test_muliplication(self):
        five_dollars = Money(5, 'Dollar')
        ten_dollars = five_dollars.times(2)
        self.assertEqual(ten_dollars, five_dollars.times(2))
    
    def test_division(self):
        won_4002 = Money(4002, 'Korean')
        won_10005 = won_4002.divide(4)
        self.assertEqual(won_10005, won_4002.divide(4))
        
    def test_addition_1(self):
        '''
        동일 화폐 더하기
        '''

        portfolio = Portfolio()
        five_dollars = Money(5, 'Dollar')
        ten_dollars = Money(10, 'Dollar')
        fifteen_dollars = Money(15, 'Dollar')

        portfolio.add(five_dollars)
        portfolio.add(ten_dollars)

        self.assertEqual(fifteen_dollars, portfolio.evaluate(self.bank, 'Dollar'))
    
    def test_addition_2(self):
        '''
        돈이 없는 상태에서 포트폴리오 평가하기
        '''

        portfolio = Portfolio()
        zero_dollar = Money(0, 'Dollar')

        portfolio.add(zero_dollar)

        self.assertEqual(zero_dollar, portfolio.evaluate(self.bank, 'Dollar'))
    
    def test_addition_dollars_and_euros(self):
        '''
        달러와 유로 더하기
        '''

        portfolio = Portfolio()

        five_dollars = Money(5, 'Dollar')
        ten_euors = Money(10, 'Euro')

        portfolio.add(five_dollars, ten_euors)
        
        seventeen_dollars = Money(17, 'Dollar')

        actual_value = portfolio.evaluate(self.bank, 'Dollar')
        self.assertEqual(
            seventeen_dollars, 
            actual_value,
            f'{seventeen_dollars} != {actual_value}'
        )
    
    def test_conversion(self):
        '''
        환전 테스트
        '''

        ten_euros = Money(10, 'Euro')
        self.assertEqual(self.bank.convert(ten_euros, 'Dollar'), Money(12, 'Dollar'))
        self.bank.add_exchange_rate('Euro', 'Dollar', 1.3)
        self.assertEqual(self.bank.convert(ten_euros, 'Dollar'), Money(13, 'Dollar'))
    
    def test_addition_with_multiple_missing_exchange_rates(self):
        '''
        여러 환율이 누락된 경우
        '''

        bank = Bank()
        ten_euros = Money(10, 'Euro')

        with self.assertRaisesRegex(
            Exception,
            'Missing exchange rates: Euro->Dollar',
        ):
            bank.convert(ten_euros, 'Dollar')


if __name__ == '__main__':
    unittest.main()