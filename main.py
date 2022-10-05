from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.pickers import MDTimePicker
import datetime
import pygame

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
        pos_hint: {"center_y": .5}
        halign: "center"
        font_size: "28sp"
        bold: True
    MDRaisedButton:
        text: "Solve"
        pos_hint: {"center_x": .5, "center_y": .4}
    
'''

# Mobile app - Kivy probably
# 1. The Quadratic Alarm: Difficulty Awakening
'''
Most people hit the snooze button when they hear the alarm go off to get extra
sleep minutes. This is a common reason people must get ready in a
hurry and are late. This application solves problems of heavy sleepers.
To turn off the alarm, they will have to complete one tasks, be it a math sum,
rewriting a text, finding a pair for a word, and so on such stimulation guarantees
to wake up the brain.
'''


# Everything used to install Kivy (this took too long to figure out)
# conda create env
# conda activate kucomp
# install kivy from Pycharm
# install KivyMD by pip


class Alarm(MDApp):

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

    def alarm(self, *args):
        i = 0
        while i == 0:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if self.root.ids.alarm_time.text == str(current_time):
                print("Alarm!")
            i += 1


if __name__ == "__main__":
    Alarm().run()
