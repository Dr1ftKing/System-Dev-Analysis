
# 🟢Daily Use – Start & Stop the Project

Use this section every time you come back to work on the project.

### ▶️ Start Working

1. **Navigate to the Project Folder**
   ```bash
   cd path/to/System-Dev-Analysis

2. **Activate the Virtual Environment**

***Windows:***
```bash
.\venv\Scripts\Activate
```

***MacOs/Linux:***
```bash
source venv/bin/activate
```

## Shut Down (First-Time or Anytime)

### To stop the development server:

Press ```Ctrl + C``` in the terminal

To deactivate the virtual environment:
        ```deactivate```

<br/>
<br/>
<br/>

# <ins> 🟢First Time setup <ins>



## Create and Activate a Virtual Environment
  ### <ins>Create a Virtual Environment<ins>
      python -m venv venv
      

  ### <ins>On Windows (PowerShell)<ins>:
    .\venv\Scripts\Activate
  ### <ins>On macOS/Linux<ins>:
    source venv/bin/activate




## <ins>Install Requirements(From inside Venv)<ins>:
    pip install -r requirements.txt
  
  


## Run the Project

### <ins>Apply Migrations(Apply Database Migrations)<ins>:
    python manage.py migrate
### <ins>Start the Development Server<ins>:
    python manage.py runserver

## Shut Down (First-Time or Anytime)

### To stop the development server:

Press ```Ctrl + C``` in the terminal

To deactivate the virtual environment:
        ```deactivate```
