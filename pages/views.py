from django.shortcuts import render
from django.http import HttpResponseRedirect
import slack

slack_token = ""


def index(request):
    return render(request, 'index.html')


def send_notification(request):
    client = slack.WebClient(token=slack_token)
    
    print('------------- Kasper notified --------------')
    response = client.chat_postMessage(
        channel='#gladibad_kasper',
        text="Baddet er ledigt nu!")
    
    return HttpResponseRedirect('/')