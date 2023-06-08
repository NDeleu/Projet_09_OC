from django import template

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.simple_tag(takes_context=True)
def user_pronoun_choice(context, user):
    if user == context['user']:
        return 'vous'
    return user.username
