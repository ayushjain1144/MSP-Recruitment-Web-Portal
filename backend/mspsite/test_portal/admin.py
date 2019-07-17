from django.contrib import admin


# Register your models here.
from .models import Candidate, Question, Response, Questionm, Questioni, Responsem, Responsei

admin.site.register(Questionm)
admin.site.register(Questioni)
admin.site.register(Question)
admin.site.register(Candidate)
admin.site.register(Response)
admin.site.register(Responsem)
admin.site.register(Responsei)
