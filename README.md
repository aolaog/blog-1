
                                               基于python django开发博客系统
源码地址：https://github.com/pengzihe/blog
django版本：1.6.5

目录结构如下：
blog:  				django项目名称
blogapp:  			django app名称
conn_mysql:  			数据库连接模块
static: 			静态资源目录，这里的样式和网页模板都是使用bootstrap3.0
静态资源如下： 
css    				放置css样式文件
fonts  				放置字体文件
Js				放置js文件
ckeditor 			放置文档编辑文件

templates: 模板目录

模板功能如下：

	index.html     		首页 	 
	archives.html           文章归档 
	category.html 		目录归档
	article_list.html       文章列表
	article_detail.html  	文章详细
	login.html		后台登陆    
	admin.html 		后台管理界面
	create_article.html  	发表文章
	admin_category.html  	管理分类目录（添加、删除操作）
	admin_article.html 	管理文章（删除操作）
	
models文件创建了两张表：

	categoryName: 		项目名称表
	
	article： 		文章表

urls文件：


urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),   		#django自带后台管理系统，可以把它禁止了
    url(r'^$',index),                            		#首页
    url(r'^article/(\d+)/',article_detail),      		#文章详细
    url(r'^create_article/$',create_article),   		#编写文章
    url(r'^submit_article/$',submit_article),			#创建文章	
    url(r'^submit_category/$',submit_category),			#创建目录
    url(r'^submit_delcategory/$',submit_delCategory),		#删除目录
    url(r'^submit_delarticle/$',submit_delArticle),		#删除文章
    url(r'^archives/(\d+)/',archives),				#目录归档
    #url(r'^category/([A-Za-z]+)/',category),
    url(r'^category/(\d+)/',category),				#文章类别详细
    url(r'^login/$',login),					#后台登陆界面
    url(r'^login_auth/$',login_auth),				#后台登陆认证
    url(r'^admin_article/$',admin_article),			#后台文章管理
    url(r'^admin_category/$',admin_category),			#后台目录管理
)

views文件，具体信息请参考github源码，功能实现和urls文件说明一样。

展示效果可以查看：http://www.pengzihe.com/?p=389

