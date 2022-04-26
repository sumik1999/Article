#### This is a simple projects with post and users app

#### documention is visible at /swagger/ route

##### Steps to follow

##### `pip install requirements.txt`

##### `python manage.py runserver ` to get the server running

##### Run `python manage.py makemigrations && python manage.py migrate` to get database

#### A user can be created at user/create with **username** and **password** and then can be credentials can be sent to user/token/ to generate token

#### This token needs to be used with `Authorization` header and ` Token .....` in headers of HTTP request for all private api routes.
