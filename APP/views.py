from django.shortcuts import render, redirect
from .models import TODO

def home(request):
    malumotlar = TODO.objects.all()
    context = {
        'malumotlar' : malumotlar
    }
    
    return render(request, "index.html", context)

def yaratish(request):
    if request.method == "POST":
        title=request.POST.get("title")
        print(title)
        todo = TODO(
            title=title
        )
        todo.save()
        return redirect('home')
    return render (request, 'create.html')


def uzgartirish(request, pk):
    task= TODO.objects.get(id=pk)
    
    print(id)
    
    context = {
        "task" : task
    }

    if request.method == "POST":
        text = request.POST.get("title")
        
        task.title = text
       
        task.save()
        return redirect("home")
    return render(request, 'edit.html', context)




def delete(request, pk):
    task = TODO.objects.get(id=pk)
    task.delete()
    return redirect("home")


    
    
