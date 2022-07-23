from django.contrib import admin
from .models import City
from .models import Speciality
from .models import Vacancy

admin.site.register(City)
admin.site.register(Speciality)
admin.site.register(Vacancy)