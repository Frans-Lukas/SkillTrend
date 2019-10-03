from django.db.models import Count
from django.db.models.functions import Coalesce
from django.shortcuts import render

# Create your views here.
from topskills.forms import DateForm
from topskills.models import Keyword


def index(request):
    # group by keyword and count occurrence
    # SELECT keyword, COUNT(keyword) AS total FROM topskills_keyword GROUP BY keyword;
    keywordsCount = Keyword.objects.values("keyword").annotate(total=Count('keyword')).order_by('-total')
    date_form = DateForm
    context = {
        'keywordsCount': keywordsCount,
        'date_form': date_form,
    }
    return render(request, 'topskills/index.html', context)

def change_date(request):
    form = DateForm(request.GET)
    if form.start.is_valid():
        start_date = form.start.cleaned_data['date']

    if form.end.is_valid():
        end_date = form.end.cleaned_data['date']
    print(end_date)