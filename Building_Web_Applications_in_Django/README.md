# Building Web Applications in Django

From edx:
https://courses.edx.org/courses/course-v1:MichiganX+dj4e102x+3T2020/course/

Model: Data-Base
View (Controller): Manage conections betwen model and template.
Template (View): The information that the user can watch. 


------------------------------------------------------------------------------
## About the course

- Understanding Model View Controler

We call the data bit  - the "Model" or Data Model.
We call the "making the next HTML" bit the "View" or "Presentation Layer".
We call the handling of input and the general orchestation of it all the "Controller".

- Django Data Models

Object Relational Mapping (ORM): We use those objects to store and retrieve data from the databases (SQLite, MySQL, Postgres, Oracle).

- Migrations: From Model to Database

The make migrations command reads all the models.py files in all the applications, and creates / nevolves the migration files.

The migrate command reads all the migrations folders in the application folders and creates / envolves the tables in the database.

- First scripts on python anywhere

git clone https://github.com/csev/dj4e-samples.git
cd dj4e-samples
workon django3 ► to activate the enviroment
pip3 install --user -r requirements.txt
python3 manage.py check
python3 manage.py makemigrations
vi users/models.py
:q
rm db.sqlite3
python3 manage.py migrate
python3 manage.py shell
    from users.models import User 
    u = User(name='Kristen', email='kf@umich.edu')
    u.save()
    u.id
    u = User(name='Chuck', email='cvl@umich.edu')
    u.save()
    u = User(name='Colleen', email='csev@umich.edu')
    u.save()
    u = User(name='Ted', email='ted@umich.edu') 
    u.save()
    u = User(name='Sally', email='a2@umich.edu')
    u.save()
    u.name
    User.objects.values() 
    User.objects.filter(email='cvl@umich.edu').values()
    quit() 

Default db in Django: sqlite3

File contains the list of INSTALLED_APPS in a Django project: settings.py

Command "python manage.py migrate": Builds/updates the database structure for the project.

Purpose of the models.py file:To define the shape of the data objects to be stored in a database.

Option "sqlmigrate": It lets you see the SQL that will run to effect a migration.

__str__ method in a Django model: It lets you specify how an instance of the model will be represented as a string.

Difference between the Django shell and a normal interactive Python shell: The Django shell loads all of the project objects before starting.

Django command to create a user/password for the admin user interface: createsuperuser.

Edit the admin.py file in a Django aplication to make sure a model appears in the admin interface.

- Task 2:
https://docs.djangoproject.com/en/3.0/intro/tutorial02/

Advices, do not run this tutorial on pythonanywhere because there are issues to open the port http://127.0.0.1:8080/ or http://127.0.0.1:8000/ if you don't have a paid account. 