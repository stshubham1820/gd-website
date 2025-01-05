from django.shortcuts import render
from django.http import JsonResponse
from .models import notify


# Create your views here.
def home_view(request):
    return render(request , 'index-slides.html')


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('EMAIL')
        if email:
            notify.objects.create(email=email)
            return JsonResponse({'message': 'Subscription successful!'}, status=200)
        else:
            return JsonResponse({'message': 'Email is required!'}, status=400)
    return JsonResponse({'message': 'Invalid request method.'}, status=405)