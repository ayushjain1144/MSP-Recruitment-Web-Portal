from django.contrib import admin


# Register your models here.
from .models import Candidate, QuestionMCQ, ResponseMCQ, QuestionSub, ResponseSub

admin.site.register(QuestionMCQ)
admin.site.register(QuestionSub)
admin.site.register(Candidate)
admin.site.register(ResponseSub)
admin.site.register(ResponseMCQ)