#pip install qrcode 
#pip install qrcode[pil]
import qrcode

img = qrcode.make("http://www.cebem.es")
img.show()

num1=5
num2=2
resultado = num1 + num2

print("el resultado de la suma es :" , resultado)
