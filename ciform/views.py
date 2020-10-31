from django.shortcuts import render


def cif(request, *args, **kwargs):
    return render(request, 'page/ciform.html')
