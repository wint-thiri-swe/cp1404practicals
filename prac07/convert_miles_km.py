from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_TO_KM = 1.609


class MilesConverter(App):
    """MilesConverter is a kivy app to convert miles to km"""
    miles = StringProperty()

    def build(self):
        """build Kivy app from the kv file"""
        Window.size = (350, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.handle_convert()
        return self.root

    def handle_convert(self):
        """handle conversion calculation by button and print output as label"""
        miles = self.handle_error()
        result = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """handle up/down button, update text input with new value, called calculation function"""
        miles = self.handle_error() + increment
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def handle_error(self):
        """handle error of input, return 0 when invalid, return input back when valid"""
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0


MilesConverter().run()
