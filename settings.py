"""
I’m using the default Django settings, but I added my chatapp so
that Django will discover my custom management command.
"""

# … other default settings above …

INSTALLED_APPS = [
    # I left the default Django apps here…
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # I added my app so I can run `manage.py chat`
    'chatapp',
]

# … rest of settings unchanged …
