from django.shortcuts import render,redirect
from django.views.generic import View
from task.forms import TodoCreateForm,TodoChangeForm
from task.models import Todos




# Create your views here.

class TodoCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TodoCreateForm()
        return render(request,"todo.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=TodoCreateForm(request.POST)
        if form.is_valid():
        #    Unpacked-->>
            Todos.objects.create(**form.cleaned_data) 
            print("Todos created")
            return render(request,"todo.html",{"form":form})
        else:
            return render(request,"todo.html",{"form":form})

    # def post(self,request,*args,**kwargs):
    #     form=TodoCreateForm(request.POST)
    #     if form.is_valid():
    #         form.save()

        
        
class TodoListView(View):
    def get(self,request,*args,**kwargs):
        qs=Todos.objects.all()
        return render(request,"todos_list.html",{"todos":qs})


class TodoDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Todos.objects.get(id=id)
        return render(request,"todo_detail.html",{"todo":qs})
    

class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todos.objects.filter(id=id).delete()
        return redirect("todo-list")
    
class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
       id=kwargs.get("pk")
       obj=Todos.objects.get(id=id)

       form=TodoChangeForm(instance=obj)
       return render(request,"todo_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Todos.objects.get(id=id)

        form=TodoChangeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("todo-list")
        else:
            return render(request,"todo_edit.html",{"form":form})
    
    



