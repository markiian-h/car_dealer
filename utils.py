from django.db.models import Max, Min

from car.models import Car
from dealers.models import NewUser

sidebar = [
    {'title': 'Cars', 'url_name': 'cars'},
    {'title': 'My cars', 'url_name': 'my_cars'},
    {'title': 'My orders', 'url_name': 'orders'},
]

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add new car', 'url_name': 'add_car'},
        {'title': 'Contact us', 'url_name': 'contact'},
        ]

sidebar_list_url = [i['url_name'] for i in sidebar]
sidebar_list_url.append('find_car')


def update_car_views(pk):
    car = Car.objects.get(pk=pk)
    car.views += 1
    car.save()
    return car.views


def get_min_price():
    return Car.objects.aggregate(Min('price'))['price__min']


def get_max_price():
    return Car.objects.aggregate(Max('price'))['price__max']


def get_cars_year():
    return Car.objects.values_list('year', flat=True)


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        user_sidebar = sidebar.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
            user_sidebar.pop(1)
            user_sidebar.pop(2)
        else:
            if not self.request.user.is_dealer:
                user_sidebar.pop(1)
        context['menu'] = user_menu
        context['sidebar'] = user_sidebar
        context['sidebar_list_url'] = sidebar_list_url
        context['path'] = self.request.path.split('/')[1]
        context['dealers'] = NewUser.objects.filter(is_dealer=True)
        context['cars_year'] = sorted(get_cars_year())
        context['min_price'] = get_min_price()
        context['max_price'] = get_max_price()

        return context
