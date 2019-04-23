from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {

    })


def about(request):
    return render(request, 'about.html', {

    })


def project(request):
    return render(request, 'project.html', {

    })


def services(request):
    return render(request, 'services.html', {

    })


def contact(request):
    return render(request, 'contact.html', {

    })


def components(request):
    return render(request, 'components.html', {

    })
