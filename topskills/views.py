from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from topskills.models import Keyword


def index(request):
    # group by keyword and count occurrence
    # SELECT keyword, COUNT(keyword) AS total FROM topskills_keyword GROUP BY keyword;
    keywordsCount = Keyword.objects.values("keyword").annotate(total=Count('keyword'))
    context = {
        'keywordsCount': keywordsCount
    }
    return render(request, 'topskills/index.html', context)