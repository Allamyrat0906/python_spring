from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.
from django.urls import reverse

months={
    "january": "eat more",
    "september": "learn more",
    "june": "swimm more",
    "april": "drink more",
    "may": "run more",
}

def index(request):
    return HttpResponse('KEEP SOME DATA')

# def test1(request):
#     return HttpResponse('this is test 1 again')

# def month_string(request,month):
#     # get_month_key= list(months.keys())
#     challenge_text =None
#     if month == "january":
#         challenge_text = "  this month january"
#     elif month == "june":
#         challenge_text= "this month may or june"
#     else:
#         return HttpResponseNotFound('Invalid month')
#     return HttpResponse(challenge_text)


def  month_string(request,month):
    challenges_text=None
    try:
        convert_to_lower=month.lower()
        challenges_text=months[convert_to_lower]
        return HttpResponse(challenges_text)
    except:
        return HttpResponseNotFound('Invalid month')
     
    
# def month_number(request,month):
#     convert_to_list=list(months.keys())

#     if month > len(convert_to_list):
#         return HttpResponseNotFound('This month invlid index ')
#     #print(convert_to_list)  # analyzes
#     challenges_text=convert_to_list[month-1]
#     get_dict=months[challenges_text]  
#     #print(get_dict)
#     return HttpResponse(get_dict)
 

 # REVERCE ABD REDIRECT COMMAND
def month_number_reverse(request,month_re):
    monts_l=list(months.keys())

    if month_re>len(monts_l):
        return HttpResponseNotFound('Invalid month')
    
    redirect_month=monts_l[month_re-1]
    redirect_path=reverse("months_challenges",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)