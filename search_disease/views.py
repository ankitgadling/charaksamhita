# views.py in myapp
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .search import disease_treatment,translate_to_hindi
from .models import Ebook

@ xframe_options_sameorigin
def viewEbook(request):
    ebooks=Ebook.objects.all()
    # if request.method=="GET":
    ebooks={'ebooks':ebooks}
    print(ebooks)
    return render(request, "view.html",ebooks)


def home(request):
    return render(request, 'home.html')



def search(request):
    query = request.GET.get('q')
    if query:
        query=translate_to_hindi(query)
        results = disease_treatment(query)
        # result=extract_slokas_and_meanings(results)
        # print(result)
    else:
        results = None
    return render(request, 'search.html', {'results': results,'query':query})


