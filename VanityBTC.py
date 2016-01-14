__author__ = 'Xcbtrader'

from bitcoin import *
from time import time

novalids = ['O', '0', 'L', 'l', ' ']

while True:
	print ()
	print ()
	print ()
	print ('#######################################################')
	print ('###########      VANITYBTC By Xcbtrader       #########')
	print ('#######################################################')
	print ('Generacion de Billeteras Bitcoin Personalizadas')
	print ('Caracteres no Validos: O 0 L l')
	print ('#######################################################')
	print ()
	error = False
	texto = input('Texto a Personalizar (RETURN/INTRO FIN) ?: ')
	if texto =='':
		print ('!!! FINALIZANDO PROGRAMA !!!')
		exit()
		
	for a in novalids:
		if a in texto:
			error = True
	if error:
		print ('!!!!! Texto incorrecto !!!!!')
	else:
		nCoincidencias = input('Numero de direcciones a encontrar: ')
		nCoincidencias = int(nCoincidencias)
		fichero = input('Nombre y extension del fichero donde guardar los resultados: ')
		for n in range (1,nCoincidencias + 1):
			encontrada = False
			start_time = time()
			print ()
			print ('#### BUSCANDO COINCIDENCIAS - NO PARE EL ORDENADOR ####')
			print ()
			while encontrada == False:
				priv = random_key()
				pub = privtopub(priv)
				addr = pubtoaddr(pub)
				if addr.find(texto) == 1:
					encontrada = True
					elapsed_time = round(time() - start_time,2)
					#Coincidencia encontrada
					#Imprimimos resultado en pantalla y guardamos en fichero
					electrumPKey = encode_privkey(priv, 'wif_compressed')
					print ('Coincidencia Numero: ' + str(n))
					print ('Tiempo Utilizado: ' + str(elapsed_time) + ' Segundos')
					print ('Direccion: ' + addr)
					print ('Clave Privada para Importar: ' + electrumPKey)
					
					fSaldo = open(fichero, "a")
					fSaldo.write(electrumPKey)
					fSaldo.write('\n')
					fSaldo.write(priv)
					fSaldo.write('\n')
					fSaldo.write(addr)
					fSaldo.write('\n')
					fSaldo.write('\n')
					fSaldo.close()
					
					print ('### DATOS GUARDADOS EN: ' + fichero)
					print ()
