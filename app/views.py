from django.shortcuts import render
from django.db.models import Count, Sum, F
from app.models import Order, Customer, Product
from datetime import date, timedelta
from django.utils import timezone

def product(request):

    order_count = Order.objects.aggregate(count=Count('id'))

    product_summ = Order.objects.aggregate(sum=Sum('quantity'))

    specific_date = date(2024, 7, 25)
    daily_sum = Order.objects.filter(sel_data=specific_date).aggregate(sum=Sum(F('quantity') * F('product__price')))

    today = timezone.now().date()

    ten_days_ago = today - timedelta(days=10)

    ten_days_sum = Order.objects.filter(sel_data__range=(ten_days_ago, today)).aggregate(sum=Sum(F('quantity') * F('product__price')))


    customer_orders = Order.objects.aggregate(sum=Sum(F('quantity') * F('product__price')))

    context = {
        'order_count': order_count,
        'product_summ': product_summ,
        'daily_sum': daily_sum,
        'ten_days_sum': ten_days_sum,
        'customer_orders': customer_orders,
    }
    return render(request, 'product.html', context)
