from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):
    add_time = DateFilter(widjet=forms.DateInput(attrs={'type': 'date'}),
                          label='Дата',
                          lookup_expr='date__gte')

    class Meta:
        model = Post
        fields = {
            'text': ['icontains', ],
        }