phone_book = {}

print("""
Twoje Kontakty:
1 - dodaj kontakt
2 - Usuń kontakt
3 - Wyszuaj kontakt
4 - Zmodyfikj kontakt
5 - Wyświetl wszytskie kontakty
6 - Wyjdź z zakładki kontakty
""")

def add_new_contact():
    name = input("Proszę podaj nazwę kontaktu do dodania: ")
    if name in phone_book:
        print("Podany kontakt już istnieje!")
    else:
        phone = input("Proszę podaj numer telefonu do dodania: ")
        phone_book[name] = phone
        print("Kontakt został dodany!")


def delete_contact():
    name = input("Proszę podaj nazwę kontaktu do usunięcia: ")
    if name in phone_book:
        del phone_book[name]
        print("Kontakt został usunięty!")
    else:
        print("Podany konakt nie istnieje!")

def search_contact():
    name = input("Proszę podaj nazwę kontaktu do wyszukania: ")
    if name in phone_book:
        print("Numer telefonu:", phone_book[name])
    else:
        print("Podany kontakt nie istnieje!")


def modify_contact():
    name = input("Proszę podaj nazwę kontaktu do modyfikacji: ")
    if name in phone_book:
        phone = input("Proszę podaj numer telefonu: ")
        phone_book[name] = phone
        print("Kontakt został zmodyfikowany!")


def show_contact():
    if len(phone_book) == 0:
        print("Brak zapisanych kontaktów.")
    else:
        for key, value in phone_book.items():
            print(key, value)

while True:
    option = int(input("Proszę wybierz opcję (1-6): "))

    if option == 1:
        add_new_contact()
    elif option == 2:
        delete_contact()
    elif option == 3:
        search_contact()
    elif option == 4:
        modify_contact()
    elif option == 5:
        show_contact()
    elif option == 6:
        print("Wychodzę z kontaktów!")
        break
    else:
        print("Funkcja niedozwolona!")