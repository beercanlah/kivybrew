from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, BooleanProperty
from kivy.clock import Clock

# For now path to ardumashtun is hard coded, sorry
import sys
sys.path.append('../ardumashtun/python')

from ardumashtun import UnoMashtun


class BrewControl(Widget):
    temperature = NumericProperty(0)
    pump_status = BooleanProperty(False)

    mashtun = UnoMashtun('/dev/tty.usbmodem1411')

    def update(self, dt):
        self.temperature = self.mashtun.temperature
        self.pump_status = self.mashtun.pump

    def toggle_pump(self):
        self.mashtun.pump = not self.mashtun.pump


class BrewApp(App):
    def build(self):
        control = BrewControl()
        Clock.schedule_interval(control.update, 1.0)
        return control


if __name__ == '__main__':
    BrewApp().run()
