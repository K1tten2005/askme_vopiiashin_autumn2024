def popular_tags(request):
    from .models import Tag
    tags = Tag.objects.get_popular()[:8]
    types = ['primary', 'secondary', 'success', 'success', 'warning', 'info', 'light', 'dark']
    tags_with_types = list(zip(tags, types))
    return {'popular_tags': tags_with_types}

def best_members(request):
    from .models import Profile
    users = Profile.objects.get_best()[:5]
    return {'best_members': users}