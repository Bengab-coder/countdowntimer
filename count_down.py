from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, BooleanProperty, StringProperty
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

Builder.load_file('down.kv')

sound = SoundLoader.load('alert.wav')


class MyLayout(Widget):
    global sound
    var = NumericProperty(0)
    count = StringProperty()
    do = BooleanProperty()

    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.val1 = 0
        self.val2 = 0
        self.val3 = 0
        self.val4 = 0
        self.do = False
        self.b = False
        self.min, self.sec =(0,0)
        self.play_sound_at_startup = False

        Clock.schedule_interval(self.get_time, 1)
        self.count = "00:00"
        self.get_time(0)

    def start(self):
        if self.var > 0:
            self.do = True
            self.b = True

    def stop(self):
        self.do = False
        self.b = True

    def reset(self):
        self.do = False
        self.var = 0
        self.count = "00 : 00"
        self.b = False
   

    def clicked1(self, btn):
        self.val1 = btn

    def clicked2(self, btn2):
        self.val2 = btn2

    def clicked3(self, btn3):
        self.val3 = btn3

    def clicked4(self, btn4):
        self.val4 = btn4

    def get_time(self, interval):
        if self.var < 0 and self.play_sound_at_startup :
            self.do = False
            #self.play=True
            if sound :#and self.play:
                #self.play=True
                sound.play()
        self.play_sound_at_startup = True

        if not self.do and self.b == False:
            self.thetwo = int(f"{self.val1}{self.val2}")
            self.thelast = int(f"{self.val3}{self.val4}")
            self.var = (self.thetwo * 60) + self.thelast

        elif self.do:
            self.min, self.sec = divmod(self.var, 60)
            self.count = "{:02d} : {:02d}".format(self.min, self.sec)
            self.var -= 1


class MyApp(App):
    def build(self):
        Window.clearcolor = (1,0,0,1)
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
