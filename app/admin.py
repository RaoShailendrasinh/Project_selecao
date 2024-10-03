from django.contrib import admin
from django.contrib import admin
from app.models import *


class Contactforadmin(admin.ModelAdmin):
    list_display = ["name","email","message","subject"]
admin.site.register(Contact,Contactforadmin)    


class Testimonialforadmin(admin.ModelAdmin):
  list_display = ["name","destination","img","content"]
admin.site.register(Testimonial,Testimonialforadmin)

class Serviceforadmin(admin.ModelAdmin):
  list_display = ["name","img","content"]
admin.site.register(Service,Serviceforadmin)  