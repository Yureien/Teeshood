from django.utils.translation import npgettext
from django_filters import FilterSet, CharFilter
from ..site.models import Career


class SortedFilterSet(FilterSet):
    """Base class for filter sets used in dashboard views.

    Adds flag `is_bound_unsorted` to indicate if filter set has data from
    filters other than `sort_by` or `page`.
    """

    def __init__(self, data, *args, **kwargs):
        self.is_bound_unsorted = self.set_is_bound_unsorted(data)
        super(SortedFilterSet, self).__init__(data, *args, **kwargs)

    def set_is_bound_unsorted(self, data):
        return any([key not in {'sort_by', 'page'} for key in data.keys()])

    def get_summary_message(self):
        """Return message displayed in dashboard filter cards.

        Inherited by subclasses for record specific naming.
        """
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard list',
            'Found %(counter)d matching record',
            'Found %(counter)d matching records',
            number=counter) % {'counter': counter}


class CareerFilter(FilterSet):
    search = CharFilter(method='career_custom_filter')

    class Meta:
        model = Career
        fields = ['search']

    def career_custom_filter(self, queryset, name, value):
        return (queryset.filter(title__icontains=value) |
                queryset.filter(experience__icontains=value) |
                queryset.filter(location__icontains=value) |
                queryset.filter(categories__icontains=value))
