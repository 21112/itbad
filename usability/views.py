from django.shortcuts import render

def usability_home(request):
    data ={
        'title': 'Usability-Site-Audit',
        'bait': 'Haben Sie Probleme:'
    }
    return render(request, 'usability/usability_home.html',data)



def description_usability(request):
    data = {
        'title': 'Что такое юзабилити сайта?'
        

    }
    return render(request, 'usability/description_usability.html',data)