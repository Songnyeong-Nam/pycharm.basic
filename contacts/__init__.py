from contacts.controller import Controller
if __name__ == '__main__':

    def print_menu():
        print('0. Exit')
        print('1. Add Contact')
        print('2. Search')
        print('3. Contact List')
        print('4. Delete Contact')
        return input('Menu\n')

    app = Controller()
    while 1:
        menu = print_menu()
        if menu == '1':
            app.register(input('Name\n'),
                        (input('Phone\n')),
                        (input('Email\n')),
                        (input('Addr\n')))

        if menu == '2':
            print(app.search(input('이름\n')))
        if menu == '3':
           print(app.list())

        if menu == '4':
            app.remove(input('name\n'))
        if menu == '0':
            break
