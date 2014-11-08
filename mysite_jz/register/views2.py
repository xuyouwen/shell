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

TYPE_CHOICE=(
        ('level1','短工'),
        ('level2','校内'),
        ('level3','实习'),
        ('level4','勤工俭学'),
        ('level5','教育/服务') 
        )


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
'''
class Org_authenticateForm(forms.Form):
    org_name=forms.CharField(label='机构名称',max_length=40)
    licence_no=forms.CharField(label='执照编号',max_length=30)
    industry=forms.CharField(label='所属行业',max_length=30)
    org_property=forms.CharField(label='机构性质',max_length=30)
    org_size=forms.IntegerField(label='机构规模')
    org_addr=forms.CharField(label='机构地址',max_length=80)
    linkman=forms.CharField(label='联系人',max_length=10)
    phone=forms.CharField(label='联系电话',max_length=15)
    intro=forms.CharField(label='机构简介',widget=forms.Textarea)

class Sch_authenticateForm(forms.Form):
    sch_name=forms.CharField(label='学校名称',max_length=40)
    sch_addr=forms.CharField(label='学校地址',max_length=80)
    linkman=forms.CharField(label='联系人',max_length=10)
    phone=forms.CharField(label='联系电话',max_length=15)
    intro=forms.CharField(label='学校简介',widget=forms.Textarea)

class ResumeForm(forms.Form):
    name=forms.CharField(label='姓名',max_length=10)
    city=forms.CharField(label='城市',max_length=15)
    age=forms.IntegerField(label='年龄')
    school=forms.CharField(label='学校',max_length=30)
    qq=forms.CharField(label='QQ',max_length=20)
    phone=forms.CharField(label='手机号',max_length=15)
    email=forms.EmailField(label='邮箱')
    desire=forms.CharField(label='求职意向',max_length=30)
    work_exp=forms.CharField(label='工作经验',widget=forms.Textarea)
    apply_exp=forms.CharField(label='求职经验',widget=forms.Textarea)

class SchoolPublishForm(forms.Form):
    title=forms.CharField(label='检学标题',max_length=40)
    work_addr=forms.CharField(label='工作地点',max_length=80)
    work_time=forms.CharField(label='工作时间',max_length=80)
    linkman=forms.CharField(label='联系人',max_length=10)
    phone=forms.CharField(label='联系电话',max_length=15)
    email=forms.EmailField(label='邮箱')
    recruit_nu=forms.IntegerField(label='招聘人数')
    wages=forms.CharField(label='工资待遇',max_length=40)
    intro=forms.CharField(label='内容描述',widget=forms.Textarea)

class OrgPublishForm(forms.Form):
    title=forms.CharField(label='兼职标题',max_length=40)
    work_type=forms.ModelMultipleChoiceField(label='兼职类型',choice=TYPE_CHOICES)
    work_addr=forms.CharField(label='工作地点',max_length=80)
    work_time=forms.CharField(label='工作时间',max_length=80)
    linkman=forms.CharField(label='联系人',max_length=10)
    phone=forms.CharField(label='联系电话',max_length=15)
    email=forms.EmailField(label='邮箱')
    recruit_nu=forms.IntegerField(label='招聘人数')
    wages=forms.CharField(label='工资待遇',max_length=40)
    intro=forms.CharField(label='内容描述',widget=forms.Textarea)
'''
#注册
'''def regist(req):
    if req.method == 'POST':
        uf = RegistForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = RegistForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))
'''
#regist
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
                return render_to_response('index.html',{'user':username})
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


def personal(req):
    return HttpResponseRedirect('/personal/')

'''def index(req):
    return HttpResponseRedirect('/index')
'''
#            
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
            return render_to_response('login.html')
        else:
            error.append('Please input all the information')
    else:
        leg_f=Org_authenticateForm()
    return render_to_response('legalize.html',{
        'leg_f':leg_f,'error':error},context_instance=RequestContext(req))

def school_legalize(req):
    error=[]
    if req.method=='POST':
        sl_f=Sch_authenticateForm(req.POST)
        if sl_f.is_valid():
            sl_f.save()
            return render_to_response('login.html')
        else:
            error.append('Please input all the information')
    else:
        sl_f=Sch_authenticateForm()
    return render_to_response('school_legalize.html',{
        'sl_f':sl_f,'error':error},context_instance=RequestContext(req))



def school_publish(req):
    error=[]
    if req.method=='POST':
        sp_f=SchoolPublishForm(req.POST)
        if sp_f.is_valid():
            sp_f.save()
            return render_to_response('login.html')
        else:
            error.append('Please input all the information')
    else:
        sp_f=SchoolPublishForm()
    return render_to_response('school_publish.html',{
        'sp_f':sp_f,'error':error},context_instance=RequestContext(req))


def publish(req):
    error=[]
    if req.method=='POST':
        p_f=OrgPublishForm(req.POST)
        if p_f.is_valid():
            p_f.save()
            return render_to_response('login.html')
        else:
            error.append('Please input all the information')
    else:
        p_f=OrgPublishForm()
    return render_to_response('publish.html',{
        'p_f':p_f,'error':error},context_instance=RequestContext(req))

def resume(req):
    error=[]
    if req.method=='POST':
        r_f=ResumeForm(req.POST)
        if r_f.is_valid():
            r_f.save()
            return render_to_response('login.html')
        else:
            error.append('Please input all the information')
    else:
        r_f=ResumeForm()
    return render_to_response('resume.html',{
        'r_f':r_f,'error':error},context_instance=RequestContext(req))
