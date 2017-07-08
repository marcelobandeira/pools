# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Sum

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=500)
	closed = models.BooleanField(default=False)
	pub_date = models.DateField(auto_now_add=True)

class Choice(models.Model):
	question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE, related_name='choices')
	choice_text = models.CharField(max_length=500)
	votes = models.IntegerField(default=0)

	@property
	def percent_prop(self):

		total_votes = self.question.choices.aggregate(soma = Sum('votes'))
		
		percent = float(self.votes) / total_votes['soma'] * 100

		return percent