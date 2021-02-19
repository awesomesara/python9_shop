from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404

from product.models import Category, Product


def homepage(requests):
    categories = Category.objects.all()
    # SELECT * FROM product_category;
    return render(requests, 'product/index.html', {'categories': categories})

# 1 вариант получения продуктов одной категории product/category
# def products_list(requests, category_slug):
#     # products = Product.objects.all()
#     # 1 вариант
#     # if Category.objects.filter(slug=category_slug).exists(): проверка по самой категории
#     #     raise Http404
#     # 2 варинат
#     products = get_list_or_404(Product, category_id=category_slug)
#     # 3 вариант
#     # category = get_object_or_404(Category, category_id=category_slug)
#     # product = Product.objects.filter(category=category)
#     #
#     # products = Product.objects.filter(category_id=category_slug)  #queryset- обьект где хранятся условия
#     return render(requests, 'product/products_list.html', {'products': products})

# product/?category
# def products_list2(requests):
#     category_slug = requests.GET.get('category')
#     products = Product.objects.all()
#     if category_slug is not None:
#         products = products.filter(category_id=category_slug)
#     return render(requests, '', {'products': products})

# TODO: переписать вьюшку product_list +
# TODO: добавить деталь продукта +
# TODO: сделать переход из категорий в листинг продуктов +
# TODO: подключение картинок для товаров +
# TODO: переписать вьюшки на СBV
# all()- выводит все обьекты моделей
#SELECT * FROM table_name;

# Category.objects.filter(...).all()

# filter() - фильтрует результат queryset запроса
# SELECT * FROM table WHERE  ...;

# exclude(условие_id = 1) - он исключает из результатов обьекты, отвечающие условию
# SELECT * FROM table WHERE category != 1;

# order_by()- сортировка результатов
# Product.objects.order_by('price')
# SELECT * FROM product ORDER BY price ASC;
#
# Product.objects.order_by('-price')
# SELECT * FROM product ORDER BY price DESC;
#
# Product.objects.order_by('price', 'popularity')
# SELECT * FROM product ORDER BY price ASC, popularity  ASC;
#
# Product.objects.order_by('?') - рандомная сортировка / не желательно использовать

# Product.objects.all() ->
# <QuerySet:["Мясо","Картошка", "Молоко"]
# Product.objects.reverse()
# <QuerySet:["Молоко","Картошка","Мясо"]

# distinct() - возвращает уникальные значения
# Product.objects.values_list('category', flat=True) - вернется в одном списке не в тюплее
# ['фрукты',"фрукты","мясо","мясо"]
# Product.objects.values_list('category', flat= True).distinct()
# ['фрукты',"мясо"]
# Product.objects.all() - вытаскивает в виде листа
#
# Product.objects.values() - вытаскивает обьекты в виде словаря
# как  значения принимает поля
#
# Product.objects.values_list() - вытаскивает обьекты в виде тюплов в листе
# можно указать поля
#
# Product.objects.values_list('title') ->
# <QuerySet:[("Молоко"),("Мясо")]>
#
# Product.objects.values_list('title', flat=True) -> flat используем для того чтобы убрать скобки и сделать просто лист
# <QuerySet:["Молоко","Мясо"]>

# Product.objects.none()
# <QuerySet:[]>
#
# select_related()
# product = Product.objects.get(id=1)
# product.category -запрос в БД
#
# product = SELECT * FROM product WHERE id= 5;
# SELECT * FROM category WHERE id = prod.id;
#
#
# product = Product.objects.select_related('category').get(id=1)
# product.category - запроса нет
#
# SELECT * FROM product AS join ctegory
#
# prefetch_related()
# categories = Category.objects.filter(..)
# for cat in categories:
#     cat.product_set.all()
# SELECT * FROM category WHERE ...;
# SELECT * FROM category WHERE id=4;
# SELECT * FROM category WHERE id=5;
# SELECT * FROM category WHERE id=6;
#
# при помощи prefetch_related() можно облегчить жизнь
# categories = Category.objects.prefetch_related().filter(..)
# for cat in categories:
#     cat.product_set.all()
# SELECT * FROM category WHERE ...;
# SELECT * FROM category WHERE id IN (4,5,6);
#
# defer()
# id, title, description price, category_id
# Product.objects.all()
# # SELECT * FROM products;
# Product.objects.defer('price, category_id')
# SELECT id, title, description FROM products;
#
#
# only()
# Product.objects.only('price, category_id')
# SELECT price, category_id FROM products;
#
# get() - возвращает один обьект
# он ищет по идентификатору
# Product.objects.get(iExistd=1) ->
#
# если нет обьекта по условию:
# Product.objects.get(id=100) -> Product.DoesNotExist
#
# Если get находит несколько обьктов:
# error: Product.MultipleObjectsReturned
#
# create() -позволяет создать новые обьекты
# Product.objects.create(title='Пшено', description = 'fbhb'....)
#
# prod= Product(title='Пшено', description = 'fbhb'....)
# prod.save()
#
# get_or_create(условие) - выбирает обьект отвечающий условию, если обьекта нет, то он создает новый
#
# update_or_create() - обновляет или создает обьекты
#
# bulk_create(list) - позволяет создатьодновременно несколько обьектов
# bulk_update() - позволяет обновить несколько обьектов
#
# count() - звращает количество результтов в queryset
#
# first(), last()
# Product.objects.first() - первое значение
#
# earliest(), latest()
# Product.objects.earliest('price') - первое значение по цене, он без ордер бай отсортирует и возьмет первое значение
#
# exist() = проверяет есть ли в queryset хоть один результат
#
# Product.objects.filter(price__gt=2000).exist() -> True/False
#
# delete() - удаляет результаты queryset
# Product.objects.filter(category_id=2).delete()
#
# explain() - возвращает sql запрос queryset
# Product.objects.all().explain() -> SELECT * FROM products;
#
# integer lookup field:
#
# __gt -> больше
# __lt -> меньше
# __gte -> >=
# __lte -> <=

# # text lookup field:
# __startswith - LIKE "A%"
# __istartswith - ILIKE 'A%'
#
# __contains - LIKE '%day%'
# __icontains - ILIKE '%DAY%'
#
# __endswith - LIKE "%J"
# __iendswith - ILIKE "%J"
#
# __exact = 'Milk' -> WHERE title = 'Milk'
# __iexact = 'Milk' -> WHERE title ILIKE 'Milk'
#
# category__isnull = True -> WHERE category IS NULL;
# category__isnull = False -> WHERE category IS NOT NULL;
#
# id__in = [1,2,3,4,5] -> WHERE id IN (1,2,3,4,5);
#
# Order.objects.filter(date__range = (start_date, stop_date)) -> WHERE date BETWEEN start_date AND end_date;


def product_list(request, category_slug):
    if not Category.objects.filter(slug=category_slug).exists():
        raise Http404('нет такой категории')
    products = Product.objects.filter(category_id=category_slug)
    return render(request, 'product/products_list.html', {'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_details.html', {'product': product})






