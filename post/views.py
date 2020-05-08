from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from .models import Post
from .forms import PostForm


def home_page(request):
    posts = Post.objects.order_by('published_date').reverse()[:10]
    # needs_to_be_appended is 0 if there is more than 9 posts and their count is divisible by 3
    # is 1 if there is less than 10 posts and their count is not divisible by 3
    needs_to_be_appended = int(len(posts) < 10 and (len(posts) - 1) % 3 != 0)
    # append N time to make posts count divisible by 3 with NONE if needs_to_be_appended is 1.
    posts = list(posts) + [None] * needs_to_be_appended * (3 - ((len(posts)-1) % 3))
    return render(request, 'home.html', {'posts': posts})

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) #commit=False cuz we need to set published_time first
            post.published_date = timezone.now()
            post.save()
            return redirect(reverse('home'))
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form, 'sufix': '/ Добавить статью'})