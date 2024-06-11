from django.shortcuts import render
from django.http import HttpResponse
from . forms import myForm

def my_view(request):
    if request.method == 'POST':
        form = myForm(request.POST)

        if form.is_valid():
            return HttpResponse('Form is valid')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = myForm()

    context = {'form':form}

    return render(request, 'index.html', context)



