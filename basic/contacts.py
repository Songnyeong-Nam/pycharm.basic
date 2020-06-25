class Model:
    def __init__(self):
        self._name = ''
        self._phone = ''
        self._email = ''
        self._addr = ''

    @property
    def name(self) -> str: return self._name
    @name.setter
    def name(self, name): self._name = name
    @property
    def phone(self) -> str: return self._phone
    @phone.setter
    def phone(self, phone): self._phone = phone
    @property
    def email(self) -> str: return self._email
    @email.setter
    def email(self, email): self._email
    @property
    def addr(self) -> str: return self._addr
    @addr.setter
    def addr(self, addr): self._addr

    def __str__(self):
        return self._name + ',' + self._phone + ',' + self._email + ',' +self._addr

    def to_string(self) -> str:
        return 'name : {}, Phone : {}, Email : {}, Addr: {}'\
            .format(self._name, self._phone, self._email)

class Service:
    def __init__(self):
        self._contacts = []

    def add_contact(self, payload):
        self._contacts.append(payload)

    def get_contact(self, payload):  # name
        for i in self._contacts:
            if payload == i.name:
                return i

    def get_contacts(self) -> []:
        contacts = []
        for i in self._contacts:
            contacts.append(i.to_string)
        return ' '.join(contacts)  # text mining 에 사용된다.

    def del_contact(self, payload):  # name
        for i, t in enumerate(self._contacts):  # 객체와 index를 바로 뽑아냄
            if payload == t.name:
                del self._contacts[i]

class Controller:
    def __init__(self):
        self._service = Service()

    def register(self, name, phone, email, addr):
        model = Model()
        model.name = name
        model.phone = phone
        model.email = email
        model.addr = addr
        self._service.add_contact(model)

    def search(self, name) -> object:
        return self._service.get_contact(name)

    def list(self) -> []:
        self._service.get_contacts()

    def remove(self, name):
        self._service.del_contact(name)


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
