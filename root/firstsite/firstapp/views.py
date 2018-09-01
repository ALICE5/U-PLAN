from django.shortcuts import render

def index(request):
	context = {
	"title" : "中国联通"
	}
	index_page = render(request, 'index.html', context)
	return index_page

def about(request):
	index_page = render(request, 'about.html')
	return index_page

# Create your views here.

