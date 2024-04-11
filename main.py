from io import BytesIO
import os

from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

from editor import ed

Window.size = (360, 740)  # Resolução do Samsung Galaxy S8

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Analizador de Imagens"
        left_action_items: [["menu", lambda x: None]]
        elevation: 3

    MDFloatLayout:

        MDRoundFlatIconButton:
            text: "Carregar Imagem"
            focus_behavior: True
            icon: "folder"
            elevation: 6
            pos_hint: {"center_x": .5, "center_y": .9}
            on_release: app.file_manager_open()  

        MDCard:
            size_hint: .7, .550            
            focus_behavior: True
            pos_hint: {"center_x": .5, "center_y": .55}
            md_bg_color: "darkgrey"
            focus_color: "grey"            
            Image:
                id: img_
                # size_hint: .5, .5
                pos_hint: {"center_x": .5, "center_y": .5}
                allow_stretch:True

        # New layout for action buttons
        MDBoxLayout:
            
            size_hint: .7, .1  # Adjust size as needed
            pos_hint: {"center_x": .5, "center_y": .220}  # Adjust position
            
            MDRoundFlatIconButton:
                text: "Girar"
                icon: "rotate-left"
                size_hint_x: .3
                pos_hint: {"center_x": .3, "center_y": .5}
                on_release: app.bt_girar_anti_horario()

            MDRoundFlatIconButton:
                text: "Girar"
                icon: "rotate-right"
                size_hint_x: .3
                pos_hint: {"center_x": .6, "center_y": .5}
                on_release: app.bt_girar_horario()


        MDBoxLayout:
            # md_bg_color: "darkgrey"
            size_hint: .7, .1  # Adjust size as needed
            pos_hint: {"center_x": .5, "center_y": .140}  # Adjust position

            MDRoundFlatIconButton:
                text: "Processar"
                icon: "image-check"
                size_hint_x: .3
                pos_hint: {"center_x": .3, "center_y": .5}
                on_release: app.exibir_imagem()

            MDRoundFlatIconButton:
                text: "Salvar"
                icon: "content-save"
                size_hint_x: .3
                pos_hint: {"center_x": .6, "center_y": .5}
                on_release: app.salvar_imagem()                
   

            
'''


class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.img = None
        self.output_path = ""
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path,
            preview=True,
        )

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def select_path(self, path: str):
        '''
        It will be called when you click on the file name
        or the catalog selection button.

        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)
        self.img= path
        ed.carregar_imagem(path)
        self.root.ids.img_.source = path

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def bt_girar_anti_horario(self):
        ed.girar_imagem('anti_horario')
        self.root.ids.img_.source = ed.rotate_img


    def bt_girar_horario(self):
        ed.girar_imagem('horario')
        self.root.ids.img_.source = ed.rotate_img

    def exibir_imagem(self):
        ed.remover_cor_imagem()
        self.output_path = f'imgs/{ed.img_nome}.png'
        self.root.ids.img_.source = self.output_path






App().run()
