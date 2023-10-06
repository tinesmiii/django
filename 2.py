DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': BASE_DIR / 'db.sqlite3',
        "OPTIONS": {
            "service": "my_service",
            "passfile": ".my_pgpass",
        },
    }
}
