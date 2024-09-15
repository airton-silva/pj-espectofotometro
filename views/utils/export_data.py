from os import path
from datetime import date
import csv
from collections import namedtuple


Rgb = namedtuple('Rgb', ['r', 'g', 'b'])
Hsl = namedtuple('Hsl', ['h', 's', 'l'])

_dados={
    "dados":[]
}

class ExportData():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dados = _dados

    def set_dados(self, dados):
        self.dados.append(dados)

    def add_amostra(self, data_colection, amostra, rgb, hsl, proportion):

        if isinstance(rgb, str):
            rgb = tuple(map(int, rgb.split(', ')))
        data = {
            "Amostra": amostra,
            "cor_principal_RGB": rgb,
            "cor_principal_HSL": hsl,
            "Percentual": proportion
        }
        data_colection['amostras'].append(data)

        _dados['dados'].append(data)
    


    def get_data(self):
        _dt =[["Amostra", "R", "G", "B", "Percentual"]]
        for dt in self.dados['dados']:
            row = [
                dt.get('Amostra'),
                dt.get('cor_principal_RGB').r,
                dt.get('cor_principal_RGB').g,
                dt.get('cor_principal_RGB').b,
                dt.get('Percentual')
            ]
            _dt.append(row)

        return _dt
        # return self.convert_data(self.dados['dados'])

    def export_to_csv(self):
        # Define os cabeçalhos do CSV
        filename = 'csv_files/Coleta_'+ str(date.today())+".csv"
       # Cria e escreve no arquivo CSV
        export = self.get_data()

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            for linha in export:
                writer.writerow(linha)
        print(f"Dados exportados para {filename}")

    def old_export_to_csv(data_colection, filename):
        # Define os cabeçalhos do CSV
        fieldnames = ["Amostra", "cor_principal_RGB", "cor_principal_HSL", "Percentual"]

        # Cria e escreve no arquivo CSV
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Escreve o cabeçalho
            writer.writeheader()

            # Escreve cada linha de dados
            for amostra in data_colection['amostras']:
                print(amostra)
                writer.writerow(amostra)

    def print_data(data_colection):
        for amostra in data_colection['amostras']:
            print (amostra)




            
    # def convert_data(self, data):
    #     """Converte a estrutura de dados para o formato da tabela.

    #     Args:
    #         data: A estrutura de dados original.

    #     Returns:
    #         Uma lista de listas representando as linhas da tabela.
    #     """

    #     result = [["Amostra", "R", "G", "B", "Percentual"]]  # Cabeçalho da tabela
    #     print(data)
    #     for item in data:
    #         for amostra in item['amostras']:
    #             row = [
    #                 amostra['Amostra'],
    #                 amostra['cor_principal_RGB'].r,
    #                 amostra['cor_principal_RGB'].g,
    #                 amostra['cor_principal_RGB'].b,
    #                 amostra['Percentual']
    #             ]
    #             result.append(row)

    #     return result