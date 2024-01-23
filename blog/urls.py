from django.urls import path
from .views import index, computers, mans_clothes, contact, womans_clothes, devicedetailview, buy, about, \
    LaptopsDeleteView, LaptopsCreateView, LaptopsUpdateView, laptopDetail

urlpatterns = [
    path("index/", index, name='index'),
    path("computers/", computers, name='computers'),
    path("contact/", contact, name='contact'),
    path("mans-clothes/", mans_clothes, name='mans-clothes'),
    path("womans-clothes/", womans_clothes, name='womans-clothes'),
    path("device/<int:id>", devicedetailview, name='device_detail_view'),
    path("buyingsomething/", buy, name='buy'),
    path("allaboutus/", about, name='about'),
    path("laptop/<slug:laptop>", laptopDetail, name='laptop_detail_view'),
    path('laptops/delete/<slug>/', LaptopsDeleteView.as_view(), name="laptopsDelete"),
    path("laptops/create", LaptopsCreateView.as_view(), name="laptopsCreate"),
    path('laptops/edit/<slug>/', LaptopsUpdateView.as_view(), name="laptopsUpdate"),
    ]