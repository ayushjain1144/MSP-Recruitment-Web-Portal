from django.contrib import admin


# Register your models here.
from .models import Candidate, QuestionMCQ, ResponseMCQ, QuestionSub, ResponseSub, Exam

admin.site.register(Candidate)
admin.site.register(ResponseMCQ)
admin.site.register(Exam)

@admin.register(QuestionSub)
class QuestionSubAdmin(admin.ModelAdmin):
    list_display=['ques_no', 'question', 'marks']

@admin.register(QuestionMCQ)
class QuestionMCQAdmin(admin.ModelAdmin):
    list_display=['ques_no', 'question', 'marks']

@admin.register(ResponseSub)
class ResponseSubAdmin(admin.ModelAdmin):
    list_display=['bitsid','quesno','free_response','marks']
