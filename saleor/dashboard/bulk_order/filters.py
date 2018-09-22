from django.utils.translation import npgettext, pgettext_lazy
from django_filters import CharFilter

from ...core.filters import SortedFilterSet
from ...core.models import BulkOrder


PRODUCT_SORT_BY_FIELDS = {
    'name': pgettext_lazy('Product list sorting option', 'name'),
}


class ProductFilter(SortedFilterSet):
    name = CharFilter(
        label=pgettext_lazy('Product list filter label', 'Name'),
        lookup_expr='icontains')

    class Meta:
        model = BulkOrder
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard products list',
            'Found %(counter)d matching product',
            'Found %(counter)d matching products',
            number=counter) % {'counter': counter}
