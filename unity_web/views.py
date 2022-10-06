
from django.shortcuts import render, redirect
from .models import passage
from .forms import PsgForm

def index(request) :
    return render(request, 'passage.html')
   
def createform(request) :
    if request.method == 'POST' :
        form = PsgForm(request.POST)

        if form.is_valid() :
            psg = passage()
            psg.content = form.cleaned_data['content']
            psg.save()
            return redirect('index')

        else :
            form = PsgForm()
        
        return render(request,'form_create.html',{'form':form})


