from django.db import models

from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Choice(models.Model):
    choice_text = models.CharField(max_length=100)

    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)