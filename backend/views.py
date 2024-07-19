from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

'''Набор запросов QuerySet фильтруется с параметром available=True, 
чтобы получать только те товары, которые имеются в наличии'''


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:  # опциональный параметр category_slug используется для дополнительной фильтрации товаров по заданной категории
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


'''Представление для извлечения и отображения одного товара'''


def product_detail(request, id, slug):  # id и slug чтобы извлекать экземпляр класса Product
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

