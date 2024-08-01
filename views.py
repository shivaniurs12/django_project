# todo/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm
import requests

def home(request):
    return render(request, 'todo/home.html')

def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo added successfully!")
        else:
            messages.error(request, "Error adding todo!")
    form = TodoForm()
    todo_list = Todo.objects.all()
    context = {
        'title': "Todo List",
        'forms': form,
        'list': todo_list,
    }
    return render(request, 'todo/index.html', context)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.success(request, "Todo removed successfully!")
    return redirect('/')

def youtube_search(request):
    query = request.GET.get('query')
    results = []
    if query:
        api_key = 'AIzaSyBZAgFep0o_BMOyzYMOvR2ztVzXflGPmTA'
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json().get('items', [])
    return render(request, 'todo/youtube_search.html', {'results': results})

def dictionary(request):
    query = request.GET.get('query')
    result = {}
    if query:
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{query}'
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()[0]
    return render(request, 'todo/dictionary.html', {'result': result})

def wikipedia_search(request):
    query = request.GET.get('query')
    api_key='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI4YzEwNzFlZGI2NDI3NWNmODIxODYxMjA2YzZmMzQxZCIsImp0aSI6ImI2NWVkYjQ5ZjQ2MTRkYzJmMmIwNzI1Y2I3NDU3ZmRhZDAxMjhhODEzMGZkOTc4MTM4YjhkMjE1ODNiMzg4ODcxOTFjZmVhMmFiNWViYTMyIiwiaWF0IjoxNzIyMjI3NTQyLjcxOTQxMSwibmJmIjoxNzIyMjI3NTQyLjcxOTQxNywiZXhwIjozMzI3OTEzNjM0Mi43MTcyLCJzdWIiOiI3NjE1ODAwMiIsImlzcyI6Imh0dHBzOi8vbWV0YS53aWtpbWVkaWEub3JnIiwicmF0ZWxpbWl0Ijp7InJlcXVlc3RzX3Blcl91bml0Ijo1MDAwLCJ1bml0IjoiSE9VUiJ9LCJzY29wZXMiOlsiYmFzaWMiXX0.pobtqC-DnyurOIkFgCfxMHl0Q-LoAaPm3GJNxbDGnNx-2XNQDpllv0ahx8i5s-UNp6CW9vgrrrPAOhlCjVRTFhlxM8gfplUq2U5p0SYgsDZadnbhbTDJOi-M6MXca1kVkrr9tc9nP_U0t8Q3kv1ZL5ZH5QuCg4Z-OiVr8H-kvyfaKbrw9G4TcND59rrZsHQkYoc9dE6Ecgudi4ELGYs_BDd00mP2iQaBylCWKUmkYmYek4ci7SNeHCYn9RYCewYy5n3tVbnXX92cdUoH5DnIf0wm2w-QPj0wxIXbnr-V6R9oI0fRV-UBBGcDMOuquiViYvJ1yMgVRhpz3GHW3vLVZhyfMUpw8zRTGuIU5HHIDdknOT3mODvMxJoqELnpNiouRd1dR9dq4IZPh1egmMVY7UFX9gBVzyqDuWtEnTI8OJqFmV1aNzybZ6PQBBqrEuExIHLfrXXXFbce099Bfz6vT835W3FmkMuLoh_WRvySl_pTC1J2pGL-mhsao3DWitrHdufDSV6Z3d4HYgMbO9d1_7JgG08WxY6We2rPivWiFbdU_ghuJz8poxymShzX5mafX70KUT-Au_7K-iX85X123F6vxxYs9ljldPSNbmU2i9ihBoMbkyAu10fqvJlm5JeNIp-I223kwLopZNo5V-esWOi8EB0GlcYRPoPVdkC5-eo'
    results = []
    if query:
        url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json&origin=*&srapi={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json().get('query', {}).get('search', [])
    return render(request, 'todo/wikipedia_search.html', {'results': results})
