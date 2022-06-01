# Django Redis Cache Example
Report Missing Person is an simple application to show how to do Django Redis Cacheing.


## Available Features
- Add Missing Person from admin Panel.
- View List of Missing Person for DB or CACHE.
- View Details of Missing Person for DB or CACHE.
- Delete Cache when new person is added/updated to reflect the changes immediately.


## Technology
- Python v3
- Django 3.2
- Django Redis 5.2


# Installation
```bash
# Clone The Repository
$ git clone https://github.com/pyshawon/django_redis_cache_example.git
$ cd django_redis_cache_example

# Create Virtual Environment and Activate
$ virtualenv -p python3 env
$ source env/bin/activate

# Install Dependency
$ pip install -r requirements.txt

# Migrate Database, Create Superuser and Run the server
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

# Cache Configuration

```python
# project/settings.py

# Redis cache backend
# https://github.com/jazzband/django-redis

CACHE_TTL = 60 * 20 
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}
```


# Contribute
If you face any problem feel free to open issue.

# Contact
If you have any suggestion:

Email: pyshawon@gmail.com

Linkedin: https://www.linkedin.com/in/pyshawon/

Facebook: https://www.facebook.com/pyshawon/



