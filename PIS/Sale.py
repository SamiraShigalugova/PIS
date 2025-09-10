class Sale:
    def __init__(self):
        self.sale_id = None
        self.client_id = None
        self.tour_id = None
        self.sale_date = None
        self.base_price = 0.0
        self.discount = 0.0
        self.final_price = 0.0



    @staticmethod
    def is_valid_id(id):
        return id is not None and id>0
    @staticmethod
    def is_valid_date(date):
        return date is not None and date.strip()!= ""
    @staticmethod
    def is_valid_price(price):
        return price > 0
    @staticmethod
    def is_valid_discount(discoint):
        return discoint>=0

    
    def get_sale_id(self):
        return self.sale_id
    def get_client_id(self):
        return self.client_id
    def get_tour_id(self):
        return self.tour_id
    def get_sale_date(self):
        return self.sale_date
    def get_base_price(self):
        return self.base_price
    def get_discount(self):
        return self.discount
    def get_final_price(self):
        return self.final_price



    def set_sale_id(self, sale_id):
        self.sale_id = sale_id
        def set_client_id(self, client_id):
        if not Sale.is_valid_id(client_id):
            raise ValueError("ID клиента должно быть положительным числом")
        self.client_id = client_id


    def set_tour_id(self, tour_id):
        if not Sale.is_valid_id(tour_id):
            raise ValueError("ID тура должно быть положительным числом")
        self.tour_id = tour_id

    def set_sale_date(self, sale_date):
        if not Sale.is_valid_date(sale_date):
            raise ValueError("Дата продажи не должна быть пустой")
        self.sale_date = sale_date

    def set_base_price(self, base_price):
        if not Sale.is_valid_price(base_price):
            raise ValueError("Стоимость должна быть положительная")
        self.base_price = base_price
        self.calculate_final_price()

    def set_discount(self, discount):
        if not Sale.is_valid_discount(discount):
            raise ValueError("Скидка не может быть отрицательной")
        self.discount = discount
        self.calculate_final_price()

    def calculate_final_price(self):
        res = self.base_price - self. discount
        if res<0:
            res = 0.0
        self.final_price = res

sale = Sale()
sale.set_client_id(123)
sale.set_tour_id(456)
sale.set_sale_date("2025-12-12")
sale.set_base_price(1000.00)
sale.set_discount(100.00)

print("Итоговая цена: ", sale.get_final_price())
