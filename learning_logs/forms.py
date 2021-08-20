#用于添加主题的表单

from django import forms
from django.forms import widgets

from .models import Topic,Entry

class TopicForm(forms.ModelForm): #定义了一个topicform类，继承了forms.ModelForm
    class Meta:
        model = Topic 
        fields = ['text']
        labels = {'text': ''}
    #最简单的modelform模型，只包含一个内嵌的meta类，它告诉django根据哪个模型创建表单，
    # 以及在表单中包含哪些字段
    #9根据模型topic创建一个表单，该表单只包含字段text，11处是让django不要为字段text生成标签。

#创建一个与模型Entry相关连的表单
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry 
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
#通过让Django使用forms.Textarea，我们定制了字段‘text’的输入小部件，将文本区域的宽度设置为80列。

