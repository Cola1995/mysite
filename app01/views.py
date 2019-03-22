from django.shortcuts import HttpResponse, render,redirect


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