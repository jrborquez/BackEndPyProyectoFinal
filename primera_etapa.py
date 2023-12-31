import re
import sys
import math

#App for executable
class App:
    #to start Main
    def __init__(self):
        self.main()

    #main method to run the App
    def main(self):

        self.videos = []

        print('-----------------------------')
        print(' Bienvenidos a la App ProGol ')
        print('-----------------------------')
        #While to make the app repeat until it´s done
        exit_app = False

        while not exit_app:
            #Input User Id and validation
            while True:
                self.user_id = input('Employee Id?: ')
                if not re.match(r"^[a-zA-Z0-9 _]+$", self.user_id):
                    print(f'Employee Id not valid, please enter letters and numbers')
                else:
                    break
            # Input User name and validation
            while True:
                self.user_name = input('Employee name?: ')
                if not re.match(r"^[a-zA-Z0-9 _]+$", self.user_name):
                    print(f'Employee Name not valid, please enter letters and numbers')
                else:
                    break
            #Quantity of videos to upload and number validation nothing else
            while True:
                try:
                    self.user_videos_qty = int(input('How many videos would you like to upload?: '))
                except:
                    print(f'Quantity Number not valid, please enter a valid number')
                else:
                    break
            #Round of yes or no, to lead to different points
            y_n = False
            while not y_n:
                msg = (f'Bienvenido {self.user_name}, tu número de nómina es "{self.user_id}" y estás intentando '
                       f'subir {self.user_videos_qty} videos. ¿Es correcta la información?')

                print(msg)

                yes_choices = ['yes', 'y', 'si', 'sipirili', 'yeap']
                no_choices = ['no', 'n', 'nop', 'nope', 'nanchis']

                user_decision = input('Type Yes or No?: ')

                if user_decision.lower() in yes_choices:
                    self.video_info()
                    y_n = True

                elif user_decision.lower() in no_choices:
                    user_decision2 = input(f'Want to Exit the App?(Type Yes or No)')
                    if user_decision2.lower() in no_choices:
                        y_n = True
                    elif user_decision2.lower() in yes_choices:
                        print('Farewell!! See you soon!!')
                        sys.exit()
                    else:
                        print('Answer not valid(2)')
                        y_n = False
                else:
                    print('Answer not valid(3)')

    #Video info method to input Video info
    def video_info(self):

        #Itirate the quantity of times for videos to upload
        for v in range(self.user_videos_qty):
            #input title and validation
            while True:
                video_title = input('Video Title: ')
                if not re.match(r"^[a-zA-Z0-9 _]+$", video_title):
                    print(f'Title not valid, please enter letters and numbers')
                else:
                    break

            # input name and validation
            while True:
                video_name = input('Video Name: ')
                if not re.match(r"^[a-zA-Z0-9 _]+$", video_name):
                    print(f'Name not valid, please enter letters and numbers')
                else:
                    break

            # input title and validation
            while True:
                video_ext = input("Video Extension: ")
                if not re.match(r"^[a-zA-Z0-9 _]+$", video_ext):
                    print(f'Extension not valid, please enter letters and numbers')
                else:
                    break
            # input size of video and validation
            mb = False
            while not mb:
                try:
                    video_size = float(input("Video Size (Max 3MB): "))
                    # no valid if not in range
                    if not 0 <= video_size <= 3:
                        print(f'¡Maximum file size 3MB, Try again!')
                        mb = False
                    elif 0 <= video_size <= 3:
                        mb = True

                except ValueError as err:
                    print(f'Only numbers are allowed, {err}')
                    mb = False
            #to append the info to a list Videos
            self.videos.append([
                video_title,
                video_name,
                video_ext,
                video_size
            ])
        #message that all is done correctly
        return print(f'{self.videos} \n'
                     f'¡¡Saved Successfully!!'
                     ), self.create_txt()

    #Method to create a file to see the info we capture
    def create_txt(self):

        info = f'|{self.user_id} | {self.user_name} | {self.user_videos_qty} | \n'

        txt_file = open('salida.txt', 'a')
        txt_file.write(info)

        #itirate the info in videos so that we can print it in a file
        for v in self.videos:
            for x in v:
                txt_file.writelines(f'| {x} |')

        txt_file.close()

        sys.exit()



