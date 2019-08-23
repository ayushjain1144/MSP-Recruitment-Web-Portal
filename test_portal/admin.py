from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from .models import Candidate, QuestionMCQ, ResponseMCQ, QuestionSub, ResponseSub, Exam,ImageMCQ, ImageSub

admin.site.register(Candidate)
admin.site.register(ResponseMCQ)
admin.site.register(Exam)
admin.site.register(ImageMCQ)
admin.site.register(ImageSub)



@admin.register(QuestionSub)
class QuestionSubAdmin(admin.ModelAdmin):

    list_display=['ques_no', 'question', 'marks', 'get_image']


@admin.register(QuestionMCQ)
class QuestionMCQAdmin(admin.ModelAdmin):
    list_display=['ques_no', 'question', 'marks','get_image']



@admin.register(ResponseSub)
class ResponseSubAdmin(admin.ModelAdmin):
    list_display=['bitsid','quesno','free_response','marks']
