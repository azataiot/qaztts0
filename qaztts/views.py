import json
from django.shortcuts import render

# Create your views here.

def kzlatinstr(string):
    with open('dict.json', 'r') as f:
        KQ=json.load(f)
    p = string
    for key, value in KQ.items():
        p = p.replace(key, value)
    return p


def HomeView(request):
    if request.method == 'GET':
        kzDefault = r"/ɑːzɑːt eɪ aɪ/"
        content={
            'kz' : kzDefault,
        }
        return render(request, 'index.html',content)

    if request.method == 'POST':
        kz = request.POST.get('kz', None)
        content = {
            'kz' : kzlatinstr(kz),
        }
        return render(request, 'index.html', content)
