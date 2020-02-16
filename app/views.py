from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
import subprocess
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def run_code(code):
    try:
        value = code.strip().split(' ')
        if len(value)&1:
            return '输入公式有误'
        value = [value[i:i+2]for i in range(0,len(value),2)]
        length = len(value)
        sum = 0
        for iterm in value:
            sum+=0.0009*(int(iterm[0])*int(iterm[1]))
            # output = subprocess.check_output(['python','-c',code],universal_newlines=True,stderr=subprocess.STDOUT,timeout=30)
        output=str(length)+"组,结果:"+str(sum)
    except :
        output = '公式输入有误'
    return output
 
 
@csrf_exempt
@require_POST
def compute(request):
    code = request.POST.get('code')
    result = run_code(code)
    return JsonResponse(data={'result':result})
def home(request):
    return render(
            request,
            'index.html',
            )

# Create your views here.
