class Bale:
    def __init__(self, bale_id, category, grade, purchase_price):
        self.bale_id = bale_id
        self.category = category
        self.grade = grade
        self.purchase_price = purchase_price
        self.sold = False

    def break_even_price(self):
        return round(self.purchase_price * 1.2, 2)

class BaleInventory:
    def __init__(self):
        self.bales = []

    def add_bale(self, bale):
        self.bales.append(bale)

    def sell_bale(self, bale_id):
        for bale in self.bales:
            if bale.bale_id == bale_id and not bale.sold:
                bale.sold = True
                return f"Bale {bale_id} sold at break-even price: {bale.break_even_price()}"
        return f"Bale {bale_id} not found or already sold."

    def stock_report(self):
        remaining = [bale for bale in self.bales if not bale.sold]
        return f"Total stock remaining: {len(remaining)}"

# Example usage
inventory = BaleInventory()
inventory.add_bale(Bale("B001", "Men's Shirts", "First Selection", 100))
inventory.add_bale(Bale("B002", "Women's Dresses", "Grade B", 80))

print(inventory.sell_bale("B001"))
print(inventory.stock_report())
