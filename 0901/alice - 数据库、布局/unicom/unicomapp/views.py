from django.shortcuts import render

# Create your views here.
from unicomapp.models import Index

def index(request):
	context = {
	"title" : "中国联通"
	}
	index_page = render(request, 'index.html', context)
	return index_page