from django.contrib import admin


# Register your models here.
from .models import Candidate, Question, Response

admin.site.register(Question)
admin.site.register(Candidate)
admin.site.register(Response)

