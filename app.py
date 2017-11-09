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
			# valida solo la primera vez que ingresa
			if not session.get('archivoerror'):
				session['archivoerror'] = True
				errores_archivo = funciones.validar_archivo_ventas()
				return render_template('errores.html', listadoerror=errores_archivo) #"Hello Boss!  <a href='/logout'>Logout</a>"
			return redirect('/ventas')

			
@app.route('/login',  methods=['GET', 'POST'])   
def do_login():
	if session.get('logged_in'):
		return home()

	loginResult = funciones.validar_usuario(request.form['username'], request.form['password'])	
	if (loginResult == 'OK'):
		session['logged_in'] = True
	else:
		return render_template('login.html',  msjerror=loginResult)

	return home()


@app.route("/logout")
def logout():
		session['logged_in'] = False
		session['archivoerror'] = False
		return home()

@app.route('/ventas',  methods=['GET', 'POST'])      
def ventasultimas():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		listado_ventas = funciones.obtener_ventas()
		return render_template('ventasultimas.html',  listado=listado_ventas, username=session.get('username'))
	
@app.route('/ventascliente',  methods=['GET', 'POST'])      
def ventascliente():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		listado_ventas = funciones.obtener_ventas()
		return render_template('ventascliente.html',  listado=listado_ventas, username=session.get('username'))
	
@app.route('/buscarventascliente',  methods=['GET', 'POST'])
def buscarventascliente(): 

	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		# si ingresa valores busca por producto ingresado
		print('listado con fitro')
		listado_ventas = funciones.obtener_ventas_cliente(request.form['cliente'])
		return render_template('ventascliente.html',  listado=listado_ventas, username=session.get('username'))
		
		
@app.route('/ventasproducto',  methods=['GET', 'POST'])
def ventasproducto(): 

	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		listado_ventas = funciones.obtener_ventas()
		return render_template('ventasproducto.html',  listado=listado_ventas, username=session.get('username'))

@app.route('/buscarventasproducto',  methods=['GET', 'POST'])
def buscarVentasproducto(): 

	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		# si ingresa valores busca por producto ingresado
		print('listado con fitro')
		listado_ventas = funciones.obtener_ventas_producto(request.form['producto'])
		return render_template('ventasproducto.html',  listado=listado_ventas, username=session.get('username'))
		
		
@app.route('/ventasmejorproducto',  methods=['GET', 'POST'])      
def mejoresproductos(): 

	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		listado_ventas = funciones.obtener_ventas_mejor_producto()
		return render_template('ventamejoresproductos.html',  listado=listado_ventas, username=session.get('username'))
		
@app.route('/ventasmejoresclientes',  methods=['GET', 'POST'])      
def mejoresclientes(): 

	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		listado_ventas = funciones.obtener_ventas_mejor_cliente()
		return render_template('ventasmejoresclientes.html', listado=listado_ventas, username=session.get('username'))
		
@app.errorhandler(404)
def notFoundError(e):
    return render_template('error404.html', username=session.get('username')), 404

@app.errorhandler(500)
def internalError(e):
    return render_template('error500.html', username=session.get('username')), 500

@app.errorhandler(FileNotFoundError)
def fileNotFound(e):
    return render_template('fileNotFound.html', username=session.get('username'))

		
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
