import re


class Persona:

    def __init__(self):
        self.__user_id = self
        self.__user_name = self
        self.id_input()
        self.name_input()
        self.print_id()
        self.print_name()

    def id_input(self):

        while True:
            self.__user_id = input('Employee PayRoll Id?: ')

            if not re.match(r"^[a-zA-Z0-9 _]+$", self.__user_id):
                print(f'Employee Id not valid, please enter letters and numbers')
            else:
                break

        return self.__user_id

    def name_input(self):

        while True:
            self.__user_name = input('Employee name?: ')
            if not re.match(r"^[a-zA-Z0-9 _]+$", self.__user_name):
                print(f'Employee Name not valid, please enter letters and numbers')
            else:
                break

        return self.__user_name

    def print_name(self):
        return print(self.__user_name)

    def print_id(self):
        return print(self.__user_id)

    def persona_info(self):
        return self.__user_id, self.__user_name


class Videos:

    #inicializamos con el constructor, atributos y métodos para la app en terminal
    def __init__(self):
        self.__video_title = self
        self.__video_name = self
        self.__video_ext = self
        self.__video_size = self
        self.video_title_input()
        self.video_name_input()
        self.video_ext_input()
        self.video_size_input()
        self.print_title()
        self.print_name()
        self.print_ext()
        self.print_size()

    #Métodos para ingresar mediante input las variables, junto a sus validaciones:
    def video_title_input(self):
        while True:
            self.__video_title = input('Video Title: ')
            if not re.match(r"^[a-zA-Z0-9 _]+$", self.__video_title):
                print(f'Title not valid, please enter letters and numbers')
            else:
                break

        return self.__video_title

    def video_name_input(self):
        while True:
            self.__video_name = input('Video Name: ')
            if not re.match(r"^[a-zA-Z0-9 _]+$", self.__video_name):
                print(f'Name not valid, please enter letters and numbers')
            else:
                break

        return self.__video_name

    def video_ext_input(self):
        while True:
            self.__video_ext = input("Video Extension: ")
            if not re.match(r"^[a-zA-Z0-9 _]+$", self.__video_ext):
                print(f'Extension not valid, please enter letters and numbers')
            else:
                break
        return self.__video_ext

    def video_size_input(self):
        mb = False
        while not mb:
            try:
                self.__video_size = float(input("Video Size (Max 3MB): "))
                # no valid if not in range
                if not 0 <= self.__video_size <= 3:
                    print(f'¡Maximum file size 3MB, Try again!')
                    mb = False
                elif 0 <= self.__video_size <= 3:
                    mb = True

            except ValueError as err:
                print(f'Only numbers are allowed, {err}')
                mb = False

        return self.__video_size

    #Métodos para imprimir las variables de la clase
    def print_title(self):
        return print(self.__video_title)

    def print_name(self):
        return print(self.__video_name)

    def print_ext(self):
        return print(self.__video_ext)

    def print_size(self):
        return print(self.__video_size)

    def videos_info(self):
        return self.__video_title, self.__video_name, self.__video_ext, self.__video_size


#Se crean instancias de Persona y Videos
persona = Persona()
video = Videos()

videos = []

info_persona = persona.persona_info()
info_video = video.videos_info()

#Almacena la info ingresada de la instancia de Persona y Videos cada una en su lista
videos.append([
    info_persona,
    info_video
    ])

for a in videos:
    for b in a:
        for v in b:
            txt_input = open('Salida2.txt', 'a')
            txt_input.write(f'|{v}|')






