from django.contrib import admin


# Register your models here.
from .models import Candidate, Question, Response, Questionm, Questioni

admin.site.register(Questionm)
admin.site.register(Questioni)
admin.site.register(Question)
admin.site.register(Candidate)
admin.site.register(Response)

