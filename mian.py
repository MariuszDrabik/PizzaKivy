from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from models import Pizza


class PizzaWidget(BoxLayout):
    pass


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza("4 cheese", "Mozzarella, emental, brie, blue cheese", 34, True),
            Pizza("Pepperoni", "Mozzarella, peproni", 28.5, False),
            Pizza("Hawaii", "Mozzarella, ham, ananas", 30.5, False),
        ]


class PizzaApp(App):
    pass


if __name__ == '__main__':
    PizzaApp().run()
