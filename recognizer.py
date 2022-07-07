from PIL import Image
import imagehash

def Recognize(im):
	hash0 = imagehash.average_hash(Image.open(im))
	hashes = [imagehash.average_hash(Image.open("images/psi.JPG")), 
				imagehash.average_hash(Image.open("images/beta.JPG")),
				imagehash.average_hash(Image.open("images/Gamma.JPG")),
				imagehash.average_hash(Image.open("images/gama.JPG")),
				imagehash.average_hash(Image.open("images/Dhelta.JPG")),
				imagehash.average_hash(Image.open("images/delta.JPG")),
				imagehash.average_hash(Image.open("images/epsilon.JPG")),
				imagehash.average_hash(Image.open("images/varepsilon.JPG")),
				imagehash.average_hash(Image.open("images/zeta.JPG")),
				imagehash.average_hash(Image.open("images/eta.JPG")),
				imagehash.average_hash(Image.open("images/theta.JPG")),
				imagehash.average_hash(Image.open("images/lambda.JPG")),
				imagehash.average_hash(Image.open("images/mu.JPG")),
				imagehash.average_hash(Image.open("images/Pih.JPG")),
				imagehash.average_hash(Image.open("images/pi.JPG")),
				imagehash.average_hash(Image.open("images/rho.JPG")),
				imagehash.average_hash(Image.open("images/Sigma.JPG")),
				imagehash.average_hash(Image.open("images/sigmah.JPG")),
				imagehash.average_hash(Image.open("images/phi.JPG")),
				imagehash.average_hash(Image.open("images/varphi.JPG")),
				imagehash.average_hash(Image.open("images/Psih.JPG")),
				imagehash.average_hash(Image.open("images/elFuerte.JPG")),
				imagehash.average_hash(Image.open("images/plus.JPG")),
				imagehash.average_hash(Image.open("images/minus.JPG")),
				imagehash.average_hash(Image.open("images/equal.JPG")),
				imagehash.average_hash(Image.open("images/equiv.JPG")),
				imagehash.average_hash(Image.open("images/approx.JPG")),
				imagehash.average_hash(Image.open("images/neq.JPG")),
				imagehash.average_hash(Image.open("images/pm.JPG")),
				imagehash.average_hash(Image.open("images/mp.JPG")),
				imagehash.average_hash(Image.open("images/lp.JPG")),
				imagehash.average_hash(Image.open("images/rp.JPG")),
				imagehash.average_hash(Image.open("images/to.JPG")),
				imagehash.average_hash(Image.open("images/d.JPG")),
				imagehash.average_hash(Image.open("images/Dh.JPG")),
				imagehash.average_hash(Image.open("images/partial.JPG")),
				imagehash.average_hash(Image.open("images/h.JPG")),
				imagehash.average_hash(Image.open("images/hbar.JPG")),
				imagehash.average_hash(Image.open("images/i.JPG")),
				imagehash.average_hash(Image.open("images/nabla.JPG")),
				imagehash.average_hash(Image.open("images/infty.JPG")),
				imagehash.average_hash(Image.open("images/sin.JPG")),
				imagehash.average_hash(Image.open("images/cos.JPG")),
				imagehash.average_hash(Image.open("images/tan.JPG")),
				imagehash.average_hash(Image.open("images/sinh.JPG")),
				imagehash.average_hash(Image.open("images/cosh.JPG")),
				imagehash.average_hash(Image.open("images/tanh.JPG")),]
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
