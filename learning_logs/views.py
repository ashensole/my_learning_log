

from django.shortcuts import render

from .models import Entry, Topic

from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
#限制对topic页面的访问

from .forms import EntryForm, TopicForm

# Create your views here.
"""编写视图"""


def index(request):
    """学习笔记主页"""
    return render(request,'learning_logs/index.html')

'''
1.render()函数，根据视图提供的数据渲染响应
2.URL请求与我们刚才定义的模式匹配时，Django将在文件views.py中查找函数index（），
再将请求对象传递给这个视图函数
3.这里向render（）提供了两个实参：原始请求对象、一个可用于创建网页的模板
'''  




#限制对topics页面的访问
@login_required
#该函数检查用户是否登录，仅当用户已登录时，Django才运行topics（）的代码，
#如果用户未登录。就重定向到登录页面

#视图函数topics
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)



#视图函数topic  
'''函数topic需要从数据库中获取指定的主题以及与之相关的所有条目'''  
def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id = topic_id)

    #确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html',context)

#视图函数new_topic

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据：创建一个新表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            #将新主题关联到新用户
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            
            return HttpResponseRedirect(reverse('learning_logs:topics'))
            
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

#视图函数new_entry()
def new_entry(request, topic_id):
    """在特定主题中添加新条目"""
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm()  #为提交数据，创建一个空列表
    else:
        form = EntryForm(data= request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))

    context = {'topic': topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

#视图函数edit_entry()
def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id = entry_id )
    topic = entry.topic

    #禁止用户通过输入类似于前面的URL来访问其他用户的条目
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context ={'entry':entry, 'topic':topic, 'form':form}
    return render(request,'learning_logs/edit_entry.html',context)





    




























