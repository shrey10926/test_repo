from django.shortcuts import render, redirect
from app1.models import UserUploadModel
from app1.forms import UserUploadForm
# Create your views here.

def home(request):
    
    if request.method=='POST':
        
        form = UserUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            f = form.save()
            f.user = request.user
            f.save()
            
            files = request.FILES.getlist('file')
            
            if files:
                for i in files:
                    file_instance = UserUploadModel(file = i)
                    file_instance.save()
            
        return redirect('app1-display')
    
    else:
        
        form = UserUploadForm()
    
    return render(request, 'app1/home.html', {'form' : form})


def display(request):
    
    x = UserUploadModel.objects.filter(user = request.user)
    context = {
        'x' : x
        }
    
    return render(request, 'app1/display.html', context)
