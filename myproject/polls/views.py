from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from .models import Choice,Question,FeatureChoose,ToolsFile
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail

def GoToIssueFeedbackPage(request):
    if not request.POST:
        return HttpResponse("傳送表單異常")
    CustomerName = request.POST['CustomerName']
    Location = request.POST['Location']
    MachineType = request.POST['MachineType']
    MacCustID = request.POST['MacCustID']
    IssueTopic = request.POST['IssueTopic']
    MacStatus = request.POST['MacStatus']
    MacDescription = request.POST['MacDescription']
    MailMsg = '''
    IssueTopic: {}
    Machine Status: {}
    Issue Description: {}'''.format(IssueTopic,MacStatus,MacDescription)
    send_mail('{},{},{},{} Got New Issue'.format(CustomerName,Location,MachineType,MacCustID), 
              MailMsg, 
              'yenchang70280@gmail.com', 
              ['yenchang70280@gmail.com'], fail_silently=False)
    return render(request, 'polls/issuefeedbackreply.htm',locals())
def SendIssueMail(request):
    MailMsg = '''
    IssueTopic: {}
    Machine Status: {}
    Issue Description: {}'''.format('aa','bb','cc')
    send_mail('{},{},{},{} Got New Issue'.format('11','22','33','44'), 
              MailMsg, 
              'yenchang70280@gmail.com', 
              ['yenchang70280@gmail.com'], fail_silently=False)
    return HttpResponse('sent!')
def detail(request, question_id):
    '''try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})'''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'FeatureItemList'

    def get_queryset(self):
        return FeatureChoose.objects.all()
class IssueFeedbackRequest(HttpRequest):
    template_name = 'polls/issuefeedbackreply.htm'
    def get_queryset(self):
        return HttpResponse('{},{}'.format(ctx['CustomerName'],ctx['Location']))
    '''Replier = HttpResponse()
    msg = '已收到來自{}, {}, {}相關的issue訊息'
    return HttpResponse(msg)
    def get_queryset(self):   
        ctx ={}
        ctx['CustomerName'] = request.POST['CustomerName']
        ctx['Location'] = request.POST['Location']
        return HttpResponse('{},{}'.format(ctx['CustomerName'],ctx['Location']))
        return render(request, "polls/issuefeedbackreply.htm", ctx)'''
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self): #加這個是避免猜到正確的網址,然後還是可以顯示網頁
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class ToolsFileView(generic.ListView):
    model = ToolsFile
    template_name = 'polls/toolsdownload.htm'
    context_object_name = 'ToolsList'
    def get_queryset(self):
        return ToolsFile.objects.all()