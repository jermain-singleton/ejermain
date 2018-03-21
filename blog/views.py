from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

from .models import Post, Entry
from .forms import PostForm, EntryForm

# @login_required
def posts(request):
    """Show all posts"""
    # posts = Post.objects.filter(owner=request.user).order_by('date_added')
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'posts.html', context)

@login_required
def post(request, post_id):
    """Show a single post and all its entries"""
    post = Post.objects.get(id=post_id)
    # Make sure the posts belongs to the current user
    #if post.owner != request.user:
        #raise Http404
        
    entries = post.entry_set.order_by('-date_added')
    context = {'post': post, 'entries': entries}
    return render(request, 'post.html', context)

@login_required
def new_post(request):
    """Add a new post"""
    if request.method != 'POST':
        # No data to submit; create blank form.
        form = PostForm()
    else:
        # POST data submitted; process data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('posts'))
    context = {'form': form}
    return render(request, 'new_post.html', context)

@login_required
def new_entry(request, post_id):
    """Add a new entry for a particular post"""
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        # No data to submit; create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.post = post
            new_entry.save()
            return HttpResponseRedirect(reverse('post', args=[post_id]))
    
    context = {'post': post, 'form': form}
    return render(request, 'new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit existing entry"""
    entry = Entry.objects.get(id=entry_id)
    post = entry.post
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # initial request prefill form with current entry
        form = EntryForm(instance=entry)
    else:
        #POST data submitted and process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post', args=[post.id]))

    context = {'entry': entry, 'post': post, 'form': form}
    return render(request, 'edit_entry.html', context)

    