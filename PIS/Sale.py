import json

class Sale:
    def __init__(self, sale_id=None, client_id=None, tour_id=None, final_price=0.0,
                 sale_date=None, base_price=0.0, discount=0.0, data=None):
        self.__sale_id = sale_id
        self.__client_id = client_id
        self.__tour_id = tour_id
        self.__final_price = final_price
        self.__sale_date = None
        self.__base_price = 0.0
        self.__discount = 0.0
        if data is not None:
            self.from_str(data)
        elif client_id is not None and tour_id is not None and sale_date is not None:
            self.set_client_id(client_id)
            self.set_tour_id(tour_id)
            self.set_sale_date(sale_date)
            self.set_base_price(base_price)
            self.set_discount(discount)

    def get_sale_id(self):
        return self.__sale_id

    def get_client_id(self):
        return self.__client_id

    def get_tour_id(self):
        return self.__tour_id

    def get_final_price(self):
        return self.__final_price

    def get_sale_date(self):
        return self.__sale_date

    def get_base_price(self):
        return self.__base_price

    def get_discount(self):
        return self.__discount

    @staticmethod
    def is_valid_id(id):
        return id is not None and id > 0

    @staticmethod
    def is_valid_price(price):
        return price > 0

    @staticmethod
    def is_valid_date(date):
        return date is not None and date.strip() != ""

    @staticmethod
    def is_valid_discount(discount):
        return discount >= 0

    def set_sale_id(self, sale_id):
        self.__sale_id = sale_id

    def set_client_id(self, client_id):
        if not Sale.is_valid_id(client_id):
            raise ValueError("ID клиента должно быть положительным числом")
        self.__client_id = client_id

    def set_tour_id(self, tour_id):
        if not Sale.is_valid_id(tour_id):
            raise ValueError("ID тура должно быть положительным числом")
        self.__tour_id = tour_id

    def set_final_price(self, final_price):
        if final_price < 0:
            raise ValueError("Итоговая цена не может быть отрицательной")
        self.__final_price = final_price

    def set_sale_date(self, sale_date):
        if not Sale.is_valid_date(sale_date):
            raise ValueError("Дата продажи не должна быть пустой")
        self.__sale_date = sale_date

    def set_base_price(self, base_price):
        if not Sale.is_valid_price(base_price):
            raise ValueError("Стоимость должна быть положительная")
        self.__base_price = base_price
        self.calculate_final_price()

    def set_discount(self, discount):
        if not Sale.is_valid_discount(discount):
            raise ValueError("Скидка не может быть отрицательной")
        self.__discount = discount
        self.calculate_final_price()

    def from_str(self, data):
        data = data.strip()
        if data.startswith("{"):
            data_dict = json.loads(data)
            self.set_client_id(data_dict["clientId"])
            self.set_tour_id(data_dict["tourId"])
            self.set_sale_date(data_dict["saleDate"])
            self.set_base_price(data_dict["basePrice"])
            self.set_discount(data_dict["discount"])
        else:
            parts = data.split(",")
            self.set_client_id(int(parts[0]))
            self.set_tour_id(int(parts[1]))
            self.set_sale_date(parts[2])
            self.set_base_price(float(parts[3]))
            self.set_discount(float(parts[4]))

    def short_version(self):
        return shortSale.short(self)

    def get_long_info(self):
        return (f"(sale_id={self.__sale_id}, client_id={self.__client_id}, "
                f"tour_id={self.__tour_id}, sale_date='{self.__sale_date}', "
                f"base_price={self.__base_price}, discount={self.__discount}, "
                f"final_price={self.__final_price})")

    def is_equal(self, obj):
        if not isinstance(obj, Sale):
            return False
        return (self.__client_id == obj.__client_id and
                self.__tour_id == obj.__tour_id and
                self.__sale_date == obj.__sale_date and
                self.__base_price == obj.__base_price and
                self.__discount == obj.__discount and
                self.__final_price == obj.__final_price)

    def calculate_final_price(self):
        res = self.__base_price - self.__discount
        if res < 0:
            res = 0.0
        self.set_final_price(res)


class shortSale(Sale):
    def __init__(self, sale_id=None, client_id=None, tour_id=None, final_price=0.0):
        super().__init__(sale_id=sale_id, client_id=client_id, tour_id=tour_id, final_price=final_price)
        self.__sale_id = sale_id
        self.__client_id = client_id
        self.__tour_id = tour_id
        self.__final_price = final_price

    @classmethod
    def short(cls, sale):
        return cls(sale.get_sale_id(),
                   sale.get_client_id(),
                   sale.get_tour_id(),
                   sale.get_final_price())

    def get_info(self):
        if self.__sale_id is not None:
            return f"#{self.__sale_id}: клиент {self.__client_id}, тур {self.__tour_id}, сумма: {self.__final_price} руб."
        else:
            return f"клиент {self.__client_id}, тур {self.__tour_id}, сумма: {self.__final_price} руб."


# Тестирование
sale1 = Sale()
sale1.set_client_id(123)
sale1.set_tour_id(456)
sale1.set_sale_date("2025-12-12")
sale1.set_base_price(1000.00)
sale1.set_discount(100.00)
print("Итоговая цена: ", sale1.get_final_price())

print("Конструктор с параметрами: ")
sale2 = Sale(client_id=123, tour_id=456,sale_date="2025-12-12",base_price=1000, discount=100)
print("Итоговая цена: ", sale2.get_final_price())

print("Конструктор из строки: ")
sale3 = Sale(data = "123,456,2025-12-12,500,300")
print("Итоговая цена: ", sale3.get_final_price())


print("Конструктор из json: ")
str = (
    '{"clientId": 123, '
       '"tourId": 456, '
       '"saleDate": "2024-12-12", '
       '"basePrice": 3000, '
       '"discount": 100}'
)
sale4 = Sale(data = str)
print("Итоговая цена: ", sale4.get_final_price())

print("Полная информация:")
print(sale1.get_long_info())
print("\nКороткая версия ")
short_sale = shortSale.short(sale1)
print("Вывод -", short_sale.get_info())
print("Продажи равны? ", sale1.is_equal(sale2))
