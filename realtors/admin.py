from django.contrib import admin
#from organizations.models import Organization,OrganizationOwner,OrganizationUser
from .models import Realtor,Agent


#admin.site.unregister(Organization)
#admin.site.unregister(OrganizationUser)
#admin.site.unregister(OrganizationOwner)
admin.site.register(Realtor)
admin.site.register(Agent)
# Register your models here.
