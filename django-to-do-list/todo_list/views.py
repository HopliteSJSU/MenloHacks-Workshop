from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request): 

    if request.method == 'POST': 
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('The todo list has been updated!'))
            return render(request, 'index.html', {'all_items': all_items})

    else: 
        all_items = List.objects.all
        return render(request, 'index.html', {'all_items': all_items})

def about(request):
    return render(request, 'about.html')

def delete(request, list_id):
        item = List.objects.get(pk=list_id)
        # Your code here
        return redirect('index')

def completed(request, list_id):
        item = List.objects.get(pk=list_id)
        # Your code here
        return redirect('index')

def not_complete(request, list_id):
        item = List.objects.get(pk=list_id)
        # Your code here
        return redirect('index')

def edit(request, list_id):
        if request.method == 'POST': 
                item = List.objects.get(pk=list_id)
                form = ListForm(request.POST or None, instance=item)

                if form.is_valid():
                        form.save()
                        messages.success(request, ('Todo has been edited!'))
                        return redirect('index')

        else: 
                item = List.objects.get(pk=list_id)
                return render(request, 'edit.html', {'item': item})