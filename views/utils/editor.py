from os import path
from PIL import Image, ImageDraw, ImageFont
import colorgram
import tempfile
from datetime import date

from views.utils.export_data import ExportData

class Editor():
	data_csv = {
		'name_file': 'Coleta_'+ str(date.today()),
		'amostras':[]
	}

	def __init__(self):
		img = None
		img_formato = None
		img_local = None
		img_nome = None
		img_ext = None
		imagem = None
		rotate_img = None
		image_tmp =None
		self.export_data_csv = ExportData()

	def resetar(self):
		self.img = None
		self.img_formato = None
		self.img_local = None
		self.img_nome = None
		self.img_ext = None
		self.rotate_img = None
		self.image_tmp = None

	def carregar_imagem(self, imagem):
		try:
			self.img = Image.open(imagem)
			self.img_formato = self.img.format
			self.img_local = path.dirname(path.realpath(imagem))
			self.img_nome, self.img_ext = path.splitext(path.basename(imagem))
			self.image_tmp = str(self.img_local)+"/"+ str(self.img_nome)+str(self.img_ext)
			print('Imagem carregada!')
			return True
		except:
			print('Falha ao carregar imagem.')
			return False

	def girar_imagem(self, sentido='horario', angulo=90):
		# try:
			imagem = Image.open(self.image_tmp)
			img_tempfile = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
			if sentido == 'horario':
				imagem = imagem.rotate(angulo * -1, expand=True)
			elif sentido == 'anti_horario':
				imagem = imagem.rotate(angulo, expand=True)
			
			imagem.save(img_tempfile.name, format='JPEG')
			self.image_tmp = img_tempfile.name
	 
		# finally:
		# 	img_tempfile.close()
		# 	os.unlink(img_tempfile.name)


	def remover_cor_imagem(self):
		try:
			imagem = self.image_tmp
			img = Image.open(imagem)
			width = img.width
			height = img.height

			colors = colorgram.extract(imagem, 6)
			swatchsize = int(round(width / 6, 0))

			num_colors = len(colors)

			image_palette = Image.new('RGB', (swatchsize * num_colors, int(swatchsize * 1.5)))
			print(image_palette)
			draw = ImageDraw.Draw(image_palette)
			
			# fonte para sistemas linux
			font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
			font = ImageFont.truetype(font_path, 14)

			# usar para fonte arial instalada
			# font = ImageFont.truetype('arial', 14)
	
			posx = 0
			count_color = 0
			for color in colors:
				txt = str(color.rgb.r) + "," + str(color.rgb.g) + "," + str(color.rgb.b)
				txta = str('red') + "," + str('gren') + "," + str('blue')
				txt2 = str(color.hsl.h) + "," + str(color.hsl.s) + "," + str(color.hsl.l)
				txta2 = str('tom') + "," + str(' sat') + "," + str(' lum')
				txt3 = str(round(color.proportion * 100, 2)) + "%"
				txta3 = str('proporção')
				print(f"color {count_color}: ({color.rgb.r},{color.rgb.g},{color.rgb.b})")
				# print(posx + 10, 0, posx + swatchsize)
				draw.rectangle([posx, 0, posx + swatchsize, int(swatchsize * 1.5)],
							fill=(color.rgb.r, color.rgb.g, color.rgb.b))
				draw.text((posx + 10, 0, posx + swatchsize), txta, font=font)
				draw.text((posx + 10, 15, posx + swatchsize), txt, font=font)
				draw.text((posx + 10, 35, posx + swatchsize), txta2, font=font)
				draw.text((posx + 10, 50, posx + swatchsize), txt2, font=font)
				draw.text((posx + 10, 70, posx + swatchsize), txta3, font=font)
				draw.text((posx + 10, 85, posx + swatchsize), txt3, font=font)

				posx = posx + swatchsize
				count_color = count_color + 1

			altura = image_palette.height
			new_im = Image.new('RGB', (width, height + altura), (250, 250, 250))
			new_im.paste(img, (0, 0))
			new_im.paste(image_palette, (0, height))
			new_im.save(f'imgs/{self.img_nome}.png', "PNG")
			self.img = new_im
			self.image_tmp = f'imgs/{self.img_nome}.png'
			#new_im.show()


			first_color = colors[0]
			rgb = first_color.rgb
			hsl = first_color.hsl
			proportion = first_color.proportion
			sorted(colors, key=lambda c: c.hsl.h)
			print('cor principal')
			print(rgb)
			print(hsl)
			print(f'{round(proportion * 100, 2)}%')

			second_color = colors[1]
			rgb = second_color.rgb
			hsl = second_color.hsl
			proportion = second_color.proportion
			sorted(colors, key=lambda c: c.hsl.h)
			print('cor secundaria')
			print(rgb)
			print(hsl)
			print(f'{round(proportion * 100, 2)}%')

			self.export_data_csv.add_amostra(self.data_csv, self.img_nome, rgb, hsl, f'{round(first_color.proportion * 100, 2)}%')
			return True
		except Exception as e:
			print(f"Error: {e}")
			return False  # Indicate failure:

	def salvar(self, pasta, arquivo_nome):
		try:
			self.img.save(pasta + '/' + arquivo_nome + '.' + self.img_formato, self.img_formato.upper())
			self.resetar()
			return True
		except:
			return False
		
	def rec_draw(self, coord):
		saida_path = f'imgs/{self.img_nome}.png'
		imagem_path = self.img_local +"/"+ str(self.img_nome)+str(self.img_ext)
		# Abra a imagem
		imagem = Image.open(imagem_path)

		# Crie um objeto ImageDraw
		draw = ImageDraw.Draw(imagem)

		# Defina as dimensões do retângulo
		largura_retangulo = 150
		altura_retangulo = 600
		
		x = int(coord.get('x'))
		y = int(coord.get('y'))

		# Calcule as coordenadas do canto inferior direito do retângulo
		x2 = x + largura_retangulo
		y2 = y + altura_retangulo

		# Desenhe o retângulo na imagem
		draw.rectangle((x, y, x2, y2), outline="red", width=2)

		imagem.save(saida_path)
		self.image_tmp = saida_path

		self.recortar_retangulo(x2, y2, coord )

	
	def recortar_retangulo(self, x2, y2, coord):
		saida_path = f'imgs/{self.img_nome}.png'
		imagem = Image.open(self.image_tmp)
		print(coord.get('x'), coord.get('y'))
		# Recorte a imagem
		recorte = imagem.crop((int(coord.get('x')), int( coord.get('y')), x2, y2))
		
		# # Salve a imagem recortada
		recorte.save(saida_path)

	# def print_data_csv(self):
	# 	ExportData.export_to_csv(self.data_csv, "coleta.csv")
	# 	ExportData.print_data(self.data_csv)
		pass