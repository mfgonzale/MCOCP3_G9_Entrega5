import glob
from PIL import Image
import re

def atoi(text):
	return int(text) if text.isdigit() else text

def natural_keys(text):
	return [atoi(c) for c in re.split(r'(\d+)',text)]

caso = 1

fp_in = f'Caso_{caso}/frame_*.png'
fp_out= f'2D_ej04_frame_Caso_{caso}.gif'

lista_imagenes=sorted(glob.glob(fp_in))
print('sorted(glob.glob(fp_in)):',lista_imagenes)
lista_imagenes.sort(key=natural_keys)
print('lista_imagenes:',lista_imagenes)
img, *imgs=[Image.open(f) for f in lista_imagenes]
img.save(fp=fp_out,format='GIF', append_images=imgs,save_all=True,duration=150,loop=0)