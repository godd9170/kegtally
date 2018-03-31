# kegtally

## Getting Started

1.  get `pipenv`

```
brew install pipenv
```

2.  make a new virtualenv

```
pipenv --three
```

3.  install all the requirements

```
pipenv install
```

4.  start up the server

```
pipenv shell
python manage.py runserver
```

## Deployment

kegtally is currently deployed on heroku. Get a heroku account, download the cli, login with `heroku login`, then from the root of this repo run `heroku create`.

To deploy, git commit all the changes you've made then run `git push heroku master`

## SSH

To `ssh` into the server simply run

```
heroku run bash
```
