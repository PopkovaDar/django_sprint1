from django.shortcuts import render
# Create your views here.


def about(request):
    about_name = 'pages/about.html'
    return render(request, about_name)


def rules(request):
    rules_name = 'pages/rules.html'
    return render(request, rules_name)
