from django.contrib import admin

# Register your models here.
from .models import Alert

# Register your models here.
# aqui dizemos que o model Question tem uma interface Admin
admin.site.register(Alert)
