.. TODO: Complete the README descriptions and "about" section.{% if False %}{# Hiding GitHub README #}

![image](https://img.shields.io/travis/edoburu/django-project-template/master.svg?branch=master)
![image](https://img.shields.io/codecov/c/github/edoburu/django-project-template/master.svg)
  

Vahaan
=======================

This project template creates a Django 2.0 project with a base set of applications

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

Apps Made:

* login
* puc
* toll

Database Uses:
* sqlite3

Configured URLs:

* ``/home/``



Templates:

* ``home.html``

Usage
-----

Create a Django project:

.. code-block:: bash

    mkdir my-website.com
    cd my-website.com
    django-admin.py startproject mywebsite . -e py,rst,example,gitignore,ini,min -n Dockerfile --template=https://github.com/edoburu/django-project-template/archive/master.zip

The layout uses an ``src`` folder.
This allows you to create folders like ``docs``, ``web``, ``logs``, ``etc`` at the toplevel.
However, feel free to undo this change.

The remaining instructions - to start the development server - can be found in the generated ``README.rst`` file.


Django-fluent template
----------------------

In a second branch, you'll find a project template for the django-fluent_ CMS:

.. code-block:: bash

    mkdir my-website.com
    cd my-website.com
    django-admin.py startproject mywebsite . -e py,rst,example,gitignore,ini,min -n Dockerfile --template=https://github.com/edoburu/django-project-template/archive/django-fluent.zip


Optional features
=================



Local testing
=============



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
* [Jigar Wala][https://github.com/JigarWala]
* [Ankit Mani](https://github.com/Ankit-22)
License
-------

# Video 
 
The video is [here](./screencast.mp4)

Describe project license here.

