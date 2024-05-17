from django.shortcuts import render,HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context

class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorite_review'] = self.request.session.get('favorite_review')
        context["is_favorite"] = str(self.object.id) == context["favorite_review"]
        return context

    # context_object_name = 'review'

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        # review = Review.objects.get(pk=review_id)
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)