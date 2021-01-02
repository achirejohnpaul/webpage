from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import SiteInfor, Partnership
from .forms import PartnerWithForm, ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    site_info = SiteInfor.objects.all()
    context = {'site_info': site_info}
    return render(request, 'home_page.html', context)


class HomeView(ListView):
    model = SiteInfor
    template_name = 'home_page.html'

    def get_context_data(self, *args, **kwargs):
        partner_data = Partnership.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['partner_data'] = partner_data
        return context


class PartnerWith(CreateView):
    model = Partnership
    form_class = PartnerWithForm
    template_name = 'add_partner.html'


def contact_us(request):
    contact_form = ContactForm()
    context = {'contact_form': contact_form}
    return render(request, 'contact_page.html', context)


def add_partner(request):
    """add new partner"""
    if request.method != 'POST':
        partner_form = PartnerWithForm()
    else:
        partner_form = PartnerWithForm(data=request.POST)
        if partner_form.is_valid():
            partner_form.save()
            return HttpResponseRedirect(reverse('partner_confirm'))

    context = {'partner_form': partner_form}
    return render(request, 'add_partner.html', context)


def confirm_partnership(request):
    return render(request, 'partner_confirm.html', {})

