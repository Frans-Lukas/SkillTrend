from datetime import timedelta, datetime

from django.db.models import Count
from django.db.models.functions import Coalesce
from django.shortcuts import render

# Create your views here.
from topskills.forms import DateForm
from topskills.models import Keyword, Job


def index(request):
    start_date = datetime.today()
    end_date = datetime.today()

    form = DateForm(request.GET)
    if form.is_valid():
        start_date = form.cleaned_data['start']
        end_date = form.cleaned_data['end']

    day_before_start = start_date - timedelta(days=1)
    day_after_end = end_date + timedelta(days=1)
    keywordsCount = Job.objects.raw('SELECT keyword, keyword AS id, count(keyword)'
                                    ' FROM topskills_job'
                                    ' INNER JOIN topskills_keyword'
                                    ' ON topskills_job .id = topskills_keyword.job_hash_id'
                                    ' WHERE date_found'
                                    ' BETWEEN \'' + day_before_start.strftime("%Y-%m-%d") + '\''
                                    ' AND \'' + day_after_end.strftime("%Y-%m-%d") + '\''
                                    'GROUP BY keyword;')
    context = {
        'keywordsCount': keywordsCount,
        'date_form': form,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'topskills/index.html', context)