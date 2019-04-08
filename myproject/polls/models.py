import datetime

from django.db import models
from django.utils import timezone

class FeatureChoose(models.Model):
    FeatureText = models.CharField(max_length=200)
    def __str__(self):
        return self.FeatureText

class Customer(models.Model):
    Customer_Name = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.Customer_Name
class Location(models.Model):
    LocationName = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.LocationName
class Machine(models.Model):
    MachineName = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.MachineName
class IssueInfo(models.Model):
    Customer = models.ForeignKey(Customer, default="", on_delete=models.SET_DEFAULT)
    Location = models.ForeignKey(Location, default="", on_delete=models.SET_DEFAULT)
    Machine_Model_Name = models.ForeignKey(Machine, default="", on_delete=models.SET_DEFAULT)
    Mach_Cust_ID = models.CharField(max_length=200)
    Issue_Topic = models.CharField(max_length=200,default="Unknown")
    Machine_Jam_Status = models.CharField(max_length=1000,blank=True)
    Issue_Describe = models.CharField(max_length=2000,blank=True)
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class ToolsFile(models.Model):
    filename_text = models.CharField(max_length=200)
    description_text = models.TextField(max_length=2000)
    def __str__(self):
        return self.filename_text