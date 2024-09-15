from collections import namedtuple

Rgb = namedtuple('Rgb', ['r', 'g', 'b'])
Hsl = namedtuple('Hsl', ['h', 's', 'l'])

class ImageData():
    def __init__(self):
        self.image_name = None
        self.rgb = None
        self.hsl = None
        self.data_image = None

    def get_image_nome (self):
        return self.image_name
    
    def set_image_name (self, name):
        self.image_name = name
        
    def get_rgb (self):
        return self.rgb

    def set_rgb (self, rgb):
        self.rbg = rgb

    def get_data_image(self):
        return self.data_image

    def set_data_image(self, data):
        self.data_image= data

    

    def convert_data(self, data):
        """Converte a estrutura de dados para o formato da tabela.

        Args:
            data: A estrutura de dados original.

        Returns:
            Uma lista de listas representando as linhas da tabela.
        """

        result = [["Amostra", "R", "G", "B", "Percentual"]]  # Cabeçalho da tabela

        for item in data:
            for amostra in item['amostras']:
                row = [
                    print(amostra['Amostra']),
                    print(amostra['cor_principal_RGB'].r),
                    amostra['cor_principal_RGB'].g,
                    amostra['cor_principal_RGB'].b,
                    amostra['Percentual']
                ]
                result.append(row)

        return result
    
        pass