from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
    """导入logout（）函数调用，它要求将request对象作为实参，
    然后重定向到主页
    """

#登录用户
def register(request):
    """注册新用户"""
    if request.method != 'POST':
        #显示空的注册表单
        form = UserCreationForm() #这是一个默认表单，检查响应的是否是POST请求，如果不是就创建一个实例，且不提供任何初始数据。
    else:
        #处理填写好的注册表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #让用户自动登录，在重定向到主页
            authenticate_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form':form}
    return render(request,'users/register.html',context)



































