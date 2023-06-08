from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from itertools import chain
from django.db.models import Q

from . import forms, models


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()

    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    paginator = Paginator(tickets_and_reviews, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'rthome/home.html', context=context)


@login_required
def post_edit(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)

    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    paginator = Paginator(tickets_and_reviews, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'rthome/post_edit.html', context=context)


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'rthome/create_ticket.html', context={'form': form})


@login_required
def create_review(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    form = forms.ReviewForm()
    if ticket:
        review_compared = models.Review.objects.filter(
            Q(ticket__id=str(ticket.id)) & Q(user__id=str(request.user.id)))
        if review_compared:
            return redirect('error_review', ticket.id)
        else:

            if request.method == 'POST':
                form = forms.ReviewForm(request.POST)
                if form.is_valid():
                    review = form.save(commit=False)
                    review.user = request.user
                    review.ticket = ticket
                    review.save()
                    return redirect('home')
    return render(
        request, 'rthome/create_review.html',
        context={'ticket': ticket, 'form': form})


@login_required
def error_review(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(
        request, 'rthome/error_review.html', context={'ticket': ticket})


@login_required
def create_ticket_and_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'rthome/create_ticket_review.html', context=context)


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    form = forms.TicketForm(instance=ticket)
    if ticket:
        if ticket.user != request.user:
            return redirect('error_change_ticket', ticket.id)
        else:
            if request.method == 'POST':
                form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
                if form.is_valid():
                    ticket_save = form.save(commit=False)
                    ticket_save.user = request.user
                    ticket_save.save()
                    return redirect('post_edit')
    return render(
        request, 'rthome/edit_ticket.html',
        context={'ticket': ticket, 'form': form})


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)

    if ticket:
        if ticket.user != request.user:
            return redirect('error_change_ticket', ticket.id)
        else:

            if request.method == 'POST':
                ticket.delete()
                return redirect('post_edit')

    return render(
        request, 'rthome/delete_ticket.html', context={'ticket': ticket})


@login_required
def error_change_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(
        request, 'rthome/error_change_ticket.html',
        context={'ticket': ticket})


@login_required
def edit_review(request, ticket_id, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    form = forms.ReviewForm(instance=review)
    if review:
        if review.user != request.user:
            return redirect('error_change_review', ticket.id, review.id)
        else:

            if request.method == 'POST':
                form = forms.ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    review = form.save(commit=False)
                    review.user = request.user
                    review.ticket = ticket
                    review.save()
                    return redirect('post_edit')
    return render(
        request, 'rthome/create_review.html',
        context={'ticket': ticket, 'review': review, 'form': form})


@login_required
def delete_review(request, ticket_id, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    ticket = get_object_or_404(models.Ticket, id=ticket_id)

    if review:
        if review.user != request.user:
            return redirect('error_change_review', ticket.id, review.id)
        else:

            if request.method == 'POST':
                review.delete()
                return redirect('post_edit')

    return render(
        request, 'rthome/delete_review.html',
        context={'ticket': ticket, 'review': review})


@login_required
def error_change_review(request, ticket_id, review_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review = get_object_or_404(models.Review, id=review_id)
    return render(
        request, 'rthome/error_change_ticket.html',
        context={'ticket': ticket, 'review': review})


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(
        request, 'rthome/ticket_detail.html',
        context={'ticket': ticket})


@login_required
def review_detail(request, ticket_id, review_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review = get_object_or_404(models.Review, id=review_id)
    return render(
        request, 'rthome/review_detail.html',
        context={'ticket': ticket, 'review': review})
