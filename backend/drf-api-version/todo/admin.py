from django.contrib import admin

from .models import Todo

modelsTuple = (
        Todo,
    )

for model in modelsTuple:
    admin.site.register(model)