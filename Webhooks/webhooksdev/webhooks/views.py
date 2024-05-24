from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import JobDelivered
import json

@csrf_exempt
def webhook_job_delivered(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            job = data.get("job")
            driver = data.get("driver")
            delivered_at = data.get("deliverAt")
            # commit to database - datetime is auto assigned for all models
            job_delivered = JobDelivered.objects.create(job=job,driver=driver,delivered_at=delivered_at)
            return JsonResponse({'status':'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status':'error','message':'Invalid JSON payload'})
    else:
        return JsonResponse({'status':'error','message':'Only POST requests are allowed'})
