from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from itertools import chain
from django.db.models import Q

from . import forms, models


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    tickets_sorted = sorted(
        chain(tickets),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    paginator = Paginator(tickets_sorted, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'rthome/home.html', context=context)


@login_required
def post_edit(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    tickets_sorted = sorted(
        chain(tickets),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    paginator = Paginator(tickets_sorted, 3)
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
