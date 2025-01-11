from datetime import date

from django.urls import reverse_lazy
from django.views.generic import View, CreateView, DeleteView, ListView, UpdateView
from django.shortcuts import get_object_or_404, redirect

from .models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = "todos/todo_list.html"


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Todo, pk=pk)
        task.finished_at = date.today()
        task.save()
        return redirect("todo_list")
