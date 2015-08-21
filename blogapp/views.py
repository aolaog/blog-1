from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, render_to_response
from blogapp.models import *
from django.db.models import Count
from django.contrib import auth,comments
import datetime,time



# Create your views here.
global category_name
category_name = ['linux',
		'database',
		'virtualization',
		'cluster',
		'monitor',
		'automation',
		'python',
		'security']


def index(request):
	archives_list = article.objects.values('archives_date').annotate(m_amount =Count('archives_date'))  #article archives
	index_content = article.objects.order_by('-id')[0]  #latest content
	latest_article = article.objects.order_by('-id') #recent articles
	category = article.objects.values('category').annotate(m_amount =Count('category'))	#category archives
	return render_to_response("index.html",{'archives_list':archives_list,'index_content':index_content,'latest_article':latest_article,'category':category,'category_name':category_name})




def article_detail(request,article_id):
	archives_list = article.objects.values('archives_date').annotate(m_amount =Count('archives_date'))
        article_obj = article.objects.get(id=article_id)
	latest_article = article.objects.order_by('-id')
	category = article.objects.values('category').annotate(m_amount =Count('category'))	
        return render_to_response("article_detail.html",{'archives_list':archives_list,'article_obj':article_obj,'latest_article':latest_article,'category':category,'category_name':category_name})



#def create_article(request):
#	return render_to_response("create_article.html")


def submit_article(request):
        article_title =  request.POST.get('article_title')
        article_content = request.POST.get('article_content')
        article_category = request.POST.get('article_category')
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
        return HttpResponse('yes')

def archives(request,archives_date):  #article archives
	archives_list = article.objects.values('archives_date').annotate(m_amount =Count('archives_date'))
	archives = article.objects.filter(archives_date=archives_date)
	latest_article = article.objects.order_by('-id')
	category = article.objects.values('category').annotate(m_amount =Count('category'))	
	return render_to_response("archives.html",{'archives_list':archives_list,'archives':archives,'latest_article':latest_article,'category':category,'category_name':category_name})

def category(request,categoryName):  #category archives
	category_list = article.objects.filter(category = categoryName)	
	archives_list = article.objects.values('archives_date').annotate(m_amount =Count('archives_date'))
	index_content = article.objects.order_by('-id')[0]
	latest_article = article.objects.order_by('-id')
	category = article.objects.values('category').annotate(m_amount =Count('category'))	
	return render_to_response("category.html",{'archives_list':archives_list,'index_content':index_content,'latest_article':latest_article,'category':category,'category_name':category_name,'category_list':category_list})



#--------------------------------------------login auth--------------------------------------------

def login(request):   #login
	return render_to_response("login.html")

def login_auth(request):
        username,password = request.POST['username'],request.POST['password']
	user = auth.authenticate(username = username,password = password)
        if user is not None:  #authentications is correct
                auth.login(request,user)
         	return render_to_response("create_article.html")
        else:
         	return render_to_response("login.html",{'login_err':"Wrong username or password!"})

	"""
	try:
        	login = userinfo.objects.get(username=username)
		if(login.username == username and login.password == password):
         		return render_to_response("create_article.html",{'username_id':login.id})
		else:
         		return render_to_response("login.html",{'login_err':"Wrong username or password!"})
	except:
         	return render_to_response("login.html",{'login_err':"Wrong username or password!"})
	"""
