from django.db import models
from django.conf import settings
# from mptt.models import MPTTModel, TreeForeignKey

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

class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses/')
    description = models.TextField(max_length=2500, null=True)
    summary = models.TextField(max_length=140, null=True, blank=False)
    rating = models.FloatField(default=0)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', models.SET_NULL, null=True)    
    author = models.CharField(max_length=100)
        
    def count_popular_vote(self, like_boolean):
        return self.popular_vote_set.filter(like=like_boolean).count()

    def count_dislikes(self):
        return self.count_popular_vote(False)

    def count_likes(self):
        return self.count_popular_vote(True)

    def get_absolute_url(self):
        return "/course/%i/" % self.id

    def get_approval_rate(self):
        sum = self.count_likes() + self.count_dislikes()
        return self.count_likes()/sum*100 if sum > 0 else 0

    def get_price_with_discount(self, discount):
        # discount is on the format (10)%, (xx)%
        return self.price * (1-(discount/100))

# Adicionar modelo para os cursos
# Create your models here.
