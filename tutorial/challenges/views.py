from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "This is the January challenge.",
    "february": "This is the February challenge.",
    "march": "This is the March challenge.",
    "april": "This is the April challenge.",
    "may": "This is the May challenge.",
    "june": "This is the June challenge.",
    "july": "This is the July challenge.",
    "august": "This is the August challenge.",
    "september": "This is the September challenge.",
    "october": "This is the October challenge.",
    "november": "This is the November challenge.",
    # "december": "This is the December challenge.",
    "december": None,
}
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{"all_months":months})
    
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
            # challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",
                    {"text": monthly_challenges[month],
                    "month_name": month})
    except:
        response_data = render_to_string("404.html")
        raise Http404(response_data)
        # return HttpResponseNotFound(response_data)