from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', cache_page(60)(StampHome.as_view()), name='home'),
    path('', StampHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('basket/', StampBasket.as_view(), name='basket'),
    path('make_order/', MakeOrderFormView.as_view(), name='make_order'),
    path('successful_order/', SuccessfulOrder.as_view(), name='successful_order'),
    path('news/', StampNews.as_view(), name='news'),
    # path('news/', StampNews.as_view(), name='news'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('where_order/', WhereOrder.as_view(), name='where_order'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', StampCategory.as_view(), name='category'),
    path('cats/<slug:cat_id>', categories),

]