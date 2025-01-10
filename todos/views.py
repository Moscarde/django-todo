from django.shortcuts import render

def todo_list(request):
    nome = "Gabriel"
    sobrenomes = ["Silva", "Moscarde"]
    return render(request, "todos/todo_list.html", {"nome": nome, "sobrenomes": sobrenomes })