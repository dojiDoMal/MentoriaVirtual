from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ad(models.Model):
    course = models.ForeignKey('Course', related_name="ads", on_delete=models.CASCADE)
    ad_image_title = models.CharField(max_length=50)
    ad_image = models.ImageField(upload_to='ad/img/%Y/%m/%d/')
    ad_video_title = models.CharField(max_length=50)
    ad_video = models.FileField(upload_to='ad/video/%Y/%m/%d/')
    ad_text = models.TextField(max_length=2500, null=True)

class Course(models.Model):
    # transformar o desconto em um field?
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses/')
    description = models.TextField(max_length=2500, null=True)
    summary = models.TextField(max_length=140, null=True, blank=False)
    rating = models.FloatField(default=0)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=100)
    link = models.URLField(max_length=200, default='#')
    discount = models.IntegerField(default=0)
    pain_point = models.TextField(max_length=500, null=True)

    class Meta:
        ordering = ['-rating']

    def get_absolute_url(self):
        return "/course/%i/" % self.id

    def get_price_with_discount(self):
        price = float(self.price) * (1-(self.discount/100))
        return "{:.2f}".format(price).replace(".",",") 
    
    def get_saving(self):
        new_price = float(self.price) * (1-(self.discount/100))
        return "{:.2f}".format(float(self.price) - new_price).replace(".", ",") 

    def get_rating(self):
        return int(self.rating*20)

class Evaluation(models.Model):
    course = models.ForeignKey('Course', related_name="evaluations", on_delete=models.CASCADE)
    raw_evaluation = models.TextField()
    evaluation_rating = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-evaluation_rating',)
