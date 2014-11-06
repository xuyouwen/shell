#coding=utf-8
from django.shortcuts import render_to_response
from django.shortcuts import render
# Create your views here.
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from register.models import User

class LoginForm(forms.Form):
#    username=forms.CharField()
#    password=forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(label='用户名:',max_length=100)
    passwold = forms.CharField(label='密  码:',widget=forms.PasswordInput())

class RegistForm(forms.Form):
    username=forms.CharField(label='用户名:')
    password1=forms.CharField(label='密  码:',widget=forms.PasswordInput)
    password2=forms.CharField(label='确  认:',widget=forms.PasswordInput)
    def pwd_validate(self,p1,p2):
        return p1==p2

'''def regist(req):
    if req.method=='POST':
        uf=RegistForm(req.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            User.object.create(username=username,password=password)
            return HttpResponseRedirect('/login/')
    else:
        uf=RegistForm()
    return render(req,'regist.html',{'uf':uf})
'''
'''def login(req):
    error=[]
    if req.method=='POST':
        uf=LoginForm(req.POST)
        if uf.is_valid():
            data=uf.cleaned_data
            username = data['username']
            password = data['password']
            if login_validate(req,username,password):
                #return render_to_response('/personal/',{'user':username})
                return HttpResponseRedirect('/personal/')
            else:
                error.append('Please input the correct password')
        else:
            error.append('Please input both username and password')
    else:
        uf= LoginForm()
    return render_to_response('login.html',{'error':error,'form':uf})
        # user=User.objects.filter(username__exact=username,password__exact=password)
           # if user:
           #     req.session['username']=username
           #     return HttpResponseRedirect('/personal/')
           # else:
           #     return HttpResponseRedirect('/login/')
   # else:
       # uf=UserForm()
#    return render_to_response('login.html',{'uf':uf})
   # return render(req,'login.html',{'uf':uf})
'''
def regist(request):
    if request.method == "POST":
        uf = RegistForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #email = uf.cleaned_data['email']
            #将表单写入数据库
            user = User()
            user.username = username
            user.password = password
            #Euser.email = email
            user.save()
            #返回注册成功页面
	    return HttpResponseRedirect('/personal/')
            #return render_to_response('success.html',{'username':username})
    else:
        uf = RegistForm()
    return render(request,'regist.html',{'uf':uf})
    #return render_to_response('regist.html',{'uf':uf})

def login_validate(request,username,password):
    rtvalue = False
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            auth_login(request,user)
            return True
    return rtvalue


def personal(req):

    return HttpResponseRedirect('/personal/')

