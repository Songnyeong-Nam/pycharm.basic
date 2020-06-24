class Service:
    def __init__(self):
        self._contacts = []


    def add_contact(self, payload):
        self._contacts.append(payload)

    def get_contact(self, payload): #name
        for i in self._contacts:
            if payload == i.name:
                return i

    def get_contacts(self) -> []:
        contacts = []
        for i in self._contacts:
            contacts.append(i.to_string)
        return ' '.join(contacts) #text mining 에 사용된다.

    def del_contact(self, payload): #name
        for i, t in enumerate(self._contacts): #객체와 index를 바로 뽑아냄
            if payload == t.name:
                del self._contacts[i]
