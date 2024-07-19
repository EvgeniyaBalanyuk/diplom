from .cart import Cart

'''Установка корзины в контекст запроса'''


def cart(request):
    return {'cart': Cart(request)}
