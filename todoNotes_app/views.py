from django.shortcuts import render
from todoNotes_app.models import TODONotes
from django.http import HttpResponseRedirect
# Create your views here.
def todo_list(request):
    todos = TODONotes.objects.all()
    records = {"all_todos":todos}
    return render(request, "index.html",records)

def add_todo(request):
    if request.method == 'POST':        
        new_todo_item = TODONotes(content = request.POST["new_todo"])
        new_todo_item.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "add_todo.html")

def delete_todo(request,pk):
    delete_todo_item = TODONotes.objects.get(pk=pk)
    delete_todo_item.delete()
    return HttpResponseRedirect("/")

def item_update(request,pk):
    if request.method == "POST":
        update_item = TODONotes.objects.get(pk=pk)
        update_item.content = request.POST["edit_todo"]
        update_item.save()
        return HttpResponseRedirect("/")
    else:
        update_item = TODONotes.objects.get(pk=pk)
        return render(request, "item_edit.html", {"todo_edit": update_item},)

   
