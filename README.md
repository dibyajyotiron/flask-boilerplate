## Flask Boilerpate - updated!

Boilerplate application for Flask

### Quick Start

Clone the repo, then:

```sh
$ git remote rm origin
$ git remote add origin <the location of my new git repository>
$ git push -u origin master
```

## Run
Before running the server, make sure to check `.env` file is created,
with the variables
```
FLASK_ENV=development
SECRET_KEY_{FLASK_ENV value in caps}, i.e SECRET_KEY_DEVELOPMENT=abcdef
APP_NAME_{FLASK_ENV value in caps}, i.e APP_NAME_DEVELOPMENT=xyzzz
```

```sh
$ python run.py
```