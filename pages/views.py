from django.shortcuts import render
from django.http import HttpResponseRedirect
import slack

slack_token = "xoxp-621793017634-632710302996-646595057600-866d33ceb6c9c599545edb3052df360c"


def index(request):
    return render(request, 'index.html')


def send_notification(request):
    client = slack.WebClient(token=slack_token)
    
    print('------------- Kasper notified --------------')
    response = client.chat_postMessage(
        channel='#gladibad_kasper',
        text="Baddet er ledigt nu!")
    
    return HttpResponseRedirect('/')