from django.shortcuts import render
from .models import Before_and_afters, Review, Enquirie
from .forms import Enquiry_Form, Review_Form
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


def home(request):
    form = Enquiry_Form()
    context = {
        'form' : form
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def past_projects(request):
    context = {
        'job' : Before_and_afters.objects.all()
    }
    return render(request, 'core/past_projects.html', context)


def reviews(request):
    context = {
        'reviews' : Review.objects.all()
    }
    return render(request, 'core/reviews.html', context)

class submit_review(View):

    def get(self, *args, **kwargs):
        form = Review_Form()
        context = {
            'form' : form
        }
        return render(self.request, 'core/make_review.html', context)

    def post(self, *args, **kwargs):
        form = Review_Form(self.request.POST or None)
        if form.is_valid():
            rating = form.cleaned_data.get('rating')
            customer_name = form.cleaned_data.get('customer_name')
            tex_review = form.cleaned_data.get('review')
            project = form.cleaned_data.get('project')
            before = Before_and_afters.objects.get(project_name=project)
            new_ting = Review(rating=rating,
                              customer_name=customer_name,
                              review=tex_review,
                              project=before)
            new_ting.save()
            before.review_for_Project = new_ting
            before.save()
            return redirect('reviews')
        else:
            messages.info(self.request, "Please fill out the form")
            return redirect('submit-a-review')

class make_an_enquiry(View):

    def get(self, *args, **kwargs):
        form = Enquiry_Form()
        context = {
            'form' : form
        }
        return render(self.request, 'core/enquiry.html', context)

    def post(self, *args, **kwargs):
        form = Enquiry_Form(self.request.POST or None)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone = form.cleaned_data.get('phone')
            issue_category = form.cleaned_data.get('issue_category')
            issue = form.cleaned_data.get('issue')
            enquiry = Enquirie(
                customer_first_name=first_name,
                customer_last_name=last_name,
                customer_phone_number=phone,
                job_category=issue_category,
                job_explanation=issue
            )
            enquiry.save()
            messages.warning(self.request, "Thank you for the enquiry we will get back to you as soon as we can!")
            return redirect('home')
        else:
            messages.warning(self.request, "Please fill out the enquiry form.")
            return redirect('enquiry')



def gravesend(request):
    return render(request, 'core/gravesend.html')

