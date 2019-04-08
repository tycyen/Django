from django.contrib import admin
from .models import Choice, Question, FeatureChoose, IssueInfo
from .models import Customer, Location, Machine,ToolsFile

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    '''fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': #['pub_date'], 'classes': ['collapse']}),
    ]'''
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']   #不知道為什麼加了這個就有搜尋功能
    #search_fields好像是ModelAdmin內的某個屬性,框架提供的東西的樣子

class CustomerInline(admin.StackedInline):
    model = IssueInfo.Customer
    #extra = 1

class IssueInfoAdmin(admin.ModelAdmin):
    list_display = ('Customer_Info','Location','Machine_Model_Name')
    def Customer_Info(self, obj):
        return '{} , {}'.format(obj.Customer,obj.Location)
#admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)
#admin.site.register(FeatureChoose)
admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(Machine)
admin.site.register(IssueInfo,IssueInfoAdmin)
admin.site.register(ToolsFile)
