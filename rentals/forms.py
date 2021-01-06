from  django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):

    class Meta:
      model = Listing
      fields = ('address', 'city', 'estate', 'description', 'rent', 'bedrooms', 'garage', 'photo_main',
                'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'is_published','list_date')
