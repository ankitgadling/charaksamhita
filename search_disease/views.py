# views.py in myapp
from django.shortcuts import render
from .search import disease_treatment

def home(request):
    return render(request, 'home.html')



def search(request):
    query = request.GET.get('q')
    if query:
        results = disease_treatment(query)
        # result=extract_slokas_and_meanings(results)
        # print(result)
    else:
        results = None
    return render(request, 'search.html', {'results': results,'query':query})


