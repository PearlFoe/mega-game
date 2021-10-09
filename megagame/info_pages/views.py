from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .utils import read_text_from_file

def index(request):
    file_text = read_text_from_file('index_text.txt')
    text_blocks = file_text.split('\n') if file_text else None
    return render(request, 'info_pages/index.html', {'text_blocks': text_blocks})

def rules(request):
    return render(request, 'info_pages/rules.html')