from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """DynamicLabels is a Kivy app to show dynamic label"""
    def __init__(self, **kwargs):
        """construct main app"""
        super().__init__(**kwargs)
        self.names = ['Bob Brown', 'Cat Cyan', 'Oren Ochre']

    def build(self):
        """build kivy GUI"""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.show_name()
        return self.root

    def show_name(self):
        """Output names as Label"""
        for name in self.names:
            # create label for each name in the list
            output_label = Label(text=str(name), id=name)
            # add the label to the 'entries_box" layout widget
            self.root.ids.entries_box.add_widget(output_label)


DynamicLabels().run()
