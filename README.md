**Exámen para Wirall**

Para iniciar el proyecto únicamente es necesario instalar los paquetes que se encuentran en requirements.txt y utilizar 
la versión 3.7 de python.
El proyecto viene con el superuser: user = admin, pass = administrador1234
Una vez teniendo el proyecto en marcha se puede ingresar a las siguientes URL para login, crear tarjetas y personas.

1. Login : 127.0.0.1:8000/accounts/login
2. Crear personas: 127.0.0.1:8000/personas/abm_personas
3. Crear Tarjetas: 127.0.0.1:8000/tarjetas/abm_tarjetas

**Requisitos del exámen**

1. Tarjetas:
Dentro de la app tarjetas se encuentra el modelo Tarjetas. En el se encuentra la lógica para obtener
datos asociados a las mismas.
Cumple con el requerimiento **a** y con el **c**

Modulo utils dentro de app tarjetas: En el módulo utils se encuentran los métodos y funciones que cumplen con el requerimiento
**b**, **d** y **e** de la parte 1.
También la función que obtiene todas las tarjetas de crédito únicas en el sistema.

2. Personas:
Dentro de la app personas encontramos el modelo que tiene un metodo asociado el cual cumple con el requerimiento
de obtener todas las tarjetas relacionadas a una persona.


 