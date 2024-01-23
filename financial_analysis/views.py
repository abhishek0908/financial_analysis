# financial_analysis_app/views.py
from django.shortcuts import render
from .models import FinancialAnalysisResult, probe_model_5l_profit
import json
from django.http import HttpResponse

def index(request):
    return HttpResponse("Test view")

def submit(request):
    print("AbhisheK uDIYA")
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        data = json.load(file)

        # Using probe_model_5l_profit instead of get_financial_analysis_result
        flags = probe_model_5l_profit(data['data'])
        # Save the result to the database
        financial_analysis_result = FinancialAnalysisResult.objects.create(
            total_revenue_5cr_flag=flags['TOTAL_REVENUE_5CR_FLAG'],
            borrowing_to_revenue_flag=flags['BORROWING_TO_REVENUE_FLAG'],
            iscr_flag=flags['ISCR_FLAG'],
        )
        print("Hello wOELS" ,financial_analysis_result)

        return render(request, 'results.html', {'result': financial_analysis_result})

    return render(request, 'index.html')
