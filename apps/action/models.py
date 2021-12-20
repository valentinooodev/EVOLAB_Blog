from django.db import models
from apps.commons.models import BaseModel
from apps.blog.models import PostModel
from django.conf import settings


# Create your models here.

class UpvoteModel(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_upvote')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='post_upvote', null=True, blank=True)

    # def __str__(self):
    #     return f'{self.user.email} - {self.post.title}'

    class Meta:
        verbose_name_plural = 'Upvotes'
        # ordering = ('-created',)
        db_table = 'upvotes'


class CommentModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='post_comment', null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.user_id}: {self.post_id} - {self.content}'

    class Meta:
        verbose_name_plural = 'Comments'
        # ordering = ('-created',)
        db_table = 'comments'

