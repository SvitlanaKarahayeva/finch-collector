from django.contrib import admin
from .models import Finch, Feeding, Park, Photo

# Register your models here.
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Park)
admin.site.register(Photo)