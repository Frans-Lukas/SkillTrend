from django import forms
from bootstrap_datepicker_plus import DatePickerInput

class DateInput(forms.DateInput):
    input_type = 'date'