from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivy.clock import Clock

from views.utils.export_data import ExportData


class TableScreen(Screen):
    pass

class ScreenTwoView(MDScreen):
   
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.export_data = ExportData()  # Create an instance of ExportData
        self.dados = self.export_data.get_data()
        self.create_table()

    def create_table(self):

        # # Criando a tabela
        
        self.data_table = MDDataTable(
            size_hint=(1, 0.6),
            pos_hint={"center_x": 0.5, "center_y": 0.57},
            use_pagination=True,
            column_data=[
                ("Amostra", dp(20)),
                ("R", dp(10)),
                ("G", dp(10)),
                ("B", dp(10)),
                ("H", dp(10)),
                ("S", dp(10)),
                ("H", dp(10)),
                ("Percentual", dp(20)),
            ],
            row_data=self.dados[1:] ,  # Ignora a primeira linha (cabeçalho)
        )

        self.add_widget(self.data_table)


    def update_table(self, *args):
        # Atualiza os dados e recria a tabela
        self.dados = self.export_data.get_data()
        self.create_table()

    def export_csv(self):
        self.export_data.export_to_csv()
        pass


