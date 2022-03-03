import imp
import re
from django.shortcuts import render
import requests


url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'
req_result = requests.get(url)
print(req_result)

# Create your views here.

def lotto(request):
    context = {

    }
    return render(request, 'lotto.html', context)
