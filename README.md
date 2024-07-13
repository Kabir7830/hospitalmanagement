# Steps to steup/run the project

install python (version greater than 3.7)
clone the project in your loal directory

Create a virtual env in that directory
To create a virtual environment follow the steps (these are the steps for a windows PC)

1) Open Powershell or terminal in the directory have placed for project's file
2) run the following command :

       python -m venv env
   
   (make sure pytohn is added to path)
4) Now to activate the environment run the following command :

        env/scripts/activate


Now install the requirements for that follow the command

    python -m pip install -r requirements.txt

Now just run the project, for that follow the command

    python manage.py runserver
