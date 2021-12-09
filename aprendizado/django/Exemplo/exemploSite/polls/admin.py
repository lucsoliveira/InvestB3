from django.contrib import admin
from .models import Question

# Register your models here.
# aqui dizemos que o model Question tem uma interface Admin
admin.site.register(Question)
