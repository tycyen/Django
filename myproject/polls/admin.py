from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    '''fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]'''
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']   #不知道為什麼加了這個就有搜尋功能
    #search_fields好像是ModelAdmin內的某個屬性,框架提供的東西的樣子

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
