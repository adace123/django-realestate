from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.forms import ModelForm
import json
from .models import Contact  
from listings.models import Listing  

# Create your views here.
class CreateContactView(View):
    model = Contact
    http_method_names = ['post']
    fields = ['name', 'email', 'listing', 'message']
    
    def post(self, request, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        missing_fields = [k for k in body if not body[k]]
        if missing_fields:
            return HttpResponse(json.dumps({'missing': ', '.join(missing_fields)}), status=400)
        listing = get_object_or_404(Listing, pk=int(body['listing']))
        contact = Contact.objects.create(listing=listing, name=body['name'], realtor=listing.realtor, email=body['email'], message=body['message'])
        contact.save()
        return HttpResponse(json.dumps({}), status=200)
