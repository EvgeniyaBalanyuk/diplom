from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

'''Добавление товаров в корзину'''


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(  # позволяет пользователю выбирать кол-во от 1 до 20
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,  # позволяет прибавлять или переопределять товар в корзине
                                  initial=False,
                                  widget=forms.HiddenInput)
