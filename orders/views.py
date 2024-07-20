from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    '''Извлечение текущей корзины'''
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()  # валидация отправленных данных и создание нового заказа
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистить корзину
            cart.clear()
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
        else:
            form = OrderCreateForm()
            return render(request,
                          'orders/order/create.html',
                          {'cart': cart, 'form': form})
