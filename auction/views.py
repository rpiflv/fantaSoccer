from django.shortcuts import render


def start_auction(request):
    return render(request, 'auction/start_auction.html')
