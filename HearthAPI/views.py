from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Cards

# Create your views here.
page = 1
cards_per_page = 10

def index(request):

    card_dict_resp = {}

    try:
        for i in range(1, cards_per_page + 1):
            current_card = Cards.objects.get(id=i)

            card_dict_resp[current_card.card_id] = create_card_dict(current_card)
    except Exception as err:
        return HttpResponse('Unknown Error: %s' % err.message)


    return JsonResponse(card_dict_resp)

def get_page(request, page_number):

    starting_id = page_number * cards_per_page + 1
    card_dict_resp = {}

    for i in range(starting_id, starting_id + 10):
        current_card = Cards.objects.get(id=i)

        card_dict_resp[current_card.card_id] = create_card_dict(current_card)

    return JsonResponse(card_dict_resp)


def create_card_dict(card):

    return {
        'card_name': card.card_name,
        'card_text': card.card_text,
        's3_image_link': card.s3_image_link
    }