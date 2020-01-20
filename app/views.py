from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from app import forms

# Create your views here.
def sample1(request):
    if request.method=="POST" and request.FILES:
        img=request.FILES['image']
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        file_url=fs.url(filename)

    return render(request,'sample1.htm',context={'filename':file_url})

def sample2(request):
    file_url=""
    if request.method=="POST" and request.FILES:
        form=forms.FormDemo(request.POST,request.FILES)
        if form.is_valid():
            img=form.cleaned_data['image']
            fs=FileSystemStorage()
            filename=fs.save(img.name,img)
            file_url=fs.url(filename)
    form=forms.FormDemo()

    return render(request,'sample1.htm',context={'filename':file_url,'form':form})

def regsiter(request):
    if request.method=='POST' and request.FILES:
        userform=forms.UserForm(request.POST)
        profileform=forms.ProfileForm(request.POST,request.FILES)
        if userform.is_valid() and profileform.is_valid():
            user=userform.save(commit=False)
            user.set_password(userform.cleaned_data["password"])
            user.save()
            profile=profileform.save(commit=False)
            profile.user=user
            profile.save()
    userform=forms.UserForm()
    profileform=forms.ProfileForm()
    return render(request,'register.htm',context={'user':userform,'profile':profileform})