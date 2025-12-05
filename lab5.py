class Flower:
    def __init__(self, height = 0.0, size = 0.0, color = "", 
                 price = 0.0, quantity = 0, delivery_rate = 0.0):
        self.__height = abs(height)
        self.__size = abs(size)
        self.__color = color
        self.__price = abs(price)
        self.__quantity = abs(int(quantity))
        self.__delivery_rate = abs(delivery_rate)
        self.available = True
        self.category = "None"

    def get_height(self):
        return self.__height

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color
    
    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_delivery_rate(self):
        return self.__delivery_rate

    def set_height(self, height):
        self.__height = height

    def set_size(self, size):
        self.__size = size

    def set_color(self, color):
        self.__color = color

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_delivery_rate(self, delivery_rate):
        self.__delivery_rate = delivery_rate

    def __str__(self):
        return (f"Квітка: {self.__color}\n"
                f"Висота: {self.__height} см\n"
                f"Розмір: {self.__size} см\n"
                f"Ціна: {self.__price} грн\n"
                f"Кількість: {self.__quantity} шт\n"
                f"Доставка: {self.__delivery_rate} грн\n"
                f"Категорія: {self.category}\n"
                f"Доступна: {'Так' if self.available else 'Ні'}")

    def __repr__(self):
        return (f"Flower(height={self.__height}, size={self.__size}, "
                f"color='{self.__color}', price={self.__price}, "
                f"quantity={self.__quantity}, delivery_rate={self.__delivery_rate})")

    def __del__(self):
        print(f"Квітка '{self.__color}' видалена з системи")

class FlowerShop:
    def __init__(self, name = "", adress = "", phone = ""):
        self.__name = name
        self.__adress = adress
        self.__phone = phone
        self.__flowers = []
        self.rating = 0.0
        self.is_open = True

    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__adress

    def get_phone(self):
        return self.__phone

    def get_flowers(self):
         return self.__flowers

    def set_name(self, name):
        self.__name = name

    def set_adress(self, adress):
        self.__adress = adress

    def set_phone(self, phone):
        self.__phone = phone

    def add_flower(self, flower):
        self.__flowers.append(flower)
        print(f"Квітку '{flower.get_color()}' додано до магазину '{self.__name}'")

    def remove_flower(self, flower):
        if flower in self.__flowers:
            self.__flowers.remove(flover)
            print(f"Квітку '{flower.get_color()}' видалено з магазину '{self.__name}'")
        else:
            print(f"Квітка не знайдена в асортименті")

    def get_most_expensive(self):
        if not self.__flowers:
            return None
        return max(self.__flowers, key = lambda f: f.get_price())

    def get_total_quantity(self):
        return sum(f.get_quantity() for f in self.__flowers)

    def get_max_bouquet_value(self):
        if not self.__flowers:
            return 0, None
        max_value = 0
        best_flower = None
        for flower in self.__flowers:
            value = flower.get_price() * flower.get_quantity()
            if value > max_value:
                max_value = value
                best_flower = flower
        return best_flower, max_value

    def __str__(self):
        return (f"Магазин: {self.__name}\n"
                f"Адреса: {self.__adress}\n"
                f"Телефон: {self.__phone}\n"
                f"Рейтинг: {self.rating}★\n"
                f"Статус: {'Відкритий' if self.is_open else 'Закритий'}")

    def __repr__(self):
        return f"FlowerShop(name='{self.__name}', address='{self.__address}', phone='{self.__phone}')"

    def __del__(self):
        print(f"Магазин '{self.__name}' закрито")

class Bouquet:
    def __init__(self, name = "", price = 0.0):
        self.__name = name
        self.__price = abs(price)
        self.__flowers = []
        self.size = "Середній"
        self.quantity = 0

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_flowers(self):
        return self.__flowers

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def add_flower(self, flower, quantity=1):
        for _ in range(quantity):
            self.__flowers.append(flower)
        print(f"Додано {quantity} шт '{flower.get_color()}' до букету '{self.__name}'")
    
    def remove_flower(self, flower):
        if flower in self.__flowers:
            self.__flowers.remove(flower)
            print(f"Видалено квітку '{flower.get_color()}' з букету '{self.__name}'")
        else:
            print(f"Квітка не знайдена в букеті")

    def get_total_flowers(self):
        return len(self.__flowers)

    def calculate_price(self):
        return sum(f.get_price() for f in self.__flowers)

    def __str__(self):
        return (f"Букет: {self.__name}\n"
                f"Ціна: {self.__price} грн\n"
                f"Розмір: {self.size}\n"
                f"Наявність: {self.quantity} шт\n"
                f"Всього квіток: {self.get_total_flowers()} шт")
   
    def __repr__(self):
        return f"Bouquet(name='{self.__name}', price={self.__price})"

    def __del__(self):
        print(f"Букет '{self.__name}' видалено з системи")

def main():
    rose = Flower(height=50, size=10, color="Червона троянда", price=45.50, quantity=100, delivery_rate=50)
    rose.category = "Троянди"
    rose.available = True
    tulip = Flower(height=40, size=8, color="Жовтий тюльпан", price=25.00, quantity=150, delivery_rate=40)
    tulip.category = "Тюльпани"
    tulip.available = True
    lily = Flower(height=60, size=12, color="Біла лілія", price=55.00, quantity=80, delivery_rate=60)
    lily.category = "Лілії"
    lily.available = True

    shop = FlowerShop(name="Квіткова Майстерня", adress="вул. Квіткова, 15", phone="+380 67 123 4567")
    shop.rating = 4.8
    shop.is_open = True

    shop.add_flower(rose)
    shop.add_flower(tulip)
    shop.add_flower(lily)

    bouquet1 = Bouquet(name="Романтичний", price=350.00)
    bouquet1.size = "Великий"
    bouquet1.quantity = 5
    bouquet1.add_flower(rose, 7)
    bouquet1.add_flower(lily, 3)
    
    bouquet2 = Bouquet(name="Весняний", price=250.00)
    bouquet2.size = "Середній"
    bouquet2.quantity = 10
    bouquet2.add_flower(tulip, 10)
    
    bouquet3 = Bouquet(name="Елегантний", price=450.00)
    bouquet3.size = "Преміум"
    bouquet3.quantity = 3
    bouquet3.add_flower(lily, 5)
    bouquet3.add_flower(rose, 5)
    bouquet3.add_flower(tulip, 3)

    print("\n МАГАЗИН:")
    print(shop)
    
    print("\n КВІТКИ В АСОРТИМЕНТІ:")
    print(rose)
    print(tulip)
    print(lily)
    
    print("\n БУКЕТИ:")
    print(bouquet1)
    print(bouquet2)
    print(bouquet3)

    most_expensive = shop.get_most_expensive()
    total_flowers = shop.get_total_quantity()
    best_flower, max_value = shop.get_max_bouquet_value()

    print(f"Найдорожча квітка: {most_expensive.get_color()} - {most_expensive.get_price()} грн")
    print(f"Загальна кількість квіток: {total_flowers} шт")

    print(f"Букет '{bouquet1.get_name()}': ціна {bouquet1.get_price()} грн, "
          f"вартість квіток {bouquet1.calculate_price():.2f} грн")
    print(f"Букет '{bouquet2.get_name()}': ціна {bouquet2.get_price()} грн, "
          f"вартість квіток {bouquet2.calculate_price():.2f} грн")
    print(f"Букет '{bouquet3.get_name()}': ціна {bouquet3.get_price()} грн, "
          f"вартість квіток {bouquet3.calculate_price():.2f} грн")
    print(f"Максимальна вартість букету: {max_value:.2f} грн")
    
if __name__ == "__main__":
    main()