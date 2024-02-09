from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task 
from django.shortcuts import get_object_or_404, redirect
from .forms import CreateNewFormTask, CreateNewFormProject

# Create your views here.
def index(request):
    title = "Welcome to Django Course!!"
    return render(request, "index.html", {
        "title": title
    })

def about(request):
    return render(request, "about.html")

def hello(request, id):
    result = id + 100 * 2
    return HttpResponse("Hello %s" % result)

def projects(request):
    #listProjects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects.html", {
        "projects": projects
    })

def tasks(request):
    #taskFindOut = Task.objects.get(id = idParam)
    #taskFindOut = get_object_or_404(Task, id = idParam)
    listTask = Task.objects.all()
    return render(request, "task.html", {
        "listTask": listTask 
    })
    
def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {
        "form": CreateNewFormTask()
    })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect("task")

def create_project(request):
    if request.method == "GET":    
        return render(request, "create_project.html",{
            "form": CreateNewFormProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect("projects")
    
def project_detail(request, id):
    projectName = Project.objects.get(id=id)
    tasksName = Task.objects.filter(project_id=id)
    return render(request, 'detail.html', {
        'projectName': projectName,
        'tasksName': tasksName
    })