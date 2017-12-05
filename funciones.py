ARCHIVO_USUARIOS_NOMBRE = "archivos/sistema/archivo_usuarios.csv"
ARCHIVO_USUARIOS_NOMBRE_TEMP = "archivos/sistema/archivo_usuarios"
ARCHIVO_USUARIOS_COLUMNAS =6
ARCHIVO_VENTAS_NOMBRE = "archivos/sistema/archivo_ventas.csv"
ARCHIVO_VENTAS_COLUMNAS = 5
ARCHIVO_RERORTE_PATH = "archivos/reportes"

#---------------------------------------------------------
# funcion para validar cada linea del archivo de ventas
# retorna OK en caso de registro valido o la concatenacion
# de errores de cada columna invalida.
#---------------------------------------------------------
def valida_linea_archivo_ventas(columnas):
	
	msjerror=  'OK'
	
	if (len(columnas) != ARCHIVO_VENTAS_COLUMNAS):
		msjerror=  '[La linea no posee el numero correcto de columnas]'
	else:	
		if len(columnas[0])==0:
			msjerror= '[Col1: Cliente vacio]'	
		
		if len(columnas[1])==0:
			msjerror= '[Col2: codigo de producto vacio]'	
			
		if len(columnas[2])==0:
			msjerror= '[Col3: Nombre de producto vacio]'	
		
		if len(columnas[3])==0:	
			msjerror= msjerror+'[Col4: cantidad vacia]'	
		else:
			try:
				valor = float(columnas[3])
			except ValueError:
				msjerror= msjerror+'[Col4: cantidad no es numerico]'	
			
		if len(columnas[3])==0:
			msjerror= msjerror+'[Col4: cantidad vacia]'	
		else:
			try:
				valor = float(columnas[4])
			except ValueError:
				msjerror= msjerror+'[Col5: precio no es numerico]'	
			
	return msjerror
			

#---------------------------------------------------------
# funcion para validar el  archivo de ventas y generar
# el reporte de errores para mostrar al login. Retorna
# una lista de los registros con error
#---------------------------------------------------------
def validar_archivo_ventas ():
	''' devuelve la lista de ventas.
    '''
	import csv
	archivoList = list()
	try:

		with open(ARCHIVO_VENTAS_NOMBRE, 'r', newline='') as csv_file:
			reader = csv.reader(line.replace('  ', ',') for line in csv_file)
			# quita el titulo		
			next(reader, None)
			#ordenar el archivo por cliente
			lineas = list(reader)
			errores = []
			nrolinea=0
			
			for columnas in lineas:
	
				msjerror=  valida_linea_archivo_ventas(columnas)
				nrolinea+=1
	
				if msjerror != 'OK':	
					errores.append("[LINEA "+str(nrolinea)+']'+msjerror+','+columnas[0]+','+columnas[1]+','+columnas[2]+','+columnas[3]+','+columnas[4])
				
		return errores
		
	except FileNotFoundError:
		msjerror ="El archivo de ventas no existe." 
		errores.append(msjerror)
		return errores
	except PermissionError:
		msjerror = "No tienes permisos sobre el archivo de ventas."
		errores.append(msjerror)
		return errores

#---------------------------------------------------------
# funcion para validar el usuario y clave
# retorna OK en caso de acceso correcto o el error
# correspondiente.
#---------------------------------------------------------
def validar_usuario (usuario, clave):
	''' devuelve la lista de usuarios.
    '''
	import csv
	existeUsr = False 
	try:

		with open(ARCHIVO_USUARIOS_NOMBRE, 'r', newline='') as csv_file:
			reader = csv.reader(line.replace('  ', ',') for line in csv_file)
			lineas = list(reader)

			for columnas in lineas:
				
				if (len(columnas) != ARCHIVO_USUARIOS_COLUMNAS):
					loginResult ='El archivo de usuarios posee lineas con formato incorrecto.'
				else:
					if (columnas[0].upper().strip() == usuario.upper().strip() ):
						existeUsr = True
						if (columnas[1].strip() == clave.strip()):
							loginResult = 'OK'
						else:
							loginResult = 'Clave ingresada incorrecta.'
						break

		if not existeUsr:
			loginResult = 'Usuario ingresado inexistente.'
		
		return loginResult
				
	except FileNotFoundError:
		print ("El archivo de usuarios no existe.") 
	except PermissionError:
		print("No tienes permisos sobre el archivo de usuarios.")

#---------------------------------------------------------
# funcion para recuperar datos del usuario 
# retorna OK en caso de acceso correcto o el error
# correspondiente.
#---------------------------------------------------------
def recuperar_usuario (usuario):
	''' devuelve la datos de usuarios.
    '''
	import csv
	existeUsr = False 
	userList = list()
	try:

		with open(ARCHIVO_USUARIOS_NOMBRE, 'r', newline='') as csv_file:
			reader = csv.reader(line.replace('  ', ',') for line in csv_file)
			lineas = list(reader)

			for columnas in lineas:
				
				if (columnas[0].upper().strip() == usuario.upper().strip() ):
					existeUsr = True
					userList.append(columnas)
					break

		
		return userList
				
	except FileNotFoundError:
		print ("El archivo de usuarios no existe.") 
	except PermissionError:
		print("No tienes permisos sobre el archivo de usuarios.")

#---------------------------------------------------------
# funcion para recuperar datos del usuario 
# retorna OK en caso de acceso correcto o el error
# correspondiente.
#---------------------------------------------------------
def registrar_usuario (usuario, clave, nombre, apellido, pregunta, respuesta):
	''' devuelve la datos de usuarios.
    '''
	import csv
	
	try:

		linea = usuario+","+clave+","+nombre+","+apellido+","+pregunta+","+respuesta
		with open(ARCHIVO_USUARIOS_NOMBRE, 'a', newline='') as csv_file:
			
			csv_file.write(linea+"\n")
			csv_file.close()
		
		return "OK"
				
	except FileNotFoundError:
		print ("El archivo de usuarios no existe.") 
	except PermissionError:
		print("No tienes permisos sobre el archivo de usuarios.")

#---------------------------------------------------------
# funcion para recuperar datos del usuario 
# retorna OK en caso de acceso correcto o el error
# correspondiente.
#---------------------------------------------------------
def guardar_usuario (usuario, clave, nombre, apellido, pregunta, respuesta):
	''' devuelve la datos de usuarios.
    '''
	import csv
	import os
	from datetime import datetime
	x = datetime.now()
	fecha = "%s" % x.isoformat() 
	fecha = fecha.replace(":",".")
	archivotemp =  ARCHIVO_USUARIOS_NOMBRE_TEMP+"-"+fecha+".csv"
	
	try:

		linea = usuario+","+clave+","+nombre+","+apellido+","+pregunta+","+respuesta
		with open(ARCHIVO_USUARIOS_NOMBRE, 'r', newline='') as csv_input,  open(archivotemp,'w') as csv_output :
			reader = csv.reader(line.replace('  ', ',') for line in csv_input)
			lineas = list(reader)

			for columnas in lineas:
				
				if (columnas[0].upper().strip() == usuario.upper().strip() ):
					csv_output.write(linea+"\n")
				else:
					lineasinmodificar = columnas[0]+","+columnas[1]+","+columnas[2]+","+columnas[3]+","+columnas[4]+","+columnas[5]+"\n"
					csv_output.write(lineasinmodificar)


			csv_input.close()
			csv_output.close()
			print("borra "+ARCHIVO_USUARIOS_NOMBRE)
			os.remove(ARCHIVO_USUARIOS_NOMBRE)
			print("renombra "+archivotemp+ " a "+ARCHIVO_USUARIOS_NOMBRE)
			os.rename(archivotemp, ARCHIVO_USUARIOS_NOMBRE)
		
		return "OK"
				
	except FileNotFoundError:
		print ("El archivo de usuarios no existe.") 
	except PermissionError:
		print("No tienes permisos sobre el archivo de usuarios.")

#---------------------------------------------------------
# funcion para obtener el listado completo de ventas contenido
# en el archivo de ventas. Retorna la lista de ventas ordenada por 
# cliente
#---------------------------------------------------------
def obtener_ventas ():
	''' devuelve la lista de ventas.
    '''
	import csv
	archivoList = list()
	try:

		with open(ARCHIVO_VENTAS_NOMBRE, 'r', newline='') as csv_file:
			reader = csv.reader(line.replace('  ', ',') for line in csv_file)
			# quita el titulo		
			next(reader, None)
			#ordenar el archivo por cliente
			lineas = sorted(reader, key=lambda row:(row[0]))

			for columnas in lineas:
				if valida_linea_archivo_ventas(columnas) == 'OK':	
					archivoList.append(columnas)

	 
		
		return archivoList
	
	except FileNotFoundError:
		print ("El archivo de ventas no existe.") 
	except PermissionError:
		print("No tienes permisos sobre el archivo de ventas.")
		
#---------------------------------------------------------
# funcion para obtener las ventas de un cliente en particular
# Mostrará todos los registros del archivo de ventas que 
# coincidan con el parametro cliente o parte de el.  Retorna
# la lista de ventas resultando ordenada por producto
#---------------------------------------------------------	
def obtener_ventas_cliente (cliente):
	''' devuelve la lista de ventas.
    '''
	import csv
	archivoList = list()
	try:

		if (cliente==''):
			return obtener_ventas ()
		else:   
			with open(ARCHIVO_VENTAS_NOMBRE, 'r', newline='') as csv_file:
				reader = csv.reader(line.replace('  ', ',') for line in csv_file)			
				# quita el titulo		
				next(reader, None)
				#ordenar el archivo por nombre producto
				lineas = sorted(reader, key=lambda row:(row[2]))

				for columnas in lineas:
					if valida_linea_archivo_ventas(columnas) == 'OK':	
						if ( cliente.upper().strip() in columnas[0].upper().strip() ):
							archivoList.append(columnas)
					
		 
			return archivoList
		
	except FileNotFoundError:
		print ("El archivo de ventas no existe.") 
	except PermissionError:
		print("No tienes permisos sobre el archivo de ventas.")

#---------------------------------------------------------
# funcion para obtener las ventas de un producto en particular
# Mostrará todos los registros del archivo de ventas que 
# coincidan con el parametro producto o parte de el. Retorna
# la lista resultante ordenada por cliente
#---------------------------------------------------------			
def obtener_ventas_producto (producto):
	''' devuelve la lista de ventas.
    '''
	import csv
	archivoList = list()
	try:

		if (producto==''):
			return obtener_ventas ()
		else:    
			with open(ARCHIVO_VENTAS_NOMBRE, 'r', newline='') as csv_file:
				reader = csv.reader(line.replace('  ', ',') for line in csv_file)
				# quita el titulo		
				next(reader, None)
				#ordenar el archivo por cliente
				lineas = sorted(reader, key=lambda row:(row[0]))
							
				for columnas in lineas:
					
					if valida_linea_archivo_ventas(columnas) == 'OK':	
						if (producto.upper().strip() in columnas[2].upper().strip() ):
							archivoList.append(columnas)
		
		 
			
			return archivoList

	except FileNotFoundError:
		print ("El archivo de ventas no existe.") 
	except PermissionError:
		print("No tienes permisos sobre el archivo de ventas.")

#---------------------------------------------------------
# funcion para obtener la suma de las compras del archivo 
# de ventas. Retorna una lista de registros agrupados por cliente,
# cantidad y monto comprados ordenadas por monto descendente.
#---------------------------------------------------------	
def obtener_ventas_mejor_cliente ():
	''' devuelve la lista de clientes mas compradores.
    '''
	import csv
	archivoList = list()
	try:

		with open(ARCHIVO_VENTAS_NOMBRE, 'r', newline='') as csv_file:
			reader = csv.reader(line.replace('  ', ',') for line in csv_file)
 		    # quita el titulo		
			next(reader, None)
			#pasa de formato reader a lista
			lineas = sorted(reader, key=lambda row:(row[0]))
			
			clienteNombre=''
			clienteMonto=0
			clienteCantidad=0
			lineaNum=0
			# itera el archivo ordenado por cliente
			for columnas in lineas:
				
				lineaNum=lineaNum+1
				
				if valida_linea_archivo_ventas(columnas) == 'OK':	
					#matriz = funciones.armar_matriz(matriz, columnas[0].upper().strip(),  columnas[4])
					if (clienteNombre.upper().strip() == columnas[0].upper().strip()):
						clienteMonto=clienteMonto+float(columnas[4])
						clienteCantidad=clienteCantidad+1
					else:
						if (lineaNum==1):
							clienteNombre=columnas[0]
							clienteCantidad=1
							clienteMonto=float(columnas[4])
						else:
							archivoList.append(( clienteNombre, clienteCantidad, round(clienteMonto,2)))
							clienteNombre=columnas[0]
							clienteMonto=float(columnas[4])
							clienteCantidad=1


		#si el archivo posee un solo registro
		if (lineaNum==1):
			archivoList.append(( clienteNombre, clienteCantidad, round(clienteMonto,2)))

		# ordena el resultado por MONTO descendente
		archivoList.sort( key=lambda cliente:cliente[2], reverse=True)
		# ordena el resultado por CANTIDAD descendente
		#archivoList.sort( key=lambda cliente:cliente[1], reverse=True)
		
	 
		return archivoList  
		
	except FileNotFoundError:
		print ("El archivo de ventas no existe.") 
	except PermissionError:
		print("No tienes permisos sobre el archivo de ventas.")

#---------------------------------------------------------
# funcion para obtener la suma de las ventas del archivo.
# Retorna una lista de registros agrupados por producto,
# cantidad y monto vendido ordenadas por monto descendente.
#---------------------------------------------------------	
def obtener_ventas_mejor_producto ():
	''' devuelve la lista de productos mas comprados.
    '''
	import csv
	archivoList = []
	try:

		with open(ARCHIVO_VENTAS_NOMBRE, 'r', newline='') as csv_file:
			reader = csv.reader(line.replace('  ', ',') for line in csv_file)
			# quita el titulo		
			next(reader, None)
			#pasa de formato reader a lista
			lineas = sorted(reader, key=lambda row:(row[1]))

			#lineas = list(reader)
			productoCodigo=''
			productoNombre=''
			productoMonto=0
			lineaNum=0
			# itera el archivo ordenado por producto
			for columnas in lineas:
				
				lineaNum=lineaNum+1
				
				if valida_linea_archivo_ventas(columnas) == 'OK':	
					# si es el mismo producto acumula monto y cantidad
					if (columnas[2].upper().strip()==productoNombre.upper().strip()):
						productoMonto=productoMonto+float(columnas[4])
						productoCantidad=productoCantidad+float(columnas[3])
					else:
						# si es la primer fila acumula monto y cantidad
						if (lineaNum==1):
							productoCodigo=columnas[1]
							productoNombre=columnas[2]
							productoCantidad=float(columnas[3])
							productoMonto=float(columnas[4])
						else:
							# si cambia de producto, agrego a la lista de resultados el producto acumulado anterior
							archivoList.append(( productoCodigo, productoNombre, productoCantidad, round(productoMonto,2)))
							# guarda las datos del nuevo producto para seguir iterando el for
							productoCodigo=columnas[1]
							productoNombre=columnas[2]
							productoCantidad=float(columnas[3])
							productoMonto=float(columnas[4])


		#si el archivo posee un solo registro
		if (lineaNum==1):
			archivoList.append(( productoCodigo, productoNombre, productoCantidad, round(productoMonto,2)))
		
		# ordena el resultado por MONTO descendente
		archivoList.sort( key=lambda producto:producto[3], reverse=True)
		# ordena el resultado por CANTIDAD descendente
		#archivoList.sort( key=lambda producto:producto[2], reverse=True)

		
	
		
		return archivoList
		
	except FileNotFoundError:
		print ("El archivo de ventas no existe.") 
	except PermissionError:
		print("No tienes permisos sobre el archivo de ventas.")

#---------------------------------------------------------
# funcion para exportar la lista que se ve en pantalla 
# 
#---------------------------------------------------------
def exportarcsv (lista, nombre, header, columnas):
	''' 
    '''
	import csv
	try:
			
		with open(nombre, 'w', newline='') as csv_file:

			#configure writer to write standard csv file
			writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
			writer.writerow(header)
			for item in lista:
				#Write item to csv_file
				
				if (columnas==1):
					writer.writerow([item[0]])	
				elif (columnas==2):
					writer.writerow([item[0], item[1]])	
				elif (columnas==3):
					writer.writerow([item[0], item[1], item[2]])	
				elif (columnas==4):
					writer.writerow([item[0], item[1], item[2], item[3]])	
				elif (columnas==5):
					writer.writerow([item[0], item[1], item[2], item[3], item[4]])
				elif (columnas==6):
					writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5]])						
			
		csv_file.close()
		
		return "OK"
				
	except FileNotFoundError:
		print ("El reporte no pudo abrirse.") 
	except PermissionError:
		print("No tienes permisos sobre el archivo de reporte.")



