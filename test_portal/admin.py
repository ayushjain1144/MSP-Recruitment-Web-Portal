from django.contrib import admin


# Register your models here.
from .models import Candidate, QuestionMCQ, ResponseMCQ, QuestionSub, ResponseSub, Exam

admin.site.register(QuestionMCQ)
admin.site.register(QuestionSub)
admin.site.register(Candidate)
admin.site.register(ResponseMCQ)
admin.site.register(Exam)



@admin.register(ResponseSub)
class ResponseSubAdmin(admin.ModelAdmin):
    list_display=['bitsid','quesno','free_response','marks']
