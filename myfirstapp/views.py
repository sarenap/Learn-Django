from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import * #import anyform
# Create your views here.
def error_404_view(request,exception):
    return render(request,'404.html') #rickrolll

def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydictionary = {
        "name" : name,
        "age" : age,
    }
    return JsonResponse(mydictionary)

def decToBase(request, num, base): #my own convert a dec to any base
    #handle error
    orignum = num
    remainders = [] #empty list of remainders. 
    while( num > 0 ):
        rem = num % base
        remainders.insert(0,rem) #prepend
        num = num // base #floor division, round down to nearest whole num
    mydictionary = {
        "orignum" : orignum,
        "num" : num,
        "base" : base,
        "remainders": remainders,
    }
    return render(request, 'bindec.html', context=mydictionary)

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request): 
    return render(request,'second.html')

def mythirdpage(request):
    #boolean. back end logic. 
    #render to display on front end
    var = "hello world" 
    greeting = "hey how are you"
    fruits = ["dragonfruit", "mango", "grape"] #list
    num1, num2 = 3, 5 
    ans = num1 > num2
    print(ans)

    mydictionary = { #left: pass in to 3rd.html header
        "var" : var,
        "msg" : greeting ,
        "myfruits" : fruits,
        "num1" : num1,
        "num2" : num2,
        "ans" : ans,
    }
    return render(request, 'third.html' , context=mydictionary)

def myimagepage(request):
    return render(request, 'imagepage.html')

def myimagepage2(request):
    return render(request, 'myimagepage2.html')

def imagepage3(request):
    return render(request, 'imagepage3.html')

def imagepage4(request):
    return render(request, 'imagepage4.html')

def imagepage5(request, imagename):
    myimagename = str(imagename);
    myimagename = myimagename.lower();
    print(myimagename)
    if myimagename == "django": var = True
    elif myimagename == "python" : var = False

    mydictionary = {
        "var" : var,
    }
    return render(request, 'imagepage5.html', context = mydictionary)

def myform(request):
    return render(request, 'myform.html')

def submitmyform(request):
    mydictionary = {
        "var1": request.POST['mytext'],
        "var2": request.POST['mytextarea'],
        "method": request.method,
    }
    return JsonResponse(mydictionary)

def myform2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            mydictionary = {
                "form" : FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                errormsg = "Title should be in Capital"
                Errors.append(errormsg)
            import re
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' #define email @
            if not re.search(regex,email):
                errorflag = True
                errormsg = "Not a Valid Email address"
                Errors.append(errormsg)
            if errorflag != True:
                mydictionary["success"] = True
                mydictionary["successmsg"] = "Form Submitted"
            mydictionary["error"] = errorflag
            mydictionary["errors"] = Errors
            print(mydictionary)
            return render(request,'myform2.html',context=mydictionary)

    elif request.method == "GET":
        form = FeedbackForm() # FeedbackForm(None)
        mydictionary = {
            "form" : form
        }
        return render(request,'myform2.html',context=mydictionary)
    
    return HttpResponse("Invalid request") 