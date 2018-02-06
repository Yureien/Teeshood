from django.utils.translation import pgettext_lazy


class ProductBulkAction:
    """Represents types of product bulk actions handled in dashboard."""

    PUBLISH = 'Publish'
    UNPUBLISH = 'Unpublish'
    ADD_TO_COLLECTION = 'Add to collection'

    CHOICES = [
        (PUBLISH, pgettext_lazy('product bulk action', 'Publish')),
        (UNPUBLISH, pgettext_lazy('product bulk action', 'Unpublish')),
        (ADD_TO_COLLECTION, pgettext_lazy(
            'product bulk action', 'Add to collection'))]
