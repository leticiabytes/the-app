from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import ToDoForm
from .models import Post

def toDo_list(request):
    template_name = 'toDo/tasks_list.html'
    form = ToDoForm(request.POST or None)

    tasks = Post.objects.all()

    context = {'object_list': tasks, 'form': form}
    return render(request, template_name, context)

@require_http_methods(['POST'])
def toDo_create(request):
    form = ToDoForm(request.POST or None)

    if form.is_valid():
        task = form.save()

    context = {'object': task}
    return render(request, 'toDo/hx/toDo_hx.html',  context)

def toDo_delete(request, pk):
    obj = Post.objects.get(pk=pk)
    obj.delete()
    return render(request, 'toDo/tasks_table.html')

def toDo_complete(request, pk):
    obj = Post.objects.get(pk=pk)
    Post.objects.filter(pk=obj.pk).update(complete=True)

    tasks = Post.objects.all()

    context = {'object_list': tasks}
    return render(request, 'toDo/tasks_table.html', context)

def toDo_incomplete(request, pk):
    obj = Post.objects.get(pk=pk)
    Post.objects.filter(pk=obj.pk).update(complete=False)

    tasks = Post.objects.all()

    context = {'object_list': tasks}
    return render(request, 'toDo/tasks_table.html', context)

def toDo_detail(request, pk):
    obj = Post.objects.get(pk=pk)
    form = ToDoForm(request.POST or None, instance=obj)

    context = {'object': obj, 'form': form}
    return render(request, 'toDo/hx/task_detail_hx.html', context)

def toDo_update(request, pk):
    obj = Post.objects.get(pk=pk)
    form = ToDoForm(request.POST or None, instance=obj)
    context = {'object': obj}

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'toDo/hx/toDo_hx.html', context)

