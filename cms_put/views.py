from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages


# Create your views here.

def main_page(request):
    response = '<h1>Ejercicio 15.6: Django-CMS_PUT</h1>'
    response += '<h3>(Use GET or PUT to add new pages).</h3>'
    pages_list = Pages.objects.all()
    if len(pages_list) != 0:
        response += '<p>Saved pages:</p>'
        response += '<ul>'
        for page in pages_list:
            response += '<p>' + str(page) + '</p>'
        response += '</ul>'
    return HttpResponse(response)


def page_searching(request, resource):

    if request.method == 'GET':
        try:
            pageSearched = Pages.objects.get(name=resource)
            return HttpResponse(pageSearched.page)
        except Pages.DoesNotExist:
            return HttpResponseNotFound('<h1>' + resource + ' not found.</h1>')
    elif request.method == 'PUT' or request.method == 'POST':
        newPage = Pages(name=resource, page=request.body)
        newPage.objects.save()
        return HttpResponse('<h1>Page added successfully.')
    else:
        return HttpResponse('<h1>Invalid method.</h1>')
