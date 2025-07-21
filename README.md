



## Create and Activate a Virtual Environment
  ### Create a Virtual Environment
      python -m venv venv
      

  ### On Windows (PowerShell):
    .\venv\Scripts\Activate
  ### On macOS/Linux:
    source venv/bin/activate




## Install Requirements:
    pip install -r requirements.txt
  
  


## Run the Project

### Apply Migrations:
    python manage.py migrate
### Start the Development Server
    python manage.py runserver
