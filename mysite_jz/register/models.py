#coding=utf-8
from django.db import models

# Create your models here.

TOPIC_CHOICES = (
                ('leve1', '短工'),
                ('leve2', '校内'),
                ('leve3', '实习'),
                ('leve3', '勤工俭学'),
                ('leve3', '教育/服务'),
                ) 
class User(models.Model):
    username=models.CharField(max_length=11)
    password=models.CharField(max_length=20)

    def __unicode__(self):
        return self.username

class Organization(models.Model):
#    org_id=models.AutoField(primary_key=True)
    org_name=models.CharField(verbose_name=u'机构名称',max_length=40)
    licence_no=models.CharField(verbose_name=u'执照编号',max_length=30)
    industry=models.CharField(verbose_name=u'所属行业',max_length=30)
    org_property=models.CharField(verbose_name=u'机构性质',max_length=30)
    org_size=models.IntegerField(verbose_name=u'机构规模',default=0)
    org_addr=models.CharField(verbose_name=u'机构地址',max_length=80)
    linkman=models.CharField(verbose_name=u'联系人',max_length=10)
    phone=models.CharField(verbose_name=u'联系电话',max_length=15)
    intro=models.TextField(verbose_name=u'机构简介',max_length=200)

    def __unicode__(self):
        return self.org_name

class School(models.Model):
#    sch_id=models.AutoField(primary_key=True)
    sch_name=models.CharField(verbose_name=u'学校名称',max_length=40)
    sch_addr=models.CharField(verbose_name=u'学校地址',max_length=80)
    linkman=models.CharField(verbose_name=u'联系人',max_length=10)
    phone=models.CharField(verbose_name=u'联系电话',max_length=15)
    intro=models.TextField(verbose_name=u'学校简介',max_length=200)

    def __unicode__(self):
        return self.sch_name

class Resume(models.Model):
    name=models.CharField(verbose_name=u'姓名',max_length=10)
    city=models.CharField(verbose_name=u'城市',max_length=15)
    age=models.IntegerField(verbose_name=u'年龄')
    school=models.CharField(verbose_name=u'学校',max_length=30)
    qq=models.CharField(verbose_name=u'QQ',max_length=20)
    phone=models.CharField(verbose_name=u'手机号',max_length=15)
    email=models.EmailField(verbose_name=u'邮箱')
    desire=models.CharField(verbose_name=u'求职意向',max_length=30)
    work_exp=models.TextField(verbose_name=u'工作经验',max_length=100)
    apply_exp=models.TextField(verbose_name=u'求职经验',max_length=100)
    def __unicode__(self):
        return self.name

class SchoolPublish(models.Model):
#    sch=models.Foreignkey(verbose_name=u'发布学校',School)
    title=models.CharField(verbose_name=u'检学标题',max_length=40)
    work_addr=models.CharField(verbose_name=u'工作地点',max_length=80)
    work_time=models.CharField(verbose_name=u'工作时间',max_length=80)
    linkman=models.CharField(verbose_name=u'联系人',max_length=10)
    phone=models.CharField(verbose_name=u'联系电话',max_length=15)
    email=models.EmailField(verbose_name=u'邮箱')
    recruit_nu=models.IntegerField(verbose_name=u'招聘人数')
    wages=models.CharField(verbose_name=u'工资待遇',max_length=40)
    intro=models.TextField(verbose_name=u'内容描述',max_length=200)
    datetime=models.DateTimeField(verbose_name=u'发布时间',auto_now_add=True)
    sch=models.ForeignKey(School,verbose_name=u'学校名称')
#    sch_id=models.AutoField(primary_key=True)
    def __unicode__(self):
        return self.title

class OrgPublish(models.Model):
#    org=models.Foreignkey(verbose_name=u'发布机构',Organization)
    title=models.CharField(verbose_name=u'兼职标题',max_length=40)
    work_type=models.CharField(verbose_name=u'兼职类型',choices=TOPIC_CHOICES,max_length=20,blank=False)
    work_addr=models.CharField(verbose_name=u'工作地点',max_length=80)
    work_time=models.CharField(verbose_name=u'工作时间',max_length=80)
    linkman=models.CharField(verbose_name=u'联系人',max_length=10)
    phone=models.CharField(verbose_name=u'联系电话',max_length=15)
    email=models.EmailField(verbose_name=u'邮箱')
    recruit_nu=models.IntegerField(verbose_name=u'招聘人数')
    wages=models.CharField(verbose_name=u'工资待遇',max_length=40)
    intro=models.TextField(verbose_name=u'内容描述',max_length=200)
    datetime=models.DateTimeField(verbose_name=u'发布时间',auto_now_add=True)
    org=models.ForeignKey(Organization,verbose_name=u'发布机构')
    def __unicode__(self):
        return self.org
