from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import DecimalField
from django.db.models.fields.files import ImageField
from mptt.models import MPTTModel, TreeForeignKey

# class Comment(MPTTModel):
#     course = models.ForeignKey('Course', on_delete=models.PROTECT)
#     raw_comment = models.TextField()
#     parent = TreeForeignKey('self',
#                             related_name='children',
#                             null=True,
#                             blank=True,
#                             db_index=True,
#                             on_delete=models.PROTECT
#                             )
#     date = models.DateTimeField()
#     comment_phase = models.PositiveSmallIntegerField()
#     deleted = models.BooleanField(default=False)
#     ip = models.CharField(max_length=20, null=True)
#     edited = models.BooleanField(default=False)

#     class MPTTMeta:
#         order_insertion_by = ['-date']

#     def log_msg(self):
#         msg = "id: {0}, course: {1} - {2}, author: {3}, raw_comment: {4}, parent: {5}, date: {6}, comment_phase: {7}, deleted: {8}, ip: {9}"
#         msg = msg.format(str(self.pk), self.course.pk, self.course.title, self.author, self.raw_comment, self.parent, self.date, self.comment_phase, self.deleted, self.ip)
#         return msg

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ad(models.Model):
    course = models.ForeignKey('Course', related_name="ads", on_delete=models.CASCADE)
    ad_image = models.ImageField(upload_to='ad/img/%Y/%m/%d/')
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

    class Meta:
        ordering = ['-rating']

    def get_absolute_url(self):
        return "/course/%i/" % self.id

    def get_price_with_discount(self):
        price = float(self.price) * (1-(self.discount/100))
        return "{:.2f}".format(price).replace(".",",") 
    
    def get_rating(self):
        return int(self.rating*20)

class Evaluation(models.Model):
    course = models.ForeignKey('Course', related_name="evaluations", on_delete=models.CASCADE)
    raw_evaluation = models.TextField()
    evaluation_rating = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-evaluation_rating',)
