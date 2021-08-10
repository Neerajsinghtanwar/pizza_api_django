
# Library_Management_App_and_Api-Django

This Api  can manage the complete work of a online pizza shop.
Customers can Login or Signup.
If user is Manger he/she can create or remove Staff.
If user is Staff he/she can update or delete price of Pizza/topping/size/type.
Price can autmatically increase or decrease by its size and toppings of Pizza.
If new Customer is register Api sends a welcome email to Customer on its registered email-id. 
Customer can choose type/size/toppings of pizaa and oreder 
Authentication is done by username and password.

## Set Up

### Install Pip
	sudo apt-get install python-pip

### Clone library repository
	https://github.com/Neerajsinghtanwar/pizza_api_django.git

### Install Requirements
	pip install -r requirements.txt

### Set Up MySQL
	sudo apt-get install libmysqlclient-dev
	sudo apt-get install mysql-server
	mysql -u root -p --execute "create database pizza; grant all on pizza.* to root@localhost identified by 'Asdf@1234';"

### Set Database (Make Sure you are in directory same as manage.py)
    python manage.py makemigrations
    python manage.py migrate

### Run Server
	python3 manage.py runserver
	open localhost:8000 in your browser

### Authors
- [Neerajsinghtanwar](https://github.com/Neerajsinghtanwar/pizza_api_django.git)

  