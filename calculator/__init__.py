from calculator.controller import Controller

if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. Calculator')
        return input('Menu\n')
    app = Controller()


    while 1:
        menu = print_menu()
        if menu == '0': break
        if menu == '1':
            app = Controller()
            print('Start Calculator')
            num1 = int(input('First No\n'))
            opcode = input('operator\n')
            num2 = int(input('Second No\n'))

            result = app.calc(num1, num2, opcode)
            print('result : %d' % result)
