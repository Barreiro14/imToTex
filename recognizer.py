from PIL import Image
import imagehash

def Recognize(im):
	hash0 = imagehash.average_hash(Image.open(im))
	hashes = [imagehash.average_hash(Image.open("images/psi.JPG")), 
				imagehash.average_hash(Image.open("images/test1.jpeg"))]
	#definir los demas hashes con las imagenes
	cutoff = 10 #se puede redefinir luego
	i = 0
	while True:
		if abs(hash0-hashes[i]) >= cutoff:
			i = i + 1
			#print(i)
		else:
			return i
			i = 0
			break
'''		
	while hash0 - hashes[i] >= cutoff:
		i = i + 1

	if i == len(hashes):
		return "no match" 
	else:
		return hashes[1]
'''