from django.urls import path
from .views import HomeView, PartnerWith, add_partner, confirm_partnership, contact_us


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('partner_with/', add_partner, name='partner_with'),
    path('partnership/confirmed/', confirm_partnership, name='partner_confirm'),
    path('contact_us/', contact_us, name='contact_us'),
]

