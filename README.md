# Django-Poll-App-
This project features a simple polling application that requires you to register as a user to vote on a particular poll. Only the admin user can add, edit, update and delete a poll or choice. This project was created by following the Django project's tutorial. 

## Getting Started
These are the steps to follow if you'd like to set up and run the project on your local machince. 

### Pre-requisites
Python version 3 or up and Django version 5 or up
### Installation

Clone this repository on your local machine by typing the following in your terminal 

`git clone https://github.com/Carissa-moodley/Django-poll-app.git`
or download using the url below

### Migrate the database
Navigate to the project directory and open a terminal to run database migrations
`python manage.py makemigrations`
`python manage.py migrate`

### Create a superuser
You will need to create a superuser to access the admin panel
`python manage.py createsuperuser`

### Run the program on a local server
Run the following command in your terminal 
`python manage.py runserver`
Access the admin panel at http://127.0.0.1:8000/admin/ and the web application at [http://127.0.0.1:8000]http://127.0.0.1:8000/) in your browser.  

### Project snapshot
#### Login Page
<img width="728" alt="login page" src="https://github.com/Carissa-moodley/Django-Poll-App-/assets/31736109/5c5b5e31-84da-4f28-8ad0-bc882b760d7a">

#### Registration Page
<img width="791" alt="register" src="https://github.com/Carissa-moodley/Django-Poll-App-/assets/31736109/4b72bf56-4d3d-4018-9036-18c63ea55c45">

#### Polls Page
<img width="959" alt="polls" src="https://github.com/Carissa-moodley/Django-Poll-App-/assets/31736109/544d7c7e-b57c-4942-a541-7113b184ee58">

#### Polls Edit Page 
<img width="956" alt="add poll" src="https://github.com/Carissa-moodley/Django-Poll-App-/assets/31736109/fead0900-76f7-4d3a-93f8-6d627f5b770f">

#### Vote for Choices
<img width="953" alt="vote" src="https://github.com/Carissa-moodley/Django-Poll-App-/assets/31736109/eaa467dd-ba83-4b77-accc-c1d788161724">

#### Edit Choices
<img width="956" alt="add choice" src="https://github.com/Carissa-moodley/Django-Poll-App-/assets/31736109/9648fa6c-4a51-4e56-ba64-6037024da226">

###Author 
Carissa Moodley
Credits: https://docs.djangoproject.com/en/5.0/

