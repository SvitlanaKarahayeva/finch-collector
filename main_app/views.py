from django.shortcuts import render
from django.http import HttpResponse

class Finch:
    def __init__(self, breed, description, size):
        self.breed = breed
        self.description = description
        self.size = size

finches= [
    Finch('Evening Grosbeak', 'Adult male Evening Grosbeaks are yellow and black birds with a prominent white patch in the wings. They have dark heads with a bright-yellow stripe over the eye.', '16-18 cm'),
    Finch('Gray-crowned Rosy-Finch', 'Adult males are rich brown suffused with pink on the body, with gray sides of the head and a black forecrown and throat. Adult females are similar but with less extensive pink. The bill is yellow.','14-21 cm')
]

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })
    

