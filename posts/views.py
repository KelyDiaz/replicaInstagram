from datetime import datetime

from django.shortcuts import render

posts = [
    {
        'title': 'One',
        'user': {
            'name': 'Kely Diaz',
            'picture': 'https://picsum.photos/60/60/?image=1027',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/1005/300/200',
    },
    {
        'title': 'Two',
        'user': {
            'name': 'Lucas Mora',
            'picture': 'https://picsum.photos/id/1074/60/60/',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/1011/300/200',
    },
    {
        'title': 'Three',
        'user': {
            'name': 'Arturo Calle',
            'picture': 'https://picsum.photos/id/132/60/60/',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/1018/300/200',
    }
]


def list_posts(request):
    return render(request, 'feed.html', {'posts': posts})
