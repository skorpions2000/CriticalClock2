from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from kivymd.app import MDApp
from kivymd.uix.card import MDCard

from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel

KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer


BoxLayout:

    HotReloadViewer:
        size_hint_x: .3
        path: app.path_to_kv_file
        errors: True
        errors_text_color: 1, 1, 0, 1
        errors_background_color: app.theme_cls.bg_dark
'''
class MainScreen(Screen):
    def on_enter(self, *args):
        self.add_widget(MDLabel(text="dsdds"))



class AskView(MDCard):
    text = StringProperty('ask')
    pass


class AnswerView(MDCard):
    pass
    # text = StringProperty('answer')


class AllViewScroll(ScrollView):
    pass


class Content(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    pass


class Example(MDApp):
    path_to_kv_file = "main.kv"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def update_kv_file(self, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)


Example().run()
