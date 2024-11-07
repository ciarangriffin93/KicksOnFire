from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


# List view for post
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/news.html"
    paginate_by = 6


# Detail view for event including comments
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.blog_comments.all().order_by("-created_on")
    liked = post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
    comment_count = post.blog_comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(
                request,)
            return redirect('post_detail', slug=slug) 

    comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'liked': liked,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form,
    })


# Like/Unlike event
def post_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', slug=slug)

# Views for comment
# Create a new comment
class NewComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment.html'

    def form_valid(self, form):
        # Set author and post before saving
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        
        # Save the form and add a success message
        response = super().form_valid(form)
        messages.success(self.request, "Your comment has been submitted.")
        return response

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})


# Edit a comment
class EditComment(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/edit_comment.html"

    def form_valid(self, form):
        messages.success(self.request, "Your comment has been updated")
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        # Update to use 'post' instead of 'event'
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})


# Delete a comment
class DeleteComment(UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})