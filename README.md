  

Vahaan
=======================

![image](https://img.shields.io/travis/edoburu/django-project-template/master.svg?branch=master) ![image](https://img.shields.io/codecov/c/github/edoburu/django-project-template/master.svg)


A webased system that help you pay for tolls before hand and automatically notifies when your PUC (pollution under control is expired). It sends sms notification for PUC renewal.

Features
---------

Application Features:

* Admin can view the Vehicle details its Registration Number etc
* Admin can impose PUC on a Vehicle By Searching the Vehicle
* Admin can create new registration of vehicle
* Admin and vehicle users can login/register 
* vehicle users can look for his PUC renewals
* vehicle users recieve an sms when PUC is going to/is expired
* vehicle users can view his tolls passing and can pay from there

Installation
--------

First install requirements using 
```
pip install -r requirements
```

Then apply all the migrations using 

```
python3 manage.py makemigrations
python3 manage.py migrate
```

Create a super user to enter superadmin at `/admin/`

```

python3 manage.py createsuperuser

```
Runserver at `port: 8000` using

```

python3 manage.py runserver

```



Demo
--------
Website is live [here](http://thedisappointmentpanda.fun/login/)

- Vehicle login Credentials 

 **username** - testuser1
 
 **password** - testing123
 
- Admin login Credentials

 **username** - testuser
 
 **password** - testing123
 
 **Note**: In admin system search for **reg_no: MH-07-246** for looking at the features.

Apps Made:

* login
* puc
* toll

Database Uses:
* sqlite3

Configured URLs:

* ``/home/``
* ``/login/``

Templates:

* ``home.html``
* ``index.html``

About
-----

Vahaan PUC and Tolls automation

Prerequisites
-------------

- Python >= 3.5
- pip
- virtualenv (virtualenvwrapper is recommended)


Contributer
--------
* [Chaitya Shah](https://github.com/Chaitya62)
* [Jigar Wala](https://github.com/JigarWala)
* [Ankit Mani](https://github.com/Ankit-22)


# Video 
 
The video is [here](./screencast.mp4)


