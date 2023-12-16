from django.shortcuts import render


def description(request):
    template = 'template/about/description.html'
    return render(request, template)
