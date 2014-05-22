from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, BooleanProperty
from kivy.clock import Clock
import re

# For now path to ardumashtun is hard coded, sorry
import sys
sys.path.append('../ardumashtun/python')

from ardumashtun import UnoMashtun


class FloatInput(TextInput):

    pat = re.compile('[^0-9]')
    multiline = False
    halign = 'center'

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class BrewControl(Widget):
    temperature = NumericProperty(0)
    pump_status = BooleanProperty(False)
    pid_status = BooleanProperty(False)
    heater_status = BooleanProperty(False)
    setpoint = NumericProperty(0)
    p_value = NumericProperty(0)
    i_value = NumericProperty(0)

    mashtun = UnoMashtun('/dev/tty.usbmodem1411')

    def update(self, dt):
        self.temperature = self.mashtun.temperature
        self.heater_status = self.mashtun.heater
        self.pump_status = self.mashtun.pump
        self.pid_status = self.mashtun.pid
        self.setpoint = self.mashtun.setpoint
        self.p_value = self.mashtun.p_value
        self.i_value = self.mashtun.i_value

    def toggle_pump(self):
        self.mashtun.pump = not self.mashtun.pump

    def toggle_pid(self):
        self.mashtun.pid = not self.mashtun.pid

    def set_setpoint(self, value):
        self.mashtun.setpoint = value

    def set_p_value(self, value):
        self.mashtun.p_value = value

    def set_i_value(self, value):
        self.mashtun.i_value = value


class BrewApp(App):
    def build(self):
        control = BrewControl()
        Clock.schedule_interval(control.update, 1.0)
        return control


if __name__ == '__main__':
    BrewApp().run()
