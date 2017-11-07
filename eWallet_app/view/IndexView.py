from django.shortcuts import render, get_object_or_404
from eWallet_app.models import UserGroup
from eWallet_app.models import GroupChange
from eWallet_app.models import ChangeDetail
from django.http import HttpResponse
from django.http import Http404

def index(request):
    changes = ChangeDetail.objects.all()
    context = {'all_changes': changes}
    return render(request, "index.html", context)

def detail(request, change_detail_id):
    change = get_object_or_404(ChangeDetail, pk=change_detail_id)
    return render(request, "detail.html", {'change': change})


