from django.db import models

# Create your models here.

class Before_and_afters(models.Model):
    project_name = models.CharField(max_length=100)
    is_there_before_photos = models.BooleanField(default=True)
    before_photo = models.ImageField(upload_to='before_and_afters/', blank=True,)
    before_description = models.CharField(max_length=300, null=True, blank=True,)
    after_photo = models.ImageField(upload_to='before_and_afters/')
    after_description = models.CharField(max_length=300)
    date = models.DateField()
    review_for_Project = models.OneToOneField('Review', unique=True, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name


ratings = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

class Review(models.Model):
    rating = models.CharField(choices=ratings, max_length=1)
    customer_name = models.CharField(max_length=100)
    review = models.TextField()
    project = models.OneToOneField(Before_and_afters, unique=True, on_delete=models.CASCADE,  blank=True, null=True)

    def __str__(self):
        return self.customer_name

work_categories = (
    ('Roofing','Roofing'),
    ('Brickwork', 'Brickwork'),
    ('Driveway', 'Driveway'),
    ('Patio', 'Patio'),
    ('Turfing', 'Turfing'),
    ('Facias and Soffits', 'Facias & Soffits '),
    ('Guttering', 'Guttering'),
    ('Flat Roofing', 'Flat Roofing'),
    ('Plastering', 'Plastering'),
    ('Painting', 'Painting'),
    ('Rendering', 'Rendering'),
    ('Pebble Dashing', 'Pebble Dashing'),
    ('Fencing', 'Fencing'),
    ('Extensions', 'Extensions')
)



class Enquirie(models.Model):
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    customer_phone_number = models.CharField(max_length=11)
    job_category = models.CharField(choices=work_categories, max_length=14)
    job_explanation = models.CharField(max_length=5000)
    enquiry_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.customer_first_name + ' ' + self.customer_last_name + ' ' + self.job_category + ' ' + str(self.enquiry_date)
