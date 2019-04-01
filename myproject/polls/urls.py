from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'polls'  #加了這一行,原本模板的{% url 'detail'就要改{% url 'polls:detail'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('issuefeedback', TemplateView.as_view(template_name='polls/issuefeedback.htm'), name = 'issuefeedback'),
    path('issuefeedbackreply', TemplateView.as_view(template_name='polls/issuefeedbackreply.htm'), name = 'issuefeedbackreply'),
    path('<int:pk>/', views.FeatureChooseView.as_view(), name='feature'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]