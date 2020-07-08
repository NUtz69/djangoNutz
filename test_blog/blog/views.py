from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Pagination
from django.core.paginator import Paginator
# Search
from django.db.models import Q


# Create your views here.


# ------------
# --- POST ---
# ------------


# About view
class AboutView(TemplateView):
    # Template
    template_name = 'about.html'


# Post list view
class PostListView(ListView):
    # Pagination
    paginate_by = 3
    # Model
    model = Post

    # Get method filter (less than or equal) ?query
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # Pagination
    def listing(request):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 3) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'post_list.html', {'page_obj': page_obj})


# Post detail view
class PostDetailView(DetailView):
    # Model
    model = Post


# Create post view
class CreatePostView(LoginRequiredMixin, CreateView):
    # Login
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    # Form
    form_class = PostForm
    # Model
    model = Post


# Update post view
class PostUpdateView(LoginRequiredMixin, UpdateView):
    # Login
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    # Form
    form_class = PostForm
    # Model
    model = Post


# Delete post view
class PostDeleteView(LoginRequiredMixin, DeleteView):
    # Model
    model = Post
    # Lazy
    success_url = reverse_lazy('post_list')


# Draft list view
class DraftListView(LoginRequiredMixin, ListView):
    # Login
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    # Model
    model = Post

    # Get method filter (Publication isNull) ?query
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


# --------------
# --- Search ---
# --------------

class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


# ---------------
# --- COMMENT ---
# ---------------


# Publish post
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


# Add comment to post
@login_required
# Add method to login_required
def add_comment_to_post(request, pk):
    # Get post
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        # Comment form
        form = CommentForm(request.POST)
        if form.is_valid():
            # Models -> Post -> def approve_comments(self):
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


# Comment approve
@login_required
def comment_approve(request, pk):
    # Get comment
    comment = get_object_or_404(Comment, pk=pk)
    # Models -> Comment -> def approve(self):
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


# Comment remove
@login_required
def comment_remove(request, pk):
    # Get comment
    comment = get_object_or_404(Comment, pk=pk)
    # Post pk
    post_pk = comment.post.pk
    # Delete comment
    comment.delete()
    return redirect('post_detail', pk=post_pk)
