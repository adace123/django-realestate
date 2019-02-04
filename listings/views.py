from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.template.defaulttags import register
from datetime import timedelta, datetime, timezone
from .models import Listing, ListingPhoto
from .models import STATES


@register.filter
def format_currency(value):
    return "${:,.0f}".format(value)

@register.filter
def to_int(value):
    return int(value)

@register.filter
def time_diff(value):
    delta = timedelta(seconds=(datetime.now(timezone.utc) - value).seconds)
    return f"{int(delta.days / 7)} weeks, {delta.days} days"


class ListingIndexView(ListView):
    model = Listing
    template_name = 'listings/index.jinja'
    paginate_by = 10
    context_object_name = 'listings'

    def get_queryset(self):
        return Listing.objects.order_by('-list_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['states'] = [state[1] for state in STATES]
        return context

class ListingDetailsView(DetailView):
    model = Listing
    template_name = 'listings/details.jinja'
    context_object_name = 'listing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_photo'] = self.object.main_photo
        return context
