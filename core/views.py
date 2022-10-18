from django.shortcuts import render
from .models import Contact, Post
from core.models import Qa
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


class PostDetail(ListView):
    template_name = 'core/post.html'
    context_object_name = 'post'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(slug=slug).first()


class Blog(ListView):
    template_name = 'core/blog.html'
    ordering = '-created'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(publish=True)


@login_required(login_url='/login')
def contact(request):
    contact = Contact.objects.all().first()
    context = {
        'contact': contact
    }
    return render(request, 'core/contact.html', context)


def manifest(request):
    contact = Contact.objects.all().first()
    qas = Qa.objects.all()
    context = {
        'qas': qas,
        'contact': contact,
    }
    return render(request, 'manifest.html', context)


def error_404(request, exception):
    return render(request, 'core/404.html', status=404)


