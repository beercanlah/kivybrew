from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

# For now path to ardumashtun is hard coded, sorry
import sys
sys.path.append('../ardumashtun/python')

from ardumashtun import UnoMashtun


class BrewControl(Widget):
    temperature = NumericProperty(0)


class BrewApp(App):
    def build(self):
        return BrewControl()


if __name__ == '__main__':
    BrewApp().run()
