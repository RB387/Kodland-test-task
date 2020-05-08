# Kodland-test-task

## Install
Make sure that you alredy have installed PostgreSQL.
https://www.postgresql.org/download/

To install Blog database run:
```
chmod +x configure_db.sh
./configure_db.sh
```

Enter your admin password in blog/settings.py (or set your password 'password')

```python
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'admin',
        'PASSWORD': 'password', #Enter your password here
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Then run server with:
```
pipenv install
pipenv run python manage.py runserver
```
