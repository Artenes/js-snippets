# JS Snippets

Web app made with python (back-end) and vue-js (front-end) to manage a list of snippets in javascript.

![Usage](docs/usage.gif)

# Features
- Add snippets in Javascript (use ctrl+Enter to add one).
- Remove snippets.
- Edit snippets in place (it uses auto save).
- Search for snippets.
- Snippets expand in height according to number of lines (no scrollbars).

# Notes
- [Flask](http://flask.pocoo.org/) is used in the back-end to manage the requests.
- The back-end serves a html page that has all the Vue.js code to run the app (no vue-cli used).
- [Ace editor](https://ace.c9.io/) is used to display the snippets.
- The queries to the database are made using SQL LIKE statements, so queries might be slow to bigger snippets.
- Only shows highlight for Javascript (but the Ace editor supports other languages too).
- There is no users. This app is more appropriate for local and personal use.
- It only uses dark (monokai) theme.

# Set up

## Requirements

- Have python 3 installed.
- Have pip installed.

Clone the repository.

```
git clone git@github.com:Artenes/js-snippets.git
```

Enter in the cloned directory.
```
cd search
```

Create a new virtual environment (good practice in python to isolate dependencies).
```
python -m venv venv
```

Activate the virtual environment (we've just created previously, now we need to activate it).
```
source venv/bin/activate
```

Install the dependencies.
```
pip install -r requirements.txt
```

Initialize the local database (this will create the database file. It is SQLite, so no server setup required).
```
flask db migrate
```

Create the tables in the database.
```
flask db upgrade
```

Run the application.
```
flask run
```

Open the browser.
```
python -mwebbrowser http://localhost:5000
```

# License

MIT License.