from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.button import Button
from datetime import datetime
from kivy.uix.dropdown import DropDown

Config.set("graphics", "resizable", "1")
Config.set("graphics", "width", "800")
Config.set("graphics", "height", "600")
Config.set("graphics", "background-color", "red")
Window.clearcolor = (1,1,1,1)

current_time = "Getting data"
towns = ["Москва","Астраханская область,Самарская область,\nУдмуртская республика,Ульяновская область"]
buttons_towns = []
towns_times = 0
def get_time(label_time, period):
        global towns
        global towns_times


        current_time = ""
        old_time = str(datetime.now()).split()[1][:8].split(":")
        old_time[0] = str((int(old_time[0]) + towns_times) % 24)
        if int(old_time[0]) < 10:
            old_time[0] = "0" + old_time[0]
        for i in range(len(old_time) - 1):
            current_time += old_time[i] + ":"
        current_time += old_time[-1]
        label_time.text = current_time
        Clock.schedule_once(lambda _: get_time(label_time, period), period)


class MyApp(App):
    global towns_times

    def HideWidgets(self, instance):
        global towns_times
        self.label_time.pos = (9999, 9999)
        self.chos_but.pos = (9999, 9999)
        self.just_text.pos = (9999, 9999)
        self.two_but.pos = (0, 440)
        self.three_but.pos = (0, 400)
        self.four_but.pos = (0, 360)
        self.five_but.pos = (0, 320)
        self.six_but.pos = (0, 280)
        self.seven_but.pos = (0, 240)
        self.eight_but.pos = (0, 200)
        self.nine_but.pos = (0, 160)
        self.ten_but.pos = (0, 120)
        self.eleven_but.pos = (0, 80)
        self.twelve_but.pos = (0, 40)

    def cur_timing(self, instance):
        global towns_times
        if "-1" in instance.text:
            towns_times = -1
        elif "0" in instance.text:
            towns_times = 0
        elif "+1" in instance.text:
            towns_times = 1
        elif "+2" in instance.text:
            towns_times = 2
        elif "+3" in instance.text:
            towns_times = 3
        elif "+4" in instance.text:
            towns_times = 4
        elif "+5" in instance.text:
            towns_times = 5
        elif "+6" in instance.text:
            towns_times = 6
        elif "+7" in instance.text:
            towns_times = 7
        elif "+8" in instance.text:
            towns_times = 8
        elif "+9" in instance.text:
            towns_times = 9
        self.label_time.pos = (0, 0)
        self.chos_but.pos = (0, 0)
        self.just_text.pos = (0, 0)
        self.two_but.pos = (9999, 9999)
        self.three_but.pos = (9999, 9999)
        self.four_but.pos = (9999, 9999)
        self.five_but.pos = (9999, 9999)
        self.six_but.pos = (9999, 9999)
        self.seven_but.pos = (9999, 9999)
        self.eight_but.pos = (9999, 9999)
        self.nine_but.pos = (9999, 9999)
        self.ten_but.pos = (9999, 9999)
        self.eleven_but.pos = (9999, 9999)
        self.twelve_but.pos = (9999, 9999)


    def build(self):
        self.label_time = Label(text=current_time, font_size="60", size_hint=(1, 1.2), color=(1, 0, 0, 1))
        self.just_text = Label(text="Choose Your Time", font_size="20", size_hint=(1, 1.8), color=(0, 0, 0, 1), valign="middle")
        self.chos_but = Button(text="Выбрать пояс", font_size="20", size_hint=(1, .10), on_press=self.HideWidgets)

        self.two_but = Button(text="Калинград -1", font_size="12", size_hint=(1, .065), pos=(9999, 9999), on_press=self.cur_timing)
        self.three_but = Button(text="Москва +0", font_size="12", size_hint=(1, .065), pos=(9999,9999), on_press=self.cur_timing)
        self.four_but = Button(text="Самара +1", font_size="12", size_hint=(1, .065), pos=(9999, 9999), on_press=self.cur_timing)
        self.five_but = Button(text="Екатеринбург +2", font_size="12", size_hint=(1, .065), pos=(9999, 9999), on_press=self.cur_timing)
        self.six_but = Button(text="Омск +3", font_size="12", size_hint=(1, .065), pos=(9999, 9999), on_press=self.cur_timing)
        self.seven_but = Button(text="Красноярск +4", font_size="12", size_hint=(1, .065), pos=(9999, 9999), on_press=self.cur_timing)
        self.eight_but = Button(text="Иркутск +5", font_size="12", size_hint=(1, .065), pos=(9999, 9999), on_press=self.cur_timing)
        self.nine_but = Button(text="Якутск +6", font_size="12", size_hint=(1, .065), pos=(9999, 9999), on_press=self.cur_timing)
        self.ten_but = Button(text="Владивосток +7", font_size="12", size_hint=(1, .065), pos=(9999, 9999), on_press=self.cur_timing)
        self.eleven_but = Button(text="Магадан +8", font_size="12", size_hint=(1, .065), pos=(9999, 9999), on_press=self.cur_timing)
        self.twelve_but = Button(text="Камчатка +9", font_size="12", size_hint=(1, .065), pos=(9999, 9999), on_press=self.cur_timing)

        FloatToLabel = FloatLayout(size = (800,600))
        FloatToLabel.add_widget(self.label_time)
        FloatToLabel.add_widget(self.just_text)
        FloatToLabel.add_widget(self.chos_but)

        FloatToLabel.add_widget(self.two_but)
        FloatToLabel.add_widget(self.three_but)
        FloatToLabel.add_widget(self.four_but)
        FloatToLabel.add_widget(self.five_but)
        FloatToLabel.add_widget(self.six_but)
        FloatToLabel.add_widget(self.seven_but)
        FloatToLabel.add_widget(self.eight_but)
        FloatToLabel.add_widget(self.nine_but)
        FloatToLabel.add_widget(self.ten_but)
        FloatToLabel.add_widget(self.eleven_but)
        FloatToLabel.add_widget(self.twelve_but)

        get_time(self.label_time, period=1)
        return FloatToLabel




if __name__ == "__main__":
    MyApp().run()









