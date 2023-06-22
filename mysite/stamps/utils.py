from django.core.cache import cache

from .models import *

menu = [{'title': 'Кошик', 'url_name': 'basket'},
        {'title': 'Новини', 'url_name': 'news'},
        {'title': 'Зворотній зв\'язок', 'url_name': 'contact'},
        {'title': 'Де моє замовлення?', 'url_name': 'where_order'}]
        # {'title': 'Увійти', 'url_name': 'login'}]

class DataMixin:
    paginate_by = 8
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.all()
            cache.set('cats', cats, 60)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(3)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context