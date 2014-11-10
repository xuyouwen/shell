#coding=utf-8
from django.shortcuts import render,render_to_response
#from django import newforms as forms
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from register.models import *
from django.template import RequestContext
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
#from django.newforms import form_for_model
from django.forms import ModelForm
import os,sys

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名:',max_length=100)
    password = forms.CharField(label='密  码:',widget=forms.PasswordInput())

class RegistForm(forms.Form):
    username=forms.CharField(label='用户名:')
    password=forms.CharField(label='密  码:',widget=forms.PasswordInput())
    password2=forms.CharField(label='确  认:',widget=forms.PasswordInput())
    def pwd_validate(self,p1,p2):
        return p1==p2

class ChangepwdForm(forms.Form):
    #username=forms.CharField(label='用户名:')
    old_pwd=forms.CharField(label='原密码:',widget=forms.PasswordInput())
    new_pwd=forms.CharField(label='新密码:',widget=forms.PasswordInput())
    new_pwd2=forms.CharField(label='确认新密码:',widget=forms.PasswordInput())

class Org_authenticateForm(ModelForm):
    class Meta:
        model=Organization

class Sch_authenticateForm(ModelForm):
    class Meta:
        model=School

class ResumeForm(ModelForm):
    class Meta:
        model=Resume

class SchoolPublishForm(ModelForm):
    class Meta:
        model=SchoolPublish

class OrgPublishForm(ModelForm):
    class Meta:
        model=OrgPublish

#注册
def regist(req):
    error=[]
    if req.method=='POST':
        rf=RegistForm(req.POST)
        if rf.is_valid():
            data=rf.cleaned_data
            username=data['username']
            password=data['password']
            password2=data['password2']
            if not User.objects.all().filter(username=username):
                if rf.pwd_validate(password,password2):
                   # user=User.objects.create_user(username,password)
                   # user.save()
                    User.objects.create(username= username,password=password)
                    login_validate(req,username,password)
                    return render_to_response('index.html',{'user':username})
                else:
                    error.append('Please input the same password')
            else:
                error.append('The username has existed,please change your username')
    else:
        rf=RegistForm()
    return render_to_response('regist.html',{'rf':rf,'error':error },context_instance=RequestContext(req))

def login_validate(request,username,password):
    rtvalue = False
    user = authenticate(username=username,password=password)
    if user is not None: 
        if user.is_active:  
            auth_login(request,user) 
            return True
    return rtvalue  

#登陆
def login(req):
    error = []
    if req.method == 'POST':
        uf = LoginForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username= uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                #response = HttpResponseRedirect('/index/')
                return render_to_response('/index',{'user':username})
                #将username写入浏览器cookie,失效时间为3600
                #response.set_cookie('username',username,3600)
                #return response#
            else:
                #比较失败，还在login
                error.append('Please input the correct password')
                #return HttpResponseRedirect('/login/')
        else:
            error.append('Please input both username and password') 
    else:
        uf = LoginForm()
        #error.append('Please input both username and password') 
    #return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))
    return render_to_response('login.html',{'error':error,'uf':uf},context_instance=RequestContext(req))

#登陆成功
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})
    #return HttpResponseRedirect('/index/')

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

#更改密码            
def changepassword(request,username):  
    error = []  
    if request.method == 'POST':  
        form = ChangepwdForm(request.POST)  
        if form.is_valid():  
            data = form.cleaned_data  
            user = authenticate(username=username,password=data['old_pwd'])  
            if user is not None:  
                if  data['new_pwd']==data['new_pwd2']:  
                    newuser = User.objects.get(username__exact=username)  
                    newuser.set_password(data['new_pwd'])  
                    newuser.save()  
                    return HttpResponseRedirect('/login/')  
                else:  
                    error.append('Please input the same password')  
            else:  
                error.append('Please correct the old password')  
        else:  
            error.append('Please input the required domain')  
    else:  
        form = ChangepwdForm()  
    return render_to_response('changepassword.html',{'form':form,'error':error},context_instance=RequestContext(request))

#机构认证

def legalize(req):
    error=[]
    if req.method=='POST':
        leg_f=Org_authenticateForm(req.POST)
        if leg_f.is_valid():                             
            leg_f.save()
#            return render_to_response('login.html')
            return HttpResponseRedirect('/index/')  
        else:
            error.append('Please input all the information')
    else:
        leg_f=Org_authenticateForm()
    return render_to_response('legalize.html',{
        'leg_f':leg_f,'error':error},context_instance=RequestContext(req))

#学校认证
def school_legalize(req):
    error=[]
    if req.method=='POST':
        sl_f=Sch_authenticateForm(req.POST)
        if sl_f.is_valid():
            sl_f.save()
#            return render_to_response('login.html')
            return HttpResponseRedirect('/index/')  
        else:
            error.append('Please input all the information')
    else:
        sl_f=Sch_authenticateForm()
    return render_to_response('school_legalize.html',{
        'sl_f':sl_f,'error':error},context_instance=RequestContext(req))


#校园发布兼职信息
def school_publish(req):
    error=[]
    if req.method=='POST':
        sp_f=SchoolPublishForm(req.POST)
        if sp_f.is_valid():
            sp_f.save()
#            return render_to_response('Campus_community.html')
            return HttpResponseRedirect('/Campus_community/')  
        else:
            error.append('Please input all the information')
    else:
        sp_f=SchoolPublishForm()
    return render_to_response('school_publish.html',{
        'sp_f':sp_f,'error':error},context_instance=RequestContext(req))

#企业发布兼职信息
def publish(req):
    error=[]
    if req.method=='POST':
        p_f=OrgPublishForm(req.POST)
        if p_f.is_valid():
            p_f.save()
#            return render_to_response('business_center.html')
            return HttpResponseRedirect('/business_center/')  
        else:
            error.append('Please input all the information')
    else:
        p_f=OrgPublishForm()
    return render_to_response('publish.html',{
        'p_f':p_f,'error':error},context_instance=RequestContext(req))

#个人简历信息
def resume(req):
    error=[]
    if req.method=='POST':
        r_f=ResumeForm(req.POST)

        if r_f.is_valid():
            name= r_f.cleaned_data['name']
            r_f.save()
            #return render_to_response('/personal',{'name':name})
            return HttpResponseRedirect('/personal/')  
        else:
            error.append('Please input all the information')
    else:
        r_f=ResumeForm()
    return render_to_response('resume.html',{
        'r_f':r_f,'error':error},context_instance=RequestContext(req))

#企业中心
def business_center(req):
    names = OrgPublish.objects.all()
    return render_to_response("business_center.html",locals())

#校园中心
def Campus_community(req):
    names = SchoolPublish.objects.all()
    return render_to_response("Campus_community.html",locals())

#个人中心
def personal(req):
    names = Resume.objects.all()
    return render_to_response("personal.html",locals())
