# FARMASOFT - Parcial Paradigmas de Programación 2°Cuatrimestre 2017 - Ana Maria Zuluaga Vasquez


 
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
  e) si el registro del archivo de usuario no es consistente (cantidad de columnas incorrecta) se omite el registro y se sigue con el siguiente.
  
2- Informacion de Errores:
  Una vez autentificado el usuario se informan, si existieran los errores existentes en el archivo de ventas para que el usuario tenga conocimiento de que el mismo no será utilizado en su totalidad.
  Esta pantalla se visualizará solo la primera vez luego del login para que la aplicacion continue con los registros correctos del archivo.
  
3- Bienvenida:
  En esta pantalla se mostrará el listado de ultimas ventas con el contenido de los registros (archivo_csv) 

<<Menu>> 
4- Logo Farmasoft:
	. El logo de farmasoft es un link que nos llevará a la pantalla de bienvenida (3).

5- Salir:
	. El menu "Salir" deslogueará al usuario de la aplicacion llevandolo nuevamente a la pantalla de Login (1)

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
	  
*NOTA*

 Se creo estructura de clases en models de los tipos necesarios en la app.
. Usuario
. Producto
. Cliente
. Venta

(No llegué a implementar la app para que pueda crear las instancias al leer el csv)

