import os

def sumar(a,b):
	r = a+b
	print "\n Resultado: "
	print "\n %d + %d = %d" % (a,b,r)

def restar(a,b):
	r = a-b
	print "\n Resultado: "
	print "\n %d - %d = %d" % (a,b,r)

def multiplicar(a,b):
	r = a*b
	print "\n Resultado: "
	print "\n %d x %d = %d" % (a,b,r)

def dividir(a,b):
	r = a/b
	print "\n Resultado: "
	print "\n %d / %d = %d" % (a,b,r)

while True:
	os.system("clear")
	print """
	         [CALCULADORA]
	         -------------

 | 1. SUMA    |[Elija un opcion]| 3. MULTIPLICAR |
  -----------------------------------------------
 | 2. RESTAR  |    5. SALIR     | 4. DIVIDIR     |"""
	opcion = int(raw_input("\n  Opcion > "))

	if opcion == 1:
		print "\n [SUMAR]"
		print " -------"
		n1 = int (raw_input("\n Numero 1: "))
		n2 = int (raw_input(" Numero 2: "))
		sumar(n1,n2)
		raw_input("\n Presione ENTER para volver al menu. ")
		os.system("clear")

	elif opcion == 2:
		print "\n [RESTAR]"
		print " --------"
		n1 = int (raw_input("\n Numero 1: "))
		n2 = int (raw_input(" Numero 2: "))
		restar(n1,n2)
		raw_input("\n Presione ENTER para volver al menu. ")
		os.system("clear")

	elif opcion == 3:
		print "\n [MULTIPLICAR]"
		print " -------------"
		n1 = int (raw_input("\n Numero 1: "))
		n2 = int (raw_input(" Numero 2: "))
		multiplicar(n1,n2)
		raw_input("\n Presione ENTER para volver al menu. ")
		os.system("clear")

	elif opcion == 4:
		print "\n [DIVIDIR]"
		print " ---------"
		n1 = int (raw_input("\n Numero 1: "))
		n2 = int (raw_input(" Numero 2: "))
		dividir(n1,n2)
		raw_input("\n Presione ENTER para volver al menu. ")
		os.system("clear")

	elif opcion == 5:
		break

	else:
		print "[opcion invalida]"





