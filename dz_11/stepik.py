
names = ["Alex", "Bob", "Markus", "Peter", "Elise"]
phone_number = ["80293345672", "80297653428", "80338765432", "80291234567", "80333459876"]


def gen_contacts_list() -> dict:
    contacts = dict(zip(names, phone_number))
    return {"contacts_list": contacts}


def search_contacts(contacts: dict, value=None):
    phone_magazine = contacts["contacts_list"]
    for name, phone in phone_magazine.items():
        if name == value or phone == value:
            return f"Calling{name}\n{phone}"
    raise ValueError("Contacts or name is not defined")


print(search_contacts(contacts=gen_contacts_list(), value="Bob"))
