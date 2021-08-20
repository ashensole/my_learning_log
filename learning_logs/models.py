


from django.db import models

#将数据关联到提交它的用户
from django.contrib.auth.models import User


# Create your models here.

#1.定义模型
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200) #属性text是一个CharField，由字符和文本组成的数据。
                                            #可存储少量文本，且要告诉django该在数据库中预留多少空间，200即200个字符
    date_added = models.DateTimeField(auto_now_add = True) #DateTimeField记录日期和时间的数据。
                                                          #传递了实参auto_now_add=true
                                                           #每当用户创建新主题时，djanggo都会将这个属性自动设置成当前日期和时间
    
    #添加字段owner，建立到模型User的外键关系
    owner = models.ForeignKey(User)
    
    def __str__(self):
        """返回存储在属性text中的字符串"""
        return self.text




#2.定义模型Entry
class Entry(models.Model): #像topic一样，entry也继承了django的基类models
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE) #foreignkey（外键）是数据库术语，引用了数据库的另一条记录
                                                                #将每个条目关联到特定的主题，每个主题创建时都会分配一个键（ID）                                                               

    text = models.TextField() #textfield字段不限制条目长度
    date_added = models.DateTimeField(auto_now_add= True) #设置的属性data_added能够按创建顺序呈现条目，并在条目旁边放置时间戳

    class Meta:   #在entry类中嵌套meta类，meta存储用于管理模型的额外信息
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."