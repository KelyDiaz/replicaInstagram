from datetime import datetime

from django.http import HttpResponse

posts = [
    {
        'name': 'One',
        'user': 'Kely Diaz',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1005/300/200',
    },
    {
        'name': 'Two',
        'user': 'Lucas Mora',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1011/300/200',
    },
    {
        'name': 'Three',
        'user': 'Arturo Calle',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1018/300/200',
    }
]


def list_posts(request):
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
