  

Vahaan
=======================

[![Website cv.lbesson.qc.to](https://img.shields.io/website-up-down-green-red/http/cv.lbesson.qc.to.svg)](http://thedisappointmentpanda.fun/login/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 


A web-based system that help you pay for tolls before hand and automatically notifies when your PUC (pollution under control is expired). It sends sms notification for PUC renewal.


Features
---------

Application Features:

* Admin can view the Vehicle details via its Registration Number using search
* Admin can impose PUC on a Vehicle By Searching the Vehicle
* Admin can create new registration of vehicle
* Admin can consume the tolls prepaid by vehicle users.
* vehicle users can look for his PUC renewals
* vehicle users recieve an sms when PUC is going to/is expired
* vehicle user recieves sms of login credentials as and when admin creates his account.
* vehicle users can view his tolls passing and can pay from there



Prerequisites
-------------

- Python >= 3.5
- pip
- virtualenv (optional)


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

Video 
--------- 
The video is [here](./screencast.mp4)


#### Demo

Website is live [here](http://thedisappointmentpanda.fun/login/)

- Vehicle login Credentials 

 **username** - testuser1
 
 **password** - testing123
 
- Admin login Credentials

 **username** - testuser
 
 **password** - testing123
 
 **Note**: In admin system search for **reg_no: MH-07-246** for looking at the features.
 
 
#### Sms Example:


<div align="center">
<img src="http://i.imgur.com/ZONyZ3e.jpg"  height="500px">
</div>

<br />
<br />


**Apps Made:**


* login
* puc
* toll

**Database Uses:**

* sqlite3

**Configured URLs:**

* ``/home/``
* ``/login/``




**Contributer**
* [Chaitya Shah](https://github.com/Chaitya62)
* [Jigar Wala](https://github.com/JigarWala)
* [Ankit Mani](https://github.com/Ankit-22)





