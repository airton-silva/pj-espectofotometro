from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screenmanager import MDScreenManager

from views.main_screen.MainScreenView import MainScreenView


Window.size = (360, 740)  # Resolução do Samsung Galaxy S8
class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        self.sm = MDScreenManager()

    def build(self):
        self.theme_cls.material_style='M3'
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette='Blue'

        self.sm.add_widget(MainScreenView())
        return self.sm

    def change_theme(self, theme):
        self.theme_cls.primary_palette = theme


        

MainApp().run()
