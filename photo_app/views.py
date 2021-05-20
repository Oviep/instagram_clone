from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from photo_app.models import Post


class PostView(ListView):
    model = Post
    template_name = 'photos/index.html'
    context_object_name = 'posts'


# def post_view(request):
#     post_details = Post.object.all()
#     context = {
#         'posts': post_details
#     }
    # return render(request, '/photos.html')
