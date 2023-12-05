from django.shortcuts import render


def templates(request):
    return render(request, 'index.html')
    