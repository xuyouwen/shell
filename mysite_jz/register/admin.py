from django.contrib import admin

# Register your models here.
from register.models import *

admin.site.register(User)
admin.site.register(Organization)
admin.site.register(School)
admin.site.register(Resume)
admin.site.register(SchoolPublish)
admin.site.register(OrgPublish)
