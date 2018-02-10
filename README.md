# Aves de Costa Rica

Administracion de Proyectos Tecnologico de Costa Rica

## Getting Started

Creado en Linux, se utiliza Django y PostgreSQL no es necesario saber el syntax de PostgreSQL ya que el ORM de Django se encarga de casi todo
Para el html y el frontend se utliza django templates (incluido en django) y boostrap

### Prerequisitos

Python 3
Pip 


### Instalando
Estas instrucciones son para linux-ubuntu pero la idea es la misma si se quiere ejecutar en otro OS solo hay que googlear las instrucciones

Se instala python 3 si no se ha instalado

```
$ sudo apt install python3
```

luego se instala pip

```
$ sudo apt-get install python-pip python-dev build-essential 
```

Para poder editar el codigo y correrlo se necesita primero clonar el repositorio
te vas a alguna carpeta en el cual clonarlo y ejecutas

```
$ git clone (url aqui)
```
despues se necesita crear un ambiente local de desarrollo

```
$ virtualenv env
```

Una vez creado lo activas

```
$ source env/bin/activate
```

luego para instalar los requerimientos de manera facil se ejecuta el comando

```
$ env/bin/pip install -r requirements.txt 
```

luego para ejecutar el debugging o ejectuar el proyecto solo entrar a la carpeta AvesCostaRica y correr

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Otros comandos ubicados en la documentacion de django

https://docs.djangoproject.com/en/2.0/


### Coding style

Se trata de seguir PEP8 pero todo relax

## Deploy

Se utilizara nginx y gunicorn pero para debuggear y development no se necesita nada en especial, solo se le hace el comando de runserver

## Built With

* [Bootstrap](https://getbootstrap.com/) - CSS Framework
* [Django](https://www.djangoproject.com/) - Web Framework
* [PostgreSQL](https://www.postgresql.org/) - Base de Datos


## Authors

* **Emmanuel Perez** - *Initial work* - [EmmanuelPerezP](https://github.com/EmmanuelPerezP)

** agregar los demas **

