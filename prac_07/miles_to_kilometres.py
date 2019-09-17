from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETRE = 1.60934


class MilesToKilometresApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_convert(self, text):
        print("handle calc")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_change(self, text, change):
        print("handle inc")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * MILES_TO_KILOMETRE)

    @staticmethod
    def convert_to_number(text):
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


MilesToKilometresApp().run()