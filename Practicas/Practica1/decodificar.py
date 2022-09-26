from models import dec_hamming

while True:
	msg = input("Ingrese rafaga de bits a decodificar:\n")
	
	print("RESULTADO:",dec_hamming(msg))
