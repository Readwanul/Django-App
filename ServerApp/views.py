from django.shortcuts import get_object_or_404, redirect, render
from .models import Student

def page2(request):
    Items=["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    Name="John Doe"
    return render(request, 'ServerApp/Page2.html', {'items': Items, 'name': Name})

def page3(request):
    return render(request, 'ServerApp/page3.html')

def page4(request):
    students = Student.objects.all()
    return render(request, 'ServerApp/page4.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        student = Student(name=name, address=address)
        student.save()
    return redirect('page4')

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('page4')

def Search(request, student_id):
    query = request.GET.get('query', '')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'ServerApp/search_results.html', {'students': students, 'query': query})




def home(request):
    context = {
        "students": [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Emma"
        ]
    }
    return render(request, "ServerApp/home.html", context)

# Create your views here.
