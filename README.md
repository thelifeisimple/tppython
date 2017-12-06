# FARMASOFT - Final Paradigmas de Programación 2°Cuatrimestre 2017 - Ana Maria Zuluaga Vasquez

 
Flujo del programa
 Es una aplicacion de consulta de ventas con diferentes reportes por pantalla. La misma fue desarrollada en Python 3.4 y utiliza Flask para renderizar los templates a los archivos Html's que componen la misma. 

Estructura de la información en los archivos

 Se configuran archivos con formato .csv, donde se encuentra la información que se vera a través de entrelazamiento web que se muestra en forma de tablas con columnas y filas. 

Uso del programa
Los modulos de la aplicación son los siguientes:
1- Login: 
  Se solicita al usuario a través de un login el código de usuario  y clave las cuales se validan contra el archivo de usuarios (.csv)
  Se valida en esta seccion:
  a) archivo de usuarios no existe. Error: "El archivo de usuarios no existe.".
  b) archivo de usuario no puede abrirse. Error: "No tienes permisos sobre el archivo de usuarios.".
  c) el usuario no existe. Error: "Usuario ingresado inexistente."
  d) la clave ingresada es incorrecta. Error: "Clave ingresada incorrecta."
  e) si el registro del archivo de usuario no es consistente (cantidad de columnas incorrecta) se omite el registro (linea) y se sigue con el siguiente.
  
1.1- Recuperar usuario:
  El usuario pordrá recuerar su clave a través de la pregunta secreta la cual esta almacenada en el archivo csv de usuarios. El formato deberá coincidir exactamente como se ingreso, con mayusculas o minusculas. 

1.2 Registrar usuario:
    En caso de que el usuario no este registrado, podra completar un formulario de inscripción al sistema. Este registro se almacena en el archivos usuario y contendrá: 
- usuario.
- la clave.
- nombre.
- apellido.
- pregunta secreta (Se eligirán entre las 3 preguntas que ofrece el sistem: "apellido de soltera de la madre", "donde nacio" o "nombre de la primera mascota").
- respuesta.

2- Bienvenida:
  En esta pantalla se mostrará el listado de ultimas ventas con el contenido de los registros (archivo_csv) 

<<-- Menu -->> 
3- Logo Farmasoft:
	. El logo de farmasoft es un link que nos llevará a la pantalla de bienvenida (3).

4- Salir:
	. El menu "Salir" deslogueará al usuario de la aplicacion llevandolo nuevamente a la pantalla de Login (1)

5-Errores:
  En esta pantalla se muestran las lineas con error detectadas en el archivo ventas, informandose el tipo de error y su linea correspondiente. Estas lineas como bien dice en la patalla no se tendrán en cuenta en los errores.

6- Ultimas Ventas:
	. En este item de menu se mostrará el reporte de ultimas ventas, el cual mostrará la informacion completa del archivo de ventas, al igual que al ingresar a la app.

7- Clientes por Producto:
	. En este item se podrá filtrar por "Nombre de producto" o por parte de él y se recuperarán todos los registros del archivo de ventas que coincidan en su nombre de producto con el filtro ingresado.

8- Productos por Cliente:
	. En este item se podrá filtrar por "Nombre de Cliente" o por parte de él y se recuperarán todos los registros del archivo de ventas que coincidan en su nombre del cliente con el filtro ingresado.

9- Mejores Productos:
	. En este item se podrá ver agrupado por Producto (Nombre) las ventas contenidas en el archivo de ventas. Los datos mostrados serán Codigo, Nombre de producto, cantidad de ventas y monto vendido. 
	  El orden de la tabla resultado será por "Monto Vendido" en forma decreciente para ver en los primeros lugares los productos mas vendidos.

10- Mejores Clientes:
	. En este item se podrá ver agrupado por Cliente las ventas contenidas en el archivo de ventas. Los datos mostrados serán Cliente, cantidad de compras y monto comprado. 
	  El orden de la tabla resultado será por "Monto Comprado" en forma decreciente para ver en los primeros lugares los clientes mas compradores.
	
11- (Menu) Mejores Productos:
	. En este item se podrá ver agrupado por Producto (Nombre) las ventas contenidas en el archivo de ventas. Los datos mostrados serán Codigo, Nombre de producto, cantidad de ventas y monto vendido. 
	  El orden de la tabla resultado será por "Monto Vendido" en forma decreciente para ver en los primeros lugares los productos mas vendidos.

12- (Menu) Mejores Clientes:
	. En este item se podrá ver agrupado por Cliente las ventas contenidas en el archivo de ventas. Los datos mostrados serán Cliente, cantidad de compras y monto comprado. 
	  El orden de la tabla resultado será por "Monto Comprado" en forma decreciente para ver en los primeros lugares los clientes mas compradores.
	  
13- Exportación de Reportes
    Cada pantalla de consulta tendrá la posibilidad de guardar su reporte en un archivo de formato .csv con las siguientes caracteristicas: 
- el nombre del archivo sera el nombre del reporte.
- En el nombre del archivo tendra la fecha y hora concatenada
- será un archivo csv.

Ejemplo: Nombre_del_reporte.YYYY(año)DD(día)MM(mes)HHMISS.csv


