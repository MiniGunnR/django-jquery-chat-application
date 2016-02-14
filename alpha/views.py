from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from chat_app import settings
#import time 
from .models import Chat
from FB import FB
from Parse import Parse
from twitterSearch import twitterSearch

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
                #WelcomeUser(user)
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

        #if(msg[0:6] == "Robot:"):
        callRobot(msg, request)
            
        
        msg = c.user.username+": "+msg

        c = Chat(user=request.user, message=msg)

        if msg != '':            
            c.save()
        #mg = src="https://scontent-ord1-1.xx.fbcdn.net/hprofile-xaf1/v/t1.0-1/p160x160/11070096_10204126647988048_6580328996672664529_n.jpg?oh=f9b916e359cd7de9871d8d8e0a269e3d&oe=576F6F12"
        return JsonResponse({ 'msg': msg, 'user': c.user.username})
    else:
        return HttpResponse('Request must be POST.')

def Messages(request):
    c = Chat.objects.all()
    return render(request, 'alpha/messages.html', {'chat': c})

def callRobot(txt,request):

    parse = Parse()
    result = []
    decision = parse.outputString(str(txt))
    if decision[0][0]==1:
        fb = FB()
        temp = fb.searchUser(str(decision[1]))
        if temp!=None and len(temp)>0:
            result.append("Result from Facebook, Total results are "+str(len(temp))+"\n")
            for i,y in temp.iteritems():
                result.append("UserID:"+i+"\tUser Full Name: "+y+"\n")
    if decision[0][1]==1:
        twitter = twitterSearch()
        temp = twitter.searchName(str(txt))
        result.append("Result from twitter Total results are :"+str(len(temp))+"\n")
        for i in temp:
            result.append("UserID:"+i[0]+"\tUser Full Name:"+i[1]+"\tUser location"+i[2]+"\n")
    if decision[0][2]==1:
        fb = FB()
        temp = fb.searchDetailInfo(str(txt))
        if "name" in temp:
            result.append("Name:    "+temp["name"])
        if "category" in temp:
            result.append("\tCategory:  "+temp["category"])
        if "birthday" in temp:
            result.append("\tBirthday:  "+temp["birthday"])
        if "about" in temp:
            result.append("\tAbout: "+temp["about"])
        if "pic" in temp:
            result.append("\tPicture:   "+temp["pic"]+"\n")
    #result = fb.searchUser(str(txt))
    message=""

    for i in result:
        message = message+i

    #for i in range(1,1000):
     #   print message.decode('unicode-escape')
    # for i in range(1,300):
    #     print message[1791:1793]
    #msg = message.decode('unicode-escape')

    
    #print result

    msg = message
    user = GetRobot(request,msg)
  
    return msg

def GetRobot(request,msg):
   # username = request.POST[Robot]
   # password = request.POST['123']
    user = authenticate(username="Robot", password=123)
    c = Chat(user=user, message=msg)
    if msg != '':            
        c.save()
    print c.message
    return user
# def WelcomeUser(user):
#     msg = "Welcome  "+user.username
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     c = Chat(user=user, message=msg)
#     c.save()
#     return JsonResponse({ 'msg': msg, 'user': "Robot"})