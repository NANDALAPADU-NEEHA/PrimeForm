from django.shortcuts import render

# Create your views here.
def func1(request):
    result=None
    print(request.GET)
    if request.method=="POST":
        a=int(request.POST.get('sname'))
        for i in range(1, int(a**0.5)+1,):
            if a%i==0:
                result=False
            else:
                result=True
    return render(request,'index.html',{'res':result})
