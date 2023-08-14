from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Page
from django.contrib.auth.decorators import login_required


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def about(request):
    return render(request, 'about.html')

def pages(request):
    pages = Page.objects.all()
    return render(request, 'pages.html', {'pages': pages})

@login_required
def create_page(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        page = Page.objects.create(title=title, content=content)
        return redirect('pages')
    else:
        return render(request, 'create_page.html')

@login_required
def update_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    if request.method == 'POST':
        page.title = request.POST['title']
        page.content = request.POST['content']
        page.save()
        return redirect('pages')
    else:
        return render(request, 'update_page.html', {'page': page})

@login_required
def delete_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    if request.method == 'POST':
        page.delete()
        return redirect('pages')
    else:
        return render(request, 'delete_page.html', {'page': page})

def get_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'get_page.html', {'page': page})


def about_me(request):
    return render(request, 'about_me.html')