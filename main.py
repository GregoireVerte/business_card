
from faker import Faker


fake = Faker()


class Business_card: ## Base Class
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    @property
    def label_length(self):
        """Zwraca długość pełnego imienia i nazwiska (łącznie ze spacją)."""
        return len(self.name + " " + self.surname)



class BaseContact(Business_card):
    def __init__(self, private_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.private_phone = private_phone

    def contact(self):
        """Wybiera prywatny numer telefonu."""
        print(f"Wybieram numer {self.private_phone} i dzwonię do {self.name} {self.surname}.")



class BusinessContact(Business_card):
    def __init__(self, work_phone, company, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_phone = work_phone
        self.company = company
        self.position = position

    def contact(self):
        """Wybiera służbowy numer telefonu."""
        print(f"Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}.")














