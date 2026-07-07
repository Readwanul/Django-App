from django.shortcuts import render

def page2(request):
    Items=["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    Name="John Doe"
    return render(request, 'ServerApp/page2.html', {'items': Items, 'name': Name})

def page3(request):
    return render(request, 'ServerApp/page3.html')

def page4(request):
    return render(request, 'ServerApp/page4.html')


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
