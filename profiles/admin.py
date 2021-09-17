from django.contrib import admin
from .models import Profile, Host_Review, Search_History
# Register your models here.
admin.site.register(Profile) 
admin.site.register(Host_Review)
admin.site.register(Search_History)