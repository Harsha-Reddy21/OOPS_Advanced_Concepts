
import re
class Product:
    def __init__(self, name, price, discount_percentage, quantity, category):
        self._name = name
        self.base_price = price
        self._discount_percent = discount_percentage
        self._stock_quantity = quantity
        self._category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not (3<=len(value)<=50):
            raise ValueError("Name must be between 3 and 50 characters")
        self._name = value

    @property
    def base_price(self):
        return self._base_price
    
    @base_price.setter
    def base_price(self, value):
        if value <= 0 or value > 50000:
            raise ValueError("Base price must be between 0 and 50000")
        self._base_price = value
    
    @property
    def discount_percent(self):
        return self._discount_percent
    
    @discount_percent.setter
    def discount_percent(self, value):
        self._discount_percent = round(value, 2)

    @property
    def stock_quantity(self):
        return self._stock_quantity
    
    @stock_quantity.setter
    def stock_quantity(self, value):
        if value < 0 or value > 10000:
            raise ValueError("Stock quantity must be between 0 and 10000")
        self._stock_quantity = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        categories = ["Electronics", "Clothing", "Books", "Home","Sports"]
        if value not in categories:
            raise ValueError("Invalid category")
        self._category = value
    
    @property
    def final_price(self):
        return round(self._base_price * (1 - self._discount_percent / 100), 2)
    
    @property
    def savings_amount(self):
        return round(self._base_price - self.final_price, 2)

    @property
    def availability_status(self):
        if self.stock_quantity==0:
            return "Out of Stock"
        elif self.stock_quantity<10:
            return "Low Stock"
        else:
            return "In Stock"
        
    def product_summary(self):
        return f"Product: {self._name}\nCategory: {self._category}\nBase Price: ${self._base_price:.2f}\nDiscount: {self._discount_percent}%\nFinal Price: ${self.final_price:.2f}\nSavings: ${self.savings_amount:.2f}\nAvailability: {self.availability_status}"
    
    





product = Product("Gaming Laptop", 1299.00, 15.5, 25, "Electronics")
assert product.name == "Gaming Laptop"
assert product.base_price == 1299.00
assert product.discount_percent == 15.5
assert abs(product.final_price - 1097.66) < 0.01
assert abs(product.savings_amount - 201.34) < 0.01
assert product.availability_status == "In Stock"


product.discount_percent = 20.567
assert product.discount_percent == 20.57
assert abs(product.final_price - 1031.79) < 0.01

product.stock_quantity = 5
assert product.availability_status == "Low Stock"

try:
    product.name='AB'
    assert False, "Invalid name should raise an error"
except ValueError as e:
    pass
    
try:
    product.base_price = -100
    assert False, "Invalid base price should raise an error"
except ValueError as e:
    pass
    
try:
    product.category = "Food"
    assert False, "Invalid category should raise an error"
except ValueError as e:
    pass
    
    

assert "Gaming Laptop" in product.product_summary()
assert "1299.00" in product.product_summary()
assert "Low Stock" in product.product_summary()

print(product.product_summary())






