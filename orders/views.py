from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
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
            # запустить асинхронное задание
            order_created.delay(order.id)
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
        else:
            form = OrderCreateForm()
            return render(request,
                          'orders/order/create.html',
                          {'cart': cart, 'form': form})
