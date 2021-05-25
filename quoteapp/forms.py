from django.forms import *
from django.forms.models import modelform_factory
from .models import *


class CusotmerForm(ModelForm):
    """ ModelForm for Customer """

    class Meta:
        """Config for Customer"""
        model = Customer
        fields = ('name', 'email', 'mobile_number')
        # fields and widgets
        widgets = {
            'name': TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Enter your Name',
                                     'autocomplete': 'off',
                                     'pattern': '[A-Za-z ]+',
                                     'title': 'Enter Characters Only '}),
            'email': EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Enter your Email'}),
            'mobile_number': TextInput(attrs={'class': 'form-control',
                                              'placeholder': '60121234567',
                                              'autocomplete': 'off',
                                              'pattern': '[0-9]{11}',
                                              'title': 'Enter 11 digit number only. '}),
        }
        

class VehicleForm(ModelForm):
    """ ModelForm for Customer """

    class Meta:
        """Config for Vehicle"""
        model = Vehicle
        fields = ('year', 'model', 'make', 'number', 'price')
        # fields and widgets
        widgets = {
            'year': Select(attrs={'class': 'form-control'}),
            'model': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter Vehicle Model',
                                      'autocomplete': 'off',
                                      'pattern': '[A-Za-z 0-9]+',
                                      'title': 'Enter Characters Only '}),
            'make': TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Enter Vehicle Make',
                                     'autocomplete': 'off',
                                     'pattern': '[A-Za-z ]+',
                                     'title': 'Enter Characters Only '}),
            'number': TextInput(attrs={'class': 'form-control',
                                       'placeholder': 'Enter Vehicle Number',
                                       'autocomplete': 'off', }),
            'price': NumberInput(attrs={'class': 'form-control',
                                        'placeholder': 'Enter Vehicle Price',
                                        'autocomplete': 'off'}),
        }


class CoverageSelectedForm(ModelForm):
    """ ModelForm for Customer """
    the_coverages = ModelMultipleChoiceField(queryset=CoverageInfo.objects.all(),
                                             required=True,
                                             widget=CheckboxSelectMultiple)

    class Meta:
        """Config for CoverageInfo"""
        model = CoverageInfo
        fields = ('name', 'value')
        exclude = ['name', 'value']
       

class LoginForm(ModelForm):
    """ ModelForm for Login """

    class Meta:
        """Config for Login form"""
        model = Customer
        fields = ('email',)
        exclude = ('name', 'mobile_number',)
        # fields and widgets
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Enter your Email'}),
        }
