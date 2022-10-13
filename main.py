import datetime
import random
import pygame
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.screen import Screen

Window.size = (350, 600)

KV = '''
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    MDLabel:
        text: "The Quadratic Alarm"
        font_size: "28sp"
        pos_hint: {"center_y": .935}
        halign: "center"
        bold: True
    MDIconButton:
        icon: "plus"
        pos_hint: {"center_x": .88, "center_y": .06}
        md_bg_color: 0, 0, 0, 1
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        on_release: app.time_picker()
    MDLabel:
        id: alarm_time
        text: ""
        pos_hint: {"center_y": .7}
        halign: "center"
        font_size: "28sp"
        bold: True
    MDLabel:
        text: app.math_problem()
        pos_hint: {"center_y": .4}
        halign: "center"
        font_size: "28sp"
        bold: True
        fon_style: "H2"
    MDTextField:
        id: field
        hint_text: "Answer"
        required: False
        mode: "rectangle"
        helper_text: "Enter Answer"
        halign: "center"
        pos_hint: {"center_y": .3}
    MDRaisedButton:
        text: "Solve"
        pos_hint: {"center_x": .5, "center_y": .2}
        on_release: app.check()
    

'''

# Mobile app - KivyMD
# 1. The Quadratic Alarm: Difficulty Awakening
'''
Most people hit the snooze button when they hear the alarm go off to get extra
sleep minutes. This is a common reason people must get ready in a
hurry and are late. This application solves problems of heavy sleepers.
To turn off the alarm, they will have to complete one tasks, be it a math sum,
rewriting a text, finding a pair for a word, and so on such stimulation guarantees
to wake up the brain.

PLEASE DO KEEP IN MIND THAT THIS IS ONLY A TEMPLATE AND IT IS NOT A COMPLETE AND FULLY FUNCTIONAL
VERSION
'''

# Everything used to install Kivy (this took too long to figure out)
# conda create env
# conda activate kucomp
# install kivy from Pycharm
# install KivyMD via pip
# install pygame via pip


class Alarm(MDApp):
    pygame.init()

    sound = pygame.mixer.Sound("alarm.mp3")
    volume = .5

    screen = Screen()

    dict = {1: " + ",
            2: " - ",
            3: " x "}

    fstr = str(random.randint(1, 12))
    rdict = str(dict[float(random.randint(1, 3))])
    sstr = str(random.randint(1, 12))
    final_string = fstr + rdict + sstr

    def build(self):
        return Builder.load_string(KV)

    def time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time, on_save=self.schedule)
        time_dialog.open()

    def get_time(self, instance, time):
        self.root.ids.alarm_time.text = str(time)

    def schedule(self, *args):
        Clock.schedule_once(self.alarm, 1)

    def check(self, *args):
        print(self.root.ids.field.text)
        if self.rdict == " + ":
            val = int(self.fstr) + int(self.sstr)
            if int(self.root.ids.field.text) == val:
                self.stop()

            else:
                return

        elif self.rdict == " - ":
            val = int(self.fstr) - int(self.sstr)
            if int(self.root.ids.field.text) == val:
                self.stop()

            else:
                return
        elif self.rdict == " x ":
            val = int(self.fstr) * int(self.sstr)
            if int(self.root.ids.field.text) == val:
                self.stop()

            else:
                return
        else:
            print("something went wrong")

    def math_problem(self):
        return self.final_string

    def alarm(self, *args):

        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if self.root.ids.alarm_time.text == str(current_time):
                self.start()
                break

    def set_volume(self, *args):
        self.sound.set_volume(self.volume)
        print(self.volume)

    def stop(self, *args):
        self.sound.stop()
        Clock.unschedule(self.set_volume)
        self.volume = 0

    def start(self, *args):
        self.sound.play(-1)
        self.set_volume()


if __name__ == "__main__":
    Alarm().run()
