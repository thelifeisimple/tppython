import csv
import sys
import os
import funciones
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
#from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def home():
		if not session.get('logged_in'):
			return render_template('login.html')
		else:			
			return redirect('/ventasultimas')

			
@app.route('/login',  methods=['GET', 'POST'])   
def do_login():
	if session.get('logged_in'):
		return home()

	loginResult = funciones.validar_usuario(request.form['username'], request.form['password'])	
	if (loginResult == 'OK'):
		session['logged_in'] = True
		session['username'] = request.form['username']

	else:
		return render_template('login.html',  msjerror=loginResult)

	return home()

@app.route('/errores',  methods=['GET', 'POST'])   
def errores():	
# valida solo la primera vez que ingresa
	if not session.get('logged_in'):
		return home()
		
	errores_archivo = funciones.validar_archivo_ventas()
	return render_template('errores.html', listadoerror=errores_archivo) 
				
@app.route('/olvidarclave',  methods=['GET', 'POST'])   
def olvidarclave():
	if session.get('logged_in'):
		return home()

	return render_template('olvidarclave.html')


@app.route('/recuperarclave',  methods=['GET', 'POST'])   
def recuperarclave():
	if session.get('logged_in'):
		return home()

	session['username'] = request.form['username']

	userResult = funciones.recuperar_usuario(request.form['username'])	
	return render_template('recuperarclave.html',  user=userResult)

	return home()

@app.route('/usuario',  methods=['GET', 'POST'])   
def usuario():

	userResult = funciones.recuperar_usuario(session['username'])	
	return render_template('usuario.html', origen="forget", user=userResult)

	return home()

@app.route('/datausuario',  methods=['GET', 'POST'])   
def datausuario():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		userResult = funciones.recuperar_usuario(session['username'])
		print (userResult)
		return render_template('datausuario.html',  user=userResult)

@app.route('/editarusuario',  methods=['GET', 'POST'])   
def editarusuario():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		userResult = funciones.recuperar_usuario(session['username'])
		print (userResult)
		return render_template('datausuario.html',  user=userResult, editar=True)

		
@app.route("/logout")
def logout():
		session['logged_in'] = False
		session['username'] = False
		session['archivoerror'] = False
		session['reportlist'] = False
		return home()

		
@app.route('/registarusuario',  methods=['GET', 'POST'])   
def registarusuario():

	if session.get('logged_in'):
		return home()

	return render_template('registrarusuario.html',  msjerror="")
		

@app.route('/guardarusuario',  methods=['GET', 'POST'])   
def guardarusuario():

	# usuario registrado edita sus datos
	if session.get('logged_in'):
			print("registrarusuario")
			print(request.form)
			resultado= funciones.guardar_usuario(request.form['username'], request.form['clave'], request.form['nombre'], request.form['apellido'], request.form['pregunta'], request.form['respuesta'])
			if resultado=="OK":
				usuarioRegistrado=funciones.recuperar_usuario(request.form['username'])	
				return render_template('datausuario.html',  origen="registro", user=usuarioRegistrado, msjerror="OK! Usuario Actualizado")
	else:
	# nuevo usuario no registrado aun
		userResult = funciones.recuperar_usuario(request.form['username'])	
		if userResult==[]:
			resultado= funciones.registrar_usuario(request.form['username'], request.form['clave'], request.form['nombre'], request.form['apellido'], request.form['pregunta'], request.form['respuesta'])
			if resultado=="OK":
				usuarioRegistrado=funciones.recuperar_usuario(request.form['username'])	
				return render_template('usuario.html',  origen="registro", user=usuarioRegistrado)
		else:
			return render_template('registrarusuario.html',  msjerror="Usuario Existente, ingrese otro nombre de usuario")
	
		
	return home()
		
@app.route('/ventasultimas',  methods=['GET', 'POST'])      
def ventasultimas():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		listado_ventas = funciones.obtener_ventas()
		# deja la lista en sesion para exportar a csv
		
		
		return render_template('ventasultimas.html',  listado=listado_ventas, username=session.get('username'))
	
@app.route('/ventascliente',  methods=['GET', 'POST'])      
def ventascliente():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		listado_ventas = funciones.obtener_ventas()
		# deja la lista en sesion para exportar a csv
		
		return render_template('ventascliente.html',  listado=listado_ventas, username=session.get('username'))
	
@app.route('/buscarventascliente',  methods=['GET', 'POST'])
def buscarventascliente(): 

	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		# si ingresa valores busca por producto ingresado
		session['cliente'] = request.form['cliente']
		listado_ventas = funciones.obtener_ventas_cliente(request.form['cliente'])
		# deja la lista en sesion para exportar a csv
		
		return render_template('ventascliente.html',  listado=listado_ventas, username=session.get('username'))
		
		
@app.route('/ventasproducto',  methods=['GET', 'POST'])
def ventasproducto(): 

	if not session.get('logged_in'):
		return render_template('login.html')
	else:

		listado_ventas = funciones.obtener_ventas()
		# deja la lista en sesion para exportar a csv
		
		
		return render_template('ventasproducto.html',  listado=listado_ventas, username=session.get('username'))

@app.route('/buscarventasproducto',  methods=['GET', 'POST'])
def buscarventasproducto(): 

	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		# si ingresa valores busca por producto ingresado
		session['producto'] = request.form['producto']
		listado_ventas = funciones.obtener_ventas_producto(request.form['producto'])
		# deja la lista en sesion para exportar a csv
		
		
		return render_template('ventasproducto.html',  listado=listado_ventas, username=session.get('username'))
		
		
@app.route('/ventasmejorproducto',  methods=['GET', 'POST'])      
def mejoresproductos(): 

	if not session.get('logged_in'):
		return render_template('login.html')
	else:

		listado_ventas = funciones.obtener_ventas_mejor_producto()
		# deja la lista en sesion para exportar a csv
		
		
		return render_template('ventamejoresproductos.html',  listado=listado_ventas, username=session.get('username'))
		
@app.route('/ventasmejoresclientes',  methods=['GET', 'POST'])      
def mejoresclientes(): 

	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		listado_ventas = funciones.obtener_ventas_mejor_cliente()
		# deja la lista en sesion para exportar a csv
		
		
		return render_template('ventasmejoresclientes.html', listado=listado_ventas, username=session.get('username'))



@app.route('/exportarventasultimas',  methods=['GET', 'POST'])      
def exportarventasultimas(): 
	x = datetime.now()
	# obtiene la fecha del sistema
	# en formato yyyyMMdd hh24:mi:ss
	fecha = "%s" % x.isoformat() 
	# reemplazo los : por .
	fecha = fecha.replace(":",".")
	# arma nombre de reporte en path /archivos/reportes/nombrereporte.20171122.23.21.43.csv
	archivo =  funciones.ARCHIVO_RERORTE_PATH+"/"+request.form["reportname"]+"-"+fecha+".csv"
	
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		# recupera reporte para exportar
		reportlist = funciones.obtener_ventas ()
		header = ['cliente', 'codigo', 'producto',  'cantidad', 'precio']
		resultado = funciones.exportarcsv(reportlist, archivo, header, 5 )
		
		return render_template('ventasultimas.html',  listado=reportlist, username=session.get('username'), archivo=archivo)
		
			
@app.route('/exportarventasproducto',  methods=['GET', 'POST'])      
def exportarventasproducto(): 

	x = datetime.now()
	fecha = "%s" % x.isoformat() 
	fecha = fecha.replace(":",".")
	archivo =  funciones.ARCHIVO_RERORTE_PATH+"/"+request.form["reportname"]+"-"+fecha+".csv"
	
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		if session.get('producto'):
			reportlist = funciones.obtener_ventas_producto(session.get('producto'))
		else:
			reportlist = funciones.obtener_ventas()

		header = ['cliente', 'codigo', 'producto',  'cantidad', 'precio']
		resultado = funciones.exportarcsv(reportlist, archivo, header, 5 )
		
		return render_template('ventasproducto.html',  listado=reportlist, username=session.get('username'), archivo=archivo)

			
@app.route('/exportarventascliente',  methods=['GET', 'POST'])      
def exportarventascliente(): 

	x = datetime.now()
	fecha = "%s" % x.isoformat() 
	fecha = fecha.replace(":",".")
	archivo =  funciones.ARCHIVO_RERORTE_PATH+"/"+request.form["reportname"]+"-"+fecha+".csv"
	
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		if session.get('cliente'):
			reportlist = funciones.obtener_ventas_cliente(session.get('cliente'))
		else:
			reportlist = funciones.obtener_ventas()

		header = ['cliente', 'codigo', 'producto',  'cantidad', 'precio']
		resultado = funciones.exportarcsv(reportlist, archivo, header, 5 )
		
		return render_template('ventascliente.html',  listado=reportlist, username=session.get('username'), archivo=archivo)
		

@app.route('/exportarmejoresproductos',  methods=['GET', 'POST'])      
def exportarmejoresproductos(): 

	x = datetime.now()
	fecha = "%s" % x.isoformat() 
	fecha = fecha.replace(":",".")
	archivo =  funciones.ARCHIVO_RERORTE_PATH+"/"+request.form["reportname"]+"-"+fecha+".csv"
	
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		reportlist = funciones.obtener_ventas_mejor_producto()
		
		header = ['codigo', 'producto',  'cantidad', 'monto']
		resultado = funciones.exportarcsv(reportlist, archivo, header, 4 )
		
		return render_template('ventamejoresproductos.html',  listado=reportlist, username=session.get('username'), archivo=archivo)

@app.route('/exportarmejoresclientes',  methods=['GET', 'POST'])      
def exportarmejoresclientes(): 

	x = datetime.now()
	fecha = "%s" % x.isoformat() 
	fecha = fecha.replace(":",".")
	archivo =  funciones.ARCHIVO_RERORTE_PATH+"/"+request.form["reportname"]+"-"+fecha+".csv"
	
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		reportlist = funciones.obtener_ventas_mejor_cliente()
		
		header = ['cliente', 'cantidad compras',   'monto']
		resultado = funciones.exportarcsv(reportlist, archivo, header, 3 )
		
		return render_template('ventasmejoresclientes.html',  listado=reportlist, username=session.get('username'), archivo=archivo)

@app.route('/exportarerrores',  methods=['GET', 'POST'])      
def exportarerrores(): 

	x = datetime.now()
	fecha = "%s" % x.isoformat() 
	fecha = fecha.replace(":",".")
	archivo =  funciones.ARCHIVO_RERORTE_PATH+"/"+request.form["reportname"]+"-"+fecha+".csv"
	
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		reportlist = funciones.validar_archivo_ventas()
		
		header = ['Linea Descripcion del error', 'cliente', 'codigo', 'producto',  'cantidad', 'precio']
		resultado = funciones.exportarcsv(reportlist, archivo, header, 6 )
		
		return render_template('errores.html',  listadoerror=reportlist, username=session.get('username'), archivo=archivo)
					
@app.errorhandler(404)
def notfounderror(e):
    return render_template('error404.html', username=session.get('username')), 404

@app.errorhandler(500)
def internalerror(e):
    return render_template('error500.html', username=session.get('username')), 500

@app.errorhandler(FileNotFoundError)
def filenotfound(e):
    return render_template('fileNotFound.html', username=session.get('username'))

		
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)