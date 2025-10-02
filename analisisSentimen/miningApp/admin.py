from django.contrib import admin
from .models import Preprocessing, Teks, Stopword, Slangword
# Register your models here.
admin.site.register(Preprocessing)
admin.site.register(Teks)
admin.site.register(Stopword)
admin.site.register(Slangword)