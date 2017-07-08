# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from pool.models import Question, Choice
from django.db.models import Sum
from django.shortcuts import redirect
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.db.models import F
# Create your views here.
def index(request):
	questions = Question.objects.all().order_by('-pub_date')
	return render(request,'index.html', {'questions': questions})

def question(request, question_id):
	question = Question.objects.get(id=question_id)
	return render(request, 'question.html', {'question': question})

def results(request, question_id):
	question = Question.objects.get(id=question_id)
	total_votes = question.choices.aggregate(soma = Sum('votes'))
	choices = question.choices.annotate(percent= Cast('votes', FloatField()) / total_votes['soma'] * 100)

	return render(request, 'results.html', {'question': question, 'total_votes':total_votes, 'choices':choices})

def vote(request, question_id):
	question = Question.objects.get(id=question_id)
	return render(request, 'vote.html', {'question': question})

def add_vote(request, choice_id):
	choice = Choice.objects.get(id=choice_id)
	choice.votes = choice.votes + 1
	choice.save()

	return redirect('index')

def manage(request, question_id):
	question = Question.objects.get(id=question_id)

	free_choices = Choice.objects.filter(question__isnull = True)
	return render(request, 'manage.html', {'question': question, 'free_choices': free_choices})

def close(request, question_id):
	question = Question.objects.get(id=question_id)
	if (question.closed):
		question.closed = False
	else:
		question.closed = True

	question.save()
	return redirect('index')

def remove(request, question_id, choice_id):
	choice = Choice.objects.get(id=choice_id)
	question = Question.objects.get(id=question_id)
	question.choices.remove(choice)

	return redirect('index')

def add_to_question(request, question_id, choice_id):
	choice = Choice.objects.get(id=choice_id)
	question = Question.objects.get(id=question_id)
	question.choices.add(choice)

	free_choices = Choice.objects.filter(question__isnull = True)

	return redirect('index')


