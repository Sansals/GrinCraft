from django.shortcuts import render

def ShowRulesPage(request):
    return render(request, 'rules/rules_page.html')
