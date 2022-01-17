from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from contas.models import Post, Contact, Category
from contas.forms import ContactForm
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.

def inicioBlog(request):
    all_category = Category.objects.order_by('id')
    post_random = Post.objects.order_by('-id')
    paginator = Paginator(post_random, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'all_category': all_category
    }
    return render(request, "contas/index.html", context)

def aboutBlog(request):
    return render(request, "contas/about.html")

def postBlog(request,id):
    page = Post.objects.get(pk=id)
    context = {
        'page': page
    }
    return render(request, "contas/post.html", context)

def contactBlog(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.phone = form.cleaned_data['phone']
            data.save()
            messages.success(request, 'Mensagem enviada!')
            return HttpResponseRedirect('/contact/')

    form = ContactForm
    context = {
        'form': form
    }
    return render(request, "contas/contact.html", context)

def filterView(request,id):
    all_category = Category.objects.order_by('id')
    id_c = id
    post = Post.objects.filter(category=id_c)
    paginator = Paginator(post, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'id_c': id_c,
        'all_category': all_category
    }
    return render(request, "contas/filter.html", context)


def baseView(request):
    all_category = Category.objects.order_by('id')
    context = {
        'all_category': all_category
    }
    return render(request, "contas/base.html", context)


def testeView(request,id):
    all_category = Category.objects.order_by('id')
    id_c = id
    post = Post.objects.filter(category=id_c)
    context = {
        'post': post,
        'id_c': id_c,
        'all_category': all_category

    }
    return render(request, "contas/teste.html", context)


