from django.shortcuts import render

# Create your views here.

def post_list_view(request):
	return render(request,'blog/post_list.html',{})
