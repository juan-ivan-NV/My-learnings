# Building Web Applications in Django

From edx:
https://courses.edx.org/courses/course-v1:MichiganX+dj4e102x+3T2020/course/

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
