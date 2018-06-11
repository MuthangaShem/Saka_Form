from django.shortcuts import render, redirect


# @login_required
def home(request):
    return render(request, 'index.html')
