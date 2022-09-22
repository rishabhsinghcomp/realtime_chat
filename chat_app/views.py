from django.shortcuts import render,redirect
from .models import room_messages,rooms
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth 
def home(request):
    return render(request,'index.html')



def checkview(request):
    username=request.POST['username']
    roomname=request.POST['room_name']
    password=request.POST['password']
    user = auth.authenticate(username=username,password=password) ##for verification
    if user is not None:
        auth.login(request,user)
        if rooms.objects.filter(room_name=roomname).exists():#checking if room exists
            return redirect(roomname+'/?username='+username)
        else:
            room=rooms.objects.create(room_name=roomname)
            room.save()
            return redirect(roomname+'/?username='+username)
    elif User.objects.filter(username=username).exists():
        messages.info(request,"invalid creditnials")
        return redirect('home')
    else:
        return redirect('register')


def room_disp(request,room_name):
    
    ##we are recivenig the value sent via the url
    room_details=rooms.objects.get(room_name=room_name)
    dic={
        "username":request.GET.get('username'),
        "room_details":room_details,
    }
    return render(request,'room.html',dic)

##we are retriveing data form ajax script without reloading pages
def recieve_message(request):
    if  request. user. is_authenticated:
        username=request.POST['username']
        room_id=request.POST['room_id']
        message=request.POST['message']
        if message!='':
            a=room_messages.objects.create(username=username,room_id=room_id,value=message)
            a.save()
        return HttpResponse("message sent")
    else:
        return HttpResponse("Login to continue")
    

###now we are sending the datat to room page in ajax script
def get_message(request,room):
    room_details=rooms.objects.get(room_name=room)
    m=room_messages.objects.filter(room_id=room_details.id)

    return JsonResponse({"messages":list(m.values()),})



def register(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            username=request.POST['username']
            password=request.POST['password1']
            email=request.POST['email']
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already registers")#message automatically 
                return redirect('register')                      #passed in redirect 
            elif username=="":
                messages.info(request,"username cant be emty")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()##creating sving objects
                messages.info(request,"account created!!!!!!!!!!!!!")
                return redirect('home')
    else:
        return render(request,'register.html')


def logout(request):
    username=request.GET.get('username')
    #user=User.objects.filter(username=username)
    auth.logout(request)
    return redirect('home')