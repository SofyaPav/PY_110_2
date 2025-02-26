from django.shortcuts import render
from django.urls import path
from django.contrib.auth import get_user
from logic.services import view_in_wishlist
from store.models import DATABASE
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from logic.services import add_to_wishlist, remove_from_wishlist, view_in_wishlist

def wishlist_view(request):
    if request.method == "GET":
        current_user = get_user(request).username
        data = view_in_wishlist(request)[current_user]
        products = []

        for product_id in data['products']:
            product = DATABASE.get(product_id)
            if product:
                products.append(product)

        return render(request, 'wishlist/wishlist.html', context={"products": products})


@login_required(login_url='login:login_view')
def wishlist_add_json(request, id_product):
    if request.method == "GET":
        result = add_to_wishlist(request, id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в избранное"},
                                json_dumps_params={'ensure_ascii': False})
        return JsonResponse({"answer": "Неудачное добавление в избранное"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})

@login_required(login_url='login:login_view')
def wishlist_del_json(request, id_product):
    if request.method == "GET":
        result = remove_from_wishlist(request, id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из избранного"},
                                json_dumps_params={'ensure_ascii': False})
        return JsonResponse({"answer": "Неудачное удаление из избранного"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})

@login_required(login_url='login:login_view')
def wishlist_json(request):
    if request.method == "GET":
        current_user = get_user(request).username
        data = view_in_wishlist(request)[current_user]
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

