from django.shortcuts import HttpResponse, render,redirect
from app01 import models


def login(request):
    error_msg=""
    if request.method == "POST":


        # print(request.POST.get('password',None))
        if request.POST.get('email',None) == "ma@123" and request.POST.get("password",None) =="123":
            # return HttpResponse("登录成功")  #返回的response必须有返回值
            return redirect("http://www.luffycity.com")
        else:
            error_msg="邮箱或密码错误"
    return render(request, "login.html",{"error":error_msg})

def user_list(request):
    '''
    查询用户
    :param request:
    :return:
    '''
    # 使用ORM工具查询所有用户
    ret = models.UserInfo.objects.all()
    # print(ret[0].id,ret[0].name)

    return render(request,'user_list.html',{'user_list':ret})



def add_user(request):
    if request.method=="POST":
        new_name=request.POST.get("name")  #获取页面上提交的数据
        # print(new_name)
        models.UserInfo.objects.create(name=new_name)   #ORM创建数据
        return redirect("/user_list/")  #重定向
    return render(request,"add_user.html")