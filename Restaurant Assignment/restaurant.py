import math

class Table:
    def __init__(self, pax: int):
        self.pax = pax
        self.bill = []

    def round_up(self, n, decimals=0):
        multiplier = 10 ** decimals
        return math.ceil(n * multiplier) / multiplier

    def pop_and_return_previous_quantity(self, item: str, pricefloat) -> int:
        previous_quantity = 0
        for index, x in enumerate(self.bill):
            if (x["item"] == item and x["price"] == price):
                previous_quantity = x["quantity"]
                self.bill.pop(index)
        return previous_quantity

    def order(self, item: str, price: float, quantity: int = 1) -> None:
        self.bill.append({"item": item, "price": price, "quantity": quantity+self.pop_and_return_previous_quantity(item,price)})

    def remove(self, item: str, price: float, quantity: int = 1) -> bool:
        if quantity <= 0:
            return False
        previous_quantity = self.pop_and_return_previous_quantity(item,price)
        if previous_quantity-quantity < 0:
            self.bill.append({"item": item, "price": price, "quantity": previous_quantity})
            return False
        self.bill.append({"item": item, "price": price, "quantity":previous_quantity-quantity})
        return True

    def get_subtotal(self) -> float:
        subtotal = 0
        for item in self.bill:
            subtotal += item["price"]*item["quantity"]
        return subtotal

    def get_total(self, service_charge: float = 0.10) -> object:
        return {"Sub Total":"£"+str( format(self.get_subtotal(), '.2f')),
                "Service Charge":"£"+str(format(self.get_subtotal()*service_charge, '.2f')),
                "Total":"£"+str(format(self.get_subtotal()+self.get_subtotal()*service_charge, '.2f'))}

    def split_bill(self) -> float:
        split = self.get_subtotal()/self.pax
        return self.round_up(split, 2)
