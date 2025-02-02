
from faker import Faker


fake = Faker("pl_PL")    # Faker z polska wersja


class Business_card: ## Base Class
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    @property
    def label_length(self):
        """Zwraca długość pełnego imienia i nazwiska (łącznie ze spacją)."""
        return len(self.name + " " + self.surname)

    def __str__(self):
        """Zwraca sformatowaną wizytówkę jako tekst"""
        return f"{self.name} {self.surname}\n{self.email}"


## wizytówka prywatna
class BaseContact(Business_card):
    def __init__(self, private_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.private_phone = private_phone

    def contact(self):
        """Wybiera prywatny numer telefonu."""
        print(f"Wybieram numer {self.private_phone} i dzwonię do {self.name} {self.surname}.")


## wizytówka firmowa
class BusinessContact(Business_card):
    def __init__(self, work_phone, company, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_phone = work_phone
        self.company = company
        self.position = position

    def contact(self):
        """Wybiera służbowy numer telefonu."""
        print(f"Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}.")



# Funkcja do tworzenia losowych wizytówek
def create_contacts(contact_type, quantity):
    """Tworzy losowe wizytówki określonego typu (BaseContact lub BusinessContact)."""
    contacts = []

    for i in range(quantity):
        name = fake.first_name()
        surname = fake.last_name()
        email = fake.email()

        if contact_type == "BaseContact":
            private_phone = fake.phone_number()
            contact = BaseContact(private_phone=private_phone, name=name, surname=surname, email=email)

        elif contact_type == "BusinessContact":
            work_phone = fake.phone_number()
            company = fake.company()
            position = fake.job()
            contact = BusinessContact(work_phone=work_phone, company=company, position=position, name=name, surname=surname, email=email)

        else:
            raise ValueError("Nieznany typ wizytówki! Użyj: 'BaseContact' lub 'BusinessContact'.")

        contacts.append(contact)

    return contacts


## Test funkcji create_contacts
base_contacts = create_contacts("BaseContact", 2)
business_contacts = create_contacts("BusinessContact", 2)


for contact in base_contacts + business_contacts:
    print(contact)
    print(f"Długość imienia i nazwiska ze spacją to: {contact.label_length}")
    contact.contact()
    if isinstance(contact, BusinessContact):
        print(f"Firma: {contact.company}  -  Stanowisko: {contact.position}")
    print("-" * 25)  # Separatory










