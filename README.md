## About Project

This project illustrates RESTFUL API with error handlers that gracefully handle errorS with meaningful messages to aidE the user understand what went wrong.

#### Pre-requisites

- Developers using this project should have Python3 and pip installed on their local machines.

- **Start your virtual environment**
  From the main folder run

```bash
# Mac users
python3 -m venv venv
source venv/bin/activate
# Windows users
> py -3 -m venv venv
> venv\Scripts\activate
```

- **Install dependencies**<br>
  From the main folder run

```bash
# All required packages are included in the requirements file.
pip3 install -r requirements.txt
```

You can start the Flask server by running the command below from the `/main/` directory.

# Mac users

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

# Windows users

```
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

You can also run `python3 Flask_RESTFUL_AP1_py` from the command after placing the ensuing code at the tailend of your code.

```
if __name__=="__main__":
    app.run(debug-True)
```

The commands above put the application in development mode and restarts the server whenever changes are made.

The application will run on `http://127.0.0.1:5000/` by default and this current version of the application does not require authentication or API keys.
