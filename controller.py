import model
import view

def run():
    view.greatings()
    while True:
        view.menu()
        answer = input('Ответ:')
        if answer == '1':
            date = model.read_phonebook()
            view.show_phonebook(date)

        elif answer == '2':
            model.add_contact()

        elif answer == '3':
            model.search_contacts()

        elif answer == '4':
            model.delete_contact()

        elif answer == '5':
            model.edit_contact()
        elif answer == '6':
            break