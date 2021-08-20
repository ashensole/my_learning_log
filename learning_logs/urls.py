'''需要在leaning_logs文件夹中创建urls.py文件'''
"""定义learning_logs的URL模式"""

from django.conf.urls import url  #导入函数url，可将URL映射到视图

from . import views #导入views模块，句点让python从当前的urls.py模块所在文件夹导入视图

urlpatterns = [
    #主页
    url(r'^$', views.index, name = 'index'),
    
    #显示所有的主题
    url(r'^topics/$', views.topics, name= 'topics'),
    
    #显示特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name= 'new_topic'),
    #这个URL模式将请求交给视图函数new_topic（）

    #用于添加新条目
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #创建一个页面，用于用户编辑既有的条目
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]


'''
实际的URL模式是一个对函数url（）的调用，这个函数接受三个实参。
第一个是正则表达式，第二个是实参（指定了要调用的视图函数），第三个实参将这个URL模式的名称指定为index（则可在其他地方引用）
正则表达式：
r 让python将接下来的字符串视为原始字符串
引号 告诉正则表达式始于何处终于何处
脱字符^ 让python查看字符串的开头，$查看字符串的末尾
总而言之这里的正则表达式让 python查找开头和末尾没有任何东西的匹配

'''












