from os import path
from datetime import date
import csv

class export_data():
    data_csv = {
        'name_file': 'Coleta_'+ str(date.today()),
        'amostras':[]
    }

    def add_amostra(data_colection, amostra, rgb, hsl, proportion):
        data = {
            "Amostra": amostra,
            "cor_principal_RGB": rgb,
            "cor_principal_HSL": hsl,
            "Percentual": proportion
        }
        data_colection['amostras'].append(data)

    def export_to_csv(data_colection, filename):
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
            
