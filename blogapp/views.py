from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, render_to_response
from blogapp.models import *
from django.db.models import Count
from django.contrib import auth,comments
import datetime,time,conn_mysql



# Create your views here.

def index(request):

	conn = conn_mysql.connMysql()
	runStatement = "select  blogapp_categoryname.id,category_name,count(category_name) as count from blogapp_categoryname,blogapp_article where category_id =  blogapp_categoryname.id group by category_name order by blogapp_categoryname.id;"
	category = conn.connMysql(runStatement)

	print category
	archives_list = article.objects.values('archives_date').annotate(m_amount =Count('archives_date'))  #article archives
	index_content = article.objects.order_by('-id')[0]  #latest content
	latest_article = article.objects.order_by('-id') #recent articles
	#category = article.objects.values('category').annotate(m_amount =Count('category'))	#category archives
	category_name = categoryName.objects.order_by('id')
	return render_to_response("index.html",{'archives_list':archives_list,'index_content':index_content,'latest_article':latest_article,'category':category,'category_name':category_name})




def article_detail(request,article_id):
	conn = conn_mysql.connMysql()
	runStatement = "select  blogapp_categoryname.id,category_name,count(category_name) as count from blogapp_categoryname,blogapp_article where category_id =  blogapp_categoryname.id group by category_name order by blogapp_categoryname.id;"
	category = conn.connMysql(runStatement)
	archives_list = article.objects.values('archives_date').annotate(m_amount =Count('archives_date'))
        article_obj = article.objects.get(id=article_id)
	latest_article = article.objects.order_by('-id')
	category_name = categoryName.objects.order_by('id')
        return render_to_response("article_detail.html",{'archives_list':archives_list,'article_obj':article_obj,'latest_article':latest_article,'category':category,'category_name':category_name})



def create_article(request):
	if not request.user.is_authenticated():
		print request.user
        	return HttpResponseRedirect("/")
	else: 
		category_name = categoryName.objects.order_by('id')
		return render_to_response("create_article.html",{'category_name':category_name})

def admin_article(request):
	if not request.user.is_authenticated():
		print request.user
        	return HttpResponseRedirect("/")
	else: 
		archives_list = article.objects.values('archives_date').annotate(m_amount =Count('archives_date'))  #article archives
		index_content = article.objects.order_by('-id')[0]  #latest content
		latest_article = article.objects.order_by('-id') #recent articles
		category_name = categoryName.objects.order_by('id')
		return render_to_response("admin_article.html",{'archives_list':archives_list,'index_content':index_content,'latest_article':latest_article,'category_name':category_name})

def admin_category(request):
	if not request.user.is_authenticated():
		print request.user
        	return HttpResponseRedirect("/")
	else: 
		category_name = categoryName.objects.order_by('id')
		return render_to_response("admin_category.html",{'category_name':category_name})


def submit_article(request):
        article_title =  request.POST.get('article_title')
        article_content = request.POST.get('article_content')
        article_category = categoryName.objects.get(id = request.POST.get('article_category'))
        username_id = request.POST.get('username_id')
        article.objects.create(
                title = article_title,
                content = article_content,
                category = article_category,
                author = User.objects.get(id = request.user.id),
                publish_date = datetime.datetime.now(),
                modify_date = datetime.datetime.now(),
		archives_date = time.strftime('%Y%m',time.localtime(time.time()))
        )
        return HttpResponseRedirect("/")


def submit_category(request):
	categoryName.objects.create(
		category_name = request.POST.get('categoryName')
	)
	print request.POST.get('categoryName')
        return HttpResponseRedirect("/admin_category/")



def archives(request,archives_date):  #article archives
	conn = conn_mysql.connMysql()
	runStatement = "select  blogapp_categoryname.id,category_name,count(category_name) as count from blogapp_categoryname,blogapp_article where category_id =  blogapp_categoryname.id group by category_name order by blogapp_categoryname.id;"
	category = conn.connMysql(runStatement)
	archives_list = article.objects.values('archives_date').annotate(m_amount =Count('archives_date'))
	archives = article.objects.filter(archives_date=archives_date)
	latest_article = article.objects.order_by('-id')
	category_name = categoryName.objects.order_by('id')
	return render_to_response("archives.html",{'archives_list':archives_list,'archives':archives,'latest_article':latest_article,'category':category,'category_name':category_name})

def category(request,category_Name):  #category archives
	conn = conn_mysql.connMysql()
	runStatement = "select  blogapp_categoryname.id,category_name,count(category_name) as count from blogapp_categoryname,blogapp_article where category_id =  blogapp_categoryname.id group by category_name order by blogapp_categoryname.id;"
	category = conn.connMysql(runStatement)
	category_list = article.objects.filter(category = category_Name)	
	archives_list = article.objects.values('archives_date').annotate(m_amount =Count('archives_date'))
	index_content = article.objects.order_by('-id')[0]
	latest_article = article.objects.order_by('-id')
	category_name = categoryName.objects.order_by('id')
	return render_to_response("category.html",{'archives_list':archives_list,'index_content':index_content,'latest_article':latest_article,'category':category,'category_name':category_name,'category_list':category_list})



#--------------------------------------------login auth--------------------------------------------

def login(request):   #login
	return render_to_response("login.html")

def login_auth(request):
        username,password = request.POST['username'],request.POST['password']
	user = auth.authenticate(username = username,password = password)
	archives_list = article.objects.values('archives_date').annotate(m_amount =Count('archives_date'))  #article archives
	index_content = article.objects.order_by('-id')[0]  #latest content
	latest_article = article.objects.order_by('-id') #recent articles
	category_name = categoryName.objects.order_by('id')
        if user is not None:  #authentications is correct
                auth.login(request,user)
		#return render_to_response("create_article.html")
		return render_to_response("admin.html",{'archives_list':archives_list,'index_content':index_content,'latest_article':latest_article,'category_name':category_name})
        else:
         	return render_to_response("login.html",{'login_err':"Wrong username or password!"})

