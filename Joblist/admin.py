from django.contrib import admin
from .models import Company,Candidates

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name','jobtitle')

class CandidatesAdmin(admin.ModelAdmin):
	list_display = ('name','qualification')

# Register your models here.

admin.site.register(Company,CompanyAdmin)
admin.site.register(Candidates,CandidatesAdmin)