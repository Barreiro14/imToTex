from PIL import Image
import os

#TODO: find a way to fix all the base images

def imFix(im):
    im = Image.open(im)
    im = im.convert('L')
    im = im.resize((255, 255))
    im.save('{}.JPG'.format(im))

hashes = ["images/psi.JPG", 
				"images/beta.JPG",
				"images/Gamma.JPG",
				"images/gama.JPG",
				"images/Dhelta.JPG",
				"images/delta.JPG",
				"images/epsilon.JPG",
				"images/varepsilon.JPG",
				"images/zeta.JPG",
				"images/eta.JPG",
				"images/theta.JPG",
				"images/lambda.JPG",
				"images/mu.JPG",
				"images/Pih.JPG",
				"images/pi.JPG",
				"images/rho.JPG",
				"images/Sigma.JPG",
				"images/sigmah.JPG",
				"images/phi.JPG",
				"images/varphi.JPG",
				"images/Psih.JPG",
				"images/elFuerte.JPG",
				"images/plus.JPG",
				"images/minus.JPG",
				"images/equal.JPG",
				"images/equiv.JPG",
				"images/approx.JPG",
				"images/neq.JPG",
				"images/pm.JPG",
				"images/mp.JPG",
				"images/lp.JPG",
				"images/rp.JPG",
				"images/to.JPG",
				"images/d.JPG",
				"images/Dh.JPG",
				"images/partial.JPG",
				"images/h.JPG",
				"images/hbar.JPG",
				"images/i.JPG",
				"images/nabla.JPG",
				"images/infty.JPG",
				"images/sin.JPG",
				"images/cos.JPG",
				"images/tan.JPG",
				"images/sinh.JPG",
				"images/cosh.JPG",
                "images/tanh.JPG"]
				
for element in hashes:
    imFix(element)


