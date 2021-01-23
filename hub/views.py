from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User


# We are bringing in our data from modles nad we are importing our Post class

# Create your views here.
def home(request):
    return render(request,'hub/home.html') # This has to have the sub and then the name of the file The third argument allows us to acces the post data that we have just made

# class views look for templates that they need <app>/<model>_<viewtype>.html or hub/post_list.hmtl
class PostListView(ListView):
    model = Post
    template_name= 'hub/ArticleBlog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

class UserPostListView(ListView):
    model = Post
    template_name = 'hub/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): # We can inherent  two of these
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView): # We can inherent  two of these
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView): # We can inherent  two of these
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request,'hub/about.html',{'title':'About Title'})

def NoteCanvas(request):
    return render(request,'hub/NoteCanvas.html')

def ArticleBlog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'hub/ArticleBlog.html',context)

# we can make class based views that have more function than these functino based views
