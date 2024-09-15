from kivy.lang import Builder

from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRoundFlatIconButton
from kivy.uix.boxlayout import BoxLayout

from kivymd.toast import toast
import os

from views.screen_two.ScreenTwo import ScreenTwoView
from views.utils.editor import Editor

screen_two = ScreenTwoView()
class ImageCutDialog(BoxLayout):
    pass

class ScreenOneView(MDScreen):
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
        self.ed = Editor()
        self.dialog = None

    def reset(self):
        self.output_path = None

    def file_manager_open(self):
        try:
            self.file_manager.show(os.path.expanduser("~"))  # Exibe o gerenciador de arquivos
            self.manager_open = True
        except Exception as e:
            print(f"Erro ao abrir o gerenciador de arquivos: {e}")
            toast("Erro ao abrir o gerenciador de arquivos")

    def select_path(self, path: str):
        '''
        It will be called when you click on the file name
        or the catalog selection button.

        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)
        self.img= path
        self.ed.carregar_imagem(path)
        # ed.carregar_imagem(path)
        self.ids.img_.source = path

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
        self.ed.girar_imagem('anti_horario')
        self.ids.img_.source = self.ed.image_tmp


    def bt_girar_horario(self):
        self.ed.girar_imagem('horario')
        self.ids.img_.source = self.ed.image_tmp

    def exibir_imagem(self):
        self.ed.remover_cor_imagem()
        self.output_path = f'imgs/{self.ed.img_nome}.png'
        img_reload = self.output_path
        self.reset()
        self.ed.carregar_imagem(img_reload)
        self.output_path = img_reload
        print(self.output_path)
        self.ids.img_.source = self.output_path
        screen_two.update_table()
        # self.ed.print_data_csv()

    def exibir_image_with_rentagule_corte(self):
        content = ImageCutDialog()  # Instanciando o widget personalizado

        self.dialog = MDDialog(
            type="custom",
            size_hint=(0.8, 0.4),
            content_cls=content,
            # size_hint=(0.8, 0.4),
            buttons=[
                MDRoundFlatIconButton(
                    text="CANCELAR",
                    on_release=self.fechar_dialog
                ),
                MDRoundFlatIconButton(
                    text="CORTAR",
                    on_release=self.cortar_imagem
                ),
            ],
        )
        self.dialog.open()

    def cortar_imagem(self, *args):
        x = int(self.dialog.content_cls.ids.coordenada_x.text)
        y = int(self.dialog.content_cls.ids.coordenada_y.text)
        self.ed.rec_draw({'x': x, 'y': y})
        self.ids.img_.source = self.ed.image_tmp
        self.dialog.dismiss()

    def fechar_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()

    def data_csv (self, *args):
        self.ed.print_data_csv()
    pass