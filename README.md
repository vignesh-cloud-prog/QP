# QP Web
**Website to get and give question papers easily.**

This is an website to help students get question papers from diffrent boards and universites. Question papers are accepted in pdf format from any authenticated user.

Users can easily signup by verifying their email through OTP and giving some basic informations. all contributions of user by providing question papers are recorded in their profile.

Right now paper verifications of question papers done manually. Users will get the confirmation email about accepting therir question papers.

Visit :  https://qpweb.herokuapp.com/

![QP Web Home Page](https://user-images.githubusercontent.com/64315495/159688750-76a4fd30-93a2-47e1-b740-17b333586055.png)

## Motivation
Problems that I faced during examiniation to find the old question papers. Old papers helped me to pass any subject easily. Practincing the pattern of question paper helped me to prepare well for board examinations. And I am also trying to fullfill my wish of getting feedback for practiced question papers through online.

## Problem Statement:
* Most of the students were not able to get previous question papers. Reasons may be,
  * Colleges are not open during exam holidays.
  * Lack of contact between seniors
  * They may be facing some other difficulties.
* There is no website which can provide all academic question papers in an organized manner.
* There is no easy way to make it available for everyone.
* Why are previous year question papers important ?
  * Question helps to get familiar with important questions.
  * By solving question papers one can do next level preparation.
  * Question papers help to easily pass the exam.


## Our Solution:
- Students can easily access required question papers.
- Anybody can upload any university, course , semester, subject and any year's question papers.
- All the question papers are displayed in an organized manner SEO friendly.
- Students can search for any question paper.
- Students should be able to practice question papers online.
- Students' answer papers can be reviewed online by lecturers.


## Features Included:
* ### Accessing question papers. 
[Demo-> Watch the video](https://youtu.be/iJHH30IJNFA)
	
* ### User creation and profile.
[Demo-> Watch the video](https://youtu.be/dDxIZDX9bx8)

* ### Providing question papers on QP Web
[Demo-> Watch the video](https://youtu.be/gbR07nkwYAo)

* ### Referring your friends
_Share your referral link with your friends._


## Upcoming Features:
* Live question paper practicing online.
* Evaluate your question papers and get suggessions.


## __*Setting up in your local system*__

#### Prerequisites:
* Python-3 https://www.python.org/downloads/
* Postgresql-12 https://www.postgresql.org/download/

#### Guidelines
* download the source code
```shell
git clone https://github.com/vignesh-cloud-prog/QP.git 
```

_move to the main directory_

* Creating virtual environment
  * Download python virtualenv module if you are not already installed
  ```shell
  pip install virtualenv
  ```
  * Create virtual environment
  ```shell
  virtualenv QP_env
  ```
  * Activating the virtual environment<br>
  _for Windows users_
  ```shell
  .\QP_env\Scripts\activate
  ```
  \
  _for Linux/Mac Users_
  ```shell
  source QP_Env/bin/activate
  ```
  * Install all the requirements 
  ```shell
  pip install -r requirements.txt
  ```
 
  
* Setting up database<br>
  You need to create a database named qp using pgAdmin or command and update credentials in settings.py
  * Creating super user(optional)
  ```shell
  python manage.py createsuperuser
  ```
  _go through the process_
  
  * Creating tables
  ```shell
  python manage.py makemigrations
  ```
  
  * Writing tables to the db
  ```shell
  python manage.py migrate
  ```
  
* Running the server
```shell
python manage.py runserver --settings MultipleSettings.development
```

* Visit website here http://127.0.0.1:8000/
* Documentation http://127.0.0.1:8000/admin/doc/


