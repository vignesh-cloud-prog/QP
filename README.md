# QP

This is an website to help students get question papers from diffrent boards and universites. Question papers are accepted in pdf format from any authenticated user. Like every other websites this website also includes about and contact pages.

Users can easily signup by verifying their email through OTP and giving some basic informations. all contributions from you by providing question papers are recorded in your profile.

Right now verifications of question papers done manually. Users will get the confirmation email about accepting therir question papers. To avoid multiple instance of same question papers some checks are to be made.

This website is hosted at https://questionpaper.herokuapp.com/

__*Setting up in your local system*__

Prerequsits :
* Python-3 https://www.python.org/downloads/
* Postgresql-12 https://www.postgresql.org/download/

Installation Guidelines
* download the source code
` git clone https://github.com/vignesh-cloud-prog/QP.git `

_move to the main directory_

* Creating virtual environment
  * Download python virtualenv module if you are not already installed
  ```pip install virtualenv```
  * Create virtual environment
  ```virtualenv QP_Env```
  * Activating the virtual environment<br>
  _for Windows users_
  `.\QP_Env\Scripts\activate`\
  _for Linux/Mac Users_
  `source QP_Env/bin/activate`
  * Install ll the requirements 
  ```pip install -r requirements.txt```
 
  
* Setting up database
  * Creating super user(optional)
  ```python manage.py createsuperuser```
  _go through the process_
  
  * Creating tables
  ```python manage.py makemigrations```
  
  * Writing tables to the db
  ```python manage.py migrate```
  
* Running the server
```python manage.py runserver```

