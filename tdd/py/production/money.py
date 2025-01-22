class Money:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency
    
    def times(self, multiplier: float) -> 'Money':
        return Money(self.amount * multiplier, self.currency)
    
    def divide(self, divisor: float) -> 'Money':
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other_money: 'Money') -> bool:
        return (
            self.currency == other_money.currency
            and self.amount == other_money.amount
        )
    
    def __str__(self) -> str:
        return f'{self.currency} {self.amount:0.2f}'