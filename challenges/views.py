from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
   'january': 'Eat no meat for the entire month!',
   'february': 'Walk at least 20 minutes every day!',
   'march': 'Learn Django for at least 20 minutes every day!',
   'april': 'Eat no meat for the entire month!',
   'may': 'Walk at least 20 minutes every day!',
   'june': 'Learn Django for at least 20 minutes every day!',
   'july': 'Eat no meat for the entire month!',
   'august': 'Walk at least 20 minutes every day!',
   'september': 'Learn Django for at least 20 minutes every day!',
   'october': 'Eat no meat for the entire month!',
   'november': 'Walk at least 20 minutes every day!',
   'december': 'Learn Django for at least 20 minutes every day!',
}


def index(request):
   list_items = ''
   months = list(monthly_challenges.keys())

   for month in months:
      month_path = reverse('month-challenge', args=[month])
      list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'

   response_data = f'<ul>{list_items}</ul>'
   return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
   months = list(monthly_challenges.keys())

   if month > len(months):
      return HttpResponseNotFound('Invalid month')

   redirect_month = months[month - 1]
   redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january
   return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
   try:
      challenge_text = monthly_challenges[month]
      return render(request, 'challenges/challenge.html', {
         'month': month,
         'text': challenge_text
      })
   except:
      return HttpResponseNotFound('<h1>This month is not supported!</h1>')