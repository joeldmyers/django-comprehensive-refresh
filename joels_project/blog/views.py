from django.shortcuts import render

posts = [
    {
        'author': 'Joel',
        'title': 'Blog Post 1',
        'content': 'This is my first post.',
        'date_posted': 'Oct 27 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'This is my second post.',
        'date_posted': 'Oct 26 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
