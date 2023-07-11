from django.contrib import admin
from .models import CandyProfile, Skill, Education, WorkExperience, Topic

# Register your models here.


admin.site.register(Skill)


class EducationInline(admin.TabularInline):
	model = Education
	fields = ['title', 'institute_name', 'enroll_year', 'passing_year']
	extra = 1


class WorkExperienceInline(admin.StackedInline):
	model = WorkExperience
	fields = ['job_title', 'company_name', 'from_date', 'to_date', 'is_currently_working', 'roles', 'technologies']
	extra = 1



class CandyProfileAdmin(admin.ModelAdmin):
	inlines = [
        EducationInline,
        WorkExperienceInline
    ]

admin.site.register(CandyProfile, CandyProfileAdmin)

admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Topic)
