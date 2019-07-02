from django.contrib import admin


# Register your models here.
from .models import Candidate, Question

admin.site.register(Question)
admin.site.register(Candidate)


