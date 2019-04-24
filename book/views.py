# Create your views here.
from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("这是首页")


# 书籍详情页
def bookDetail(request, bid):
    return HttpResponse("这是{0}书籍详情页".format(bid))


# 观看历史页
def viewHistory(request):
    return HttpResponse("这是观看历史页")


# 书籍分类页
def bookCate(requests, cateid):
    return HttpResponse("这是{0}分类".format(cateid))


# 登录页面
def logIn(request):
    return HttpResponse("这是登录页")


# 注册页面
def register(request):
    return HttpResponse("这是注册页")
