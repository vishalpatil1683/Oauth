from django.shortcuts import render

# Create your views here.


def index_view(request):
    context = {
        "Title": "Datachamps"
    }
    return render(request, 'powerbi_api/index.html', context=context)
    

# def power_api(request):
#     pass