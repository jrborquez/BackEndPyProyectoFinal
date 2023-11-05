import re

class Validate:

    def __init__(self, x, msg):
        self.__x = x
        self.__msg = msg

    #Validar Número:
    def num(self, x, msg):
        while True:
            try:
                self.user_id = int(input('Employee number?: '))
            except:
                print(f'Employee Number not valid, please enter a valid number')
            else:
                break

    #Validar Números y Letras sin espacio:


    #Validar
