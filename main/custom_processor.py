from .models import Category, Post, ContactUs
from django.db.models import Q

def category_renderer(request):
    return {
        'all_categories': Category.objects.all(),
        'latest':  Post.objects.filter(
            status='published').order_by('date_created')[:5],
        'popular':  Post.objects.filter(
            status='published').order_by('view_count')[:7],
        'trend' : Post.objects.filter(
            Q(status='published') & Q(view_count__gte=10))[:7],
        'contactus' : ContactUs.objects.get(id=1)
    }
