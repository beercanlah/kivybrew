from kivy.app import App
from kivy.uix.widget import Widget


class BrewControl(Widget):
    pass


class BrewApp(App):
    def build(self):
        return BrewControl()


if __name__ == '__main__':
    BrewApp().run()
