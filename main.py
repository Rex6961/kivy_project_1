from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

# import random for to use random colores

#if the file name is not 'MyApp.kv'
# import library 'kivy.lang.builder' with the name of your file.
# Example Builder.load_file('name.kv')
Builder.load_file('my.kv')


class ScatterTextWidget(BoxLayout):
    pass
    # to use code for random colores or another to use code in my.kv file
    # def change_label_colour(self, *args):
    #     a = random.random()
    #     colour = [random.random() for i in range(3)] + [a + 0.3 if a < 0.4 else a]
    #     label = self.ids['my_label']
    #     label.color = colour


class TutorialApp(App):

    def build(self):
        return ScatterTextWidget()


if __name__ == '__main__':
    TutorialApp().run()
