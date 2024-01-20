# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Subject(models.Model):

    #__Subject_FIELDS__
    subject name = models.CharField(max_length=255, null=True, blank=True)

    #__Subject_FIELDS__END

    class Meta:
        verbose_name        = _("Subject")
        verbose_name_plural = _("Subject")


class Exam(models.Model):

    #__Exam_FIELDS__
    exam name = models.CharField(max_length=255, null=True, blank=True)

    #__Exam_FIELDS__END

    class Meta:
        verbose_name        = _("Exam")
        verbose_name_plural = _("Exam")


class Topic(models.Model):

    #__Topic_FIELDS__
    topic name = models.CharField(max_length=255, null=True, blank=True)

    #__Topic_FIELDS__END

    class Meta:
        verbose_name        = _("Topic")
        verbose_name_plural = _("Topic")


class Flashcard Deck(models.Model):

    #__Flashcard Deck_FIELDS__

    #__Flashcard Deck_FIELDS__END

    class Meta:
        verbose_name        = _("Flashcard Deck")
        verbose_name_plural = _("Flashcard Deck")


class Flashcard(models.Model):

    #__Flashcard_FIELDS__
    question = models.CharField(max_length=255, null=True, blank=True)
    answer = models.CharField(max_length=255, null=True, blank=True)

    #__Flashcard_FIELDS__END

    class Meta:
        verbose_name        = _("Flashcard")
        verbose_name_plural = _("Flashcard")


class Quiz(models.Model):

    #__Quiz_FIELDS__

    #__Quiz_FIELDS__END

    class Meta:
        verbose_name        = _("Quiz")
        verbose_name_plural = _("Quiz")


class Quiz Question(models.Model):

    #__Quiz Question_FIELDS__
    quiz question = models.CharField(max_length=255, null=True, blank=True)
    quiz answer a = models.CharField(max_length=255, null=True, blank=True)
    quiz answer b = models.CharField(max_length=255, null=True, blank=True)
    quiz answer c = models.CharField(max_length=255, null=True, blank=True)
    quiz answer d = models.CharField(max_length=255, null=True, blank=True)
    quiz correct answer = models.CharField(max_length=255, null=True, blank=True)

    #__Quiz Question_FIELDS__END

    class Meta:
        verbose_name        = _("Quiz Question")
        verbose_name_plural = _("Quiz Question")



#__MODELS__END
