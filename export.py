from os import path
from datetime import date

class export_data():
    data_csv = {
        'name_file': 'Coleta'+ str(date.today()),
        'data':{}
    }

    
    def export_to_csv(self, data):
        self.data_csv['data'] = data
        # print("--"*10 + "\n")
        # print( self.data_csv)
        # print("--"*10 + "\n")

    def print_data(self):
        return self.data_csv
