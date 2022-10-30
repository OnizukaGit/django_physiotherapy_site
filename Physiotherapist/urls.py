"""Physiotherapist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.i18n import JavaScriptCatalog
from django.contrib import admin
from django.urls import path,re_path
from Physiotherapist_project.views import Start,PriceList,BuyProduct,PageOne,PageTwo,PageThree,\
    Bookings,Login,Logout,Register,UsersPanel,LoadProduct,LoadSession,LoadPrice,PhysiotherapistDetailsView,\
    DeleteBooking

urlpatterns = [
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('admin/', admin.site.urls),
    path('', Start.as_view(), name="start"),
    path('price-list/', PriceList.as_view(), name='Price-list'),
    path('product/', BuyProduct.as_view(), name='Product'),
    path('login/', Login.as_view(), name="Login"),
    path('logout/', Logout.as_view(), name='Logout'),
    path('register/', Register.as_view(), name="Register"),
    path('page-one/', PageOne.as_view(), name="Page1"),
    path('page-two/', PageTwo.as_view(), name="Page2"),
    path('page-three/', PageThree.as_view(), name="Page3"),
    path('booking/', Bookings.as_view(), name="Booking"),
    re_path('^username/(?P<username>.+)/$', UsersPanel.as_view(), name="UsersPanel"),
    path('ajax/product/', LoadProduct.as_view(), name='ajax_load_product'),
    path('ajax/session/', LoadSession.as_view(), name='ajax_load_session'),
    path('ajax/price/', LoadPrice.as_view(), name='ajax_load_price'),
    path('delete-page/<int:pk>', DeleteBooking.as_view(), name='Delete'),
    path('details-view/', PhysiotherapistDetailsView.as_view(), name="PhysiotherapistDetailsView"),
]


