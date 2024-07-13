# Steps to setup/run the project

install python (version greater than 3.7)
clone the project in your local directory

Create a virtual env in that directory
To create a virtual environment follow the steps (these are the steps for a Windows PC)

1) Open Powershell or terminal in the directory where you have placed the project's files
2) run the following command :

       python -m venv env
   
   (make sure Python is added to the path)
4) Now to activate the environment run the following command :

        env/scripts/activate


Now install the requirements using the command

    python -m pip install -r requirements.txt

Now just run the project using the command

    python manage.py runserver



# File Structure

The files in the "Project" folder consist of 4 major files
1) settings.py (All your project configurations are done in the setting.py file)
2) asgi.py (Setup the files for the project)
4) wsgi.py (Setup the files for the project)
6) urls.py (Defines the URL of the project (the endpoints))

Inside the "patients" folder we have 4 major files and 2 major folder
Files 
1) Views.py (defines the functions that will be called when a URL endpoint Is hit)
2) urls.py (defines the URL for the patient app)
3) models.py (all the database models are structured in the models.py file)
4) context_processor.py (defines the global variables which can be accessed at any point in the template)

Folders
1) templates (contains all the HTML files)
2) static (contains all the static files such as images, CSS, JS, etc)



