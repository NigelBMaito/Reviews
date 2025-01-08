from django.shortcuts import render

# Create your views here.
def deals_view(request):
    return render(request, 'deals/packages.html')