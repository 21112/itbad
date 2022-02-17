from django.shortcuts import render


def index(request):
    data = {
        'title': 'Usability-Site-Audit',
        'bait': 'Haben Sie Probleme:',
        'obj': {
            '1': 'Erzielt Ihre Website niedrige Conversions?',
            '2': 'Sind die meisten Werbekanäle ineffektiv?',
            '3': 'Hat Ihre Website Traffic, aber keine Verkäufe?'
        }

    }
    return render(request, 'usability/index.html', data)

def about(request):
    return render(request, 'main/about.html')

