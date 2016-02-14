from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from chat_app import settings

from .models import Chat

def test(request):
    return render(request,'alpha/test.html',{'next': next})

def index(request):
    #return render_to_response('index.html')
    return render(request, 'alpha/login.html', {'next': next})

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "alpha/login.html", {'next': next})

def Logout(request):
    #logout(request)
    Chat.objects.all().delete()
    return HttpResponseRedirect('/login/')

def Home(request):
    c = Chat.objects.all()
    return render(request, "alpha/home.html", {'home': 'active', 'chat': c})

def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':            
            c.save()

        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

def Messages(request):
    c = Chat.objects.all()
    return render(request, 'alpha/messages.html', {'chat': c})

def postToServer(txt):
    c=Chat.objects.create("11111")
    b=Chat.objects.create(txt+"    edddasdadsa")
    c.save()
    b.save()
    return