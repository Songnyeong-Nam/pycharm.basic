from calculator.model import Model
from calculator.service import Service

class Controller:

    def calc(self, num1, num2, opcode):
        model = Model()
        model.num1 = num1
        model.num2 = num2
        model.opcode = opcode
        service = Service(model)
        if opcode == '+': result = service.plus()
        if opcode == '-': result = service.minus()
        if opcode == '*': result = service.multiply()
        if opcode == '/': result = service.divide()

        return result
