from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
# from kivy.uix.scatter import Scatter
# from kivy.uix.label import Label
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.textinput import TextInput


#if the file name is not 'MyApp.kv'
# import library 'kivy.lang.builder' with the name of your file.
# Example Builder.load_file('name.kv')
Builder.load_file('my.kv')


class ScatterTextWidget(BoxLayout):
    pass


class TutorialApp(App):

    # def build(self):
    #     b = BoxLayout(orientation='vertical')
    #     t = TextInput(font_size=50,
    #                   size_hint_y=None,
    #                   height=75,
    #                   text='Hello, world!')
    #     f = FloatLayout()
    #     s = Scatter()
    #
    #     l = Label(text='Hello, world!',
    #                   font_size=50)
    #     t.bind(text=l.setter('text'))
    #
    #     f.add_widget(s)
    #     s.add_widget(l)
    #
    #     b.add_widget(t)
    #     b.add_widget(f)
    #     return b
    def build(self):
        return ScatterTextWidget()


if __name__ == '__main__':
    TutorialApp().run()
