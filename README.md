# Coding_Interview

Agnos coding Interview 

***HOW TO DEPLOY ON LOCAL*** 

First, I need you to open this project in Visual Studio Code (download this project (code->download zip) and open "Agnos" folder in VSCode)

then, open the terminal (view->terminal) (check that you cd to the correct directory to this project)

then, ***if you haven't install Django and Djangorestframework, please use "pip install django" and "pip install djangorestframework" to install first***

finally, use the command "python manage.py runserver" to deploy on local

***HOW TO TEST API***

Once you finished the deployment. You'll have the link on your localhost ,for exammple, http://127.0.0.1:8000/ 

then, I need you to add tag to this url with api/is_match so the result is http://127.0.0.1:8000/api/is_match

then, to test , you have to send 2 parameters to this site by using query parameter ,for example, http://127.0.0.1:8000/api/is_match?message=aaa&pattern=bbb (adding '?message=aaa&pattern=bbb')

You should have seen the website like this. You may try to send 1 parameter or 0 parameter. Looks what is happenning!

***USE test_case.txt to test logic***

![demo1](https://user-images.githubusercontent.com/107032349/172550283-1625bc40-8ddb-468c-b1a9-2e933dbfb423.jpg)
