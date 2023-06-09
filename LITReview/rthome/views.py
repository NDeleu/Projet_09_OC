from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.db.models import Q

from . import forms, models


@login_required
def home(request):
    main_user = forms.User.objects.get(username=request.user.username)
    tickets = models.Ticket.objects.filter(
        Q(user__in=main_user.follows.all()) | Q(user=main_user)
    )
    reviews = models.Review.objects.filter(
        Q(user__in=main_user.follows.all()) |
        Q(user=main_user) |
        Q(ticket__user=main_user)
    )

    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    context = {'tickets_and_reviews': tickets_and_reviews}
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

    context = {'tickets_and_reviews': tickets_and_reviews}
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
        request, 'rthome/edit_review.html',
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


@login_required
def follow_users(request):
    form = forms.FollowUsersForm()
    main_user = forms.User.objects.get(username=request.user.username)
    following_all = main_user.following.all()
    followed_by_all = main_user.followed_by.all()

    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST)
        if form.is_valid():
            user_pre_add = form.cleaned_data['follows']

            if user_pre_add == request.user.username:
                return redirect('error_self_follow')
            else:

                user_add = forms.User.objects.get(username=user_pre_add)
                main_user.follows.add(
                    user_add,
                    through_defaults={
                        'user_name': request.user.username,
                        'followed_user_name': user_add.username
                    })

                return redirect('follow_users')

    context = {
        'form': form,
        'following_all': following_all,
        'followed_by_all': followed_by_all,
    }

    return render(
        request, 'rthome/follow_users_form.html', context=context)


@login_required
def error_self_follow(request):
    return render(request, 'rthome/error_self_follow.html')


@login_required
def delete_follow(request, following_id):
    main_user = forms.User.objects.get(username=request.user.username)
    following = get_object_or_404(main_user.following.all(), id=following_id)

    if request.method == 'POST':
        following.delete()
        return redirect('follow_users')

    return render(
        request,
        'rthome/delete_follow.html',
        context={'following': following})
