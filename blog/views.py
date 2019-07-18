from django.shortcuts import get_object_or_404, render
from .models import Blog
# Create your views here.
def allblogs(request):
    blogs = Blog.objects.order_by('-pub_date')
    return render(request, 'blogs/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog':detailblog})
