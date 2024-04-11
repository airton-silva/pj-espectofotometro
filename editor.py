from os import path
from PIL import Image, ImageDraw, ImageFont
import colorgram
import tempfile

class editor():
	img = None
	img_formato = None
	img_local = None
	img_nome = None
	img_ext = None
	imagem = None
	rotate_img = None

	def resetar(self):
		self.img = None
		self.img_formato = None
		self.img_local = None
		self.img_nome = None
		self.img_ext = None
		self.rotate_img = None

	def carregar_imagem(self, imagem):
		try:
			self.img = Image.open(imagem)
			self.img_formato = self.img.format
			self.img_local = path.dirname(path.realpath(imagem))
			self.img_nome, self.img_ext = path.splitext(path.basename(imagem))
			print('Imagem carregada!')
			return True
		except:
			print('Falha ao carregar imagem.')
			return False

	def girar_imagem(self, sentido='horario', angulo=90):
		# try:
			img_tempfile = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
			if sentido == 'horario':
				self.img = self.img.rotate(angulo * -1, expand=True)
			elif sentido == 'anti_horario':
				self.img = self.img.rotate(angulo, expand=True)
			
			self.img.save(img_tempfile.name, format='JPEG')
			self.rotate_img = img_tempfile.name
	 
		# finally:
		# 	img_tempfile.close()
		# 	os.unlink(img_tempfile.name)


	def remover_cor_imagem(self):
		imagem = str(self.img_local)+"/"+ str(self.img_nome)+str(self.img_ext)
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

		return True

	def salvar(self, pasta, arquivo_nome):
		try:
			self.img.save(pasta + '/' + arquivo_nome + '.' + self.img_formato, self.img_formato.upper())
			self.resetar()
			return True
		except:
			return False


ed = editor()