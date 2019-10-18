
from django.urls import path
from . import views
from .views import submit_review, make_an_enquiry

urlpatterns = [
    path('', views.home, name='home'),
    path('what-can-we-do', views.about, name='about'),
    path('previous-projects', views.past_projects, name='past-projects'),
    path('testimonials', views.reviews, name='reviews'),
    path('submit-a-review', submit_review.as_view(), name='submit-a-review'),
    path('gravesend-property-maintenance', views.gravesend, name='gravesend'),
    path('submit-an-enquiry',make_an_enquiry.as_view(), name='enquiry')
]