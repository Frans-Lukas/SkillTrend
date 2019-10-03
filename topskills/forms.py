import datetime

from django import forms
from bootstrap_datepicker_plus import DatePickerInput

class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    start = forms.DateField(widget=DateInput, initial=datetime.date.today)
    end = forms.DateField(widget=DateInput, initial=datetime.date.today)