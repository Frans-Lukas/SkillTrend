import datetime

from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    start = forms.DateField(widget=DateInput, initial=datetime.date.today)
    end = forms.DateField(widget=DateInput, initial=datetime.date.today)
    num_per_page = forms.IntegerField(initial=10)