from django.conf import settings
from django.db import models
from django.db.models import F, Max
from versatileimagefield.fields import VersatileImageField
from django.core.validators import RegexValidator


class BaseNote(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True,
        on_delete=models.SET_NULL)
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    content = models.TextField()
    is_public = models.BooleanField(default=True)

    class Meta:
        abstract = True


class SortableModel(models.Model):
    sort_order = models.PositiveIntegerField(editable=False, db_index=True)

    class Meta:
        abstract = True

    def get_ordering_queryset(self):
        raise NotImplementedError('Unknown ordering queryset')

    def save(self, *args, **kwargs):
        if self.sort_order is None:
            qs = self.get_ordering_queryset()
            existing_max = qs.aggregate(Max('sort_order'))
            existing_max = existing_max.get('sort_order__max')
            self.sort_order = 0 if existing_max is None else existing_max + 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        qs = self.get_ordering_queryset()
        qs.filter(sort_order__gt=self.sort_order).update(
            sort_order=F('sort_order') - 1)
        super().delete(*args, **kwargs)


class CustomDesign(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = VersatileImageField(upload_to='custom-design-uploads')

    def __str__(self):
        return self.name


class BulkOrderType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BulkOrderColor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BulkOrder(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Max 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    order_type = models.ForeignKey(BulkOrderType, on_delete=models.CASCADE)
    order_color = models.ForeignKey(BulkOrderColor, on_delete=models.CASCADE)
    number_of_pieces = models.IntegerField()
    upload_design = models.FileField(upload_to='bulk-order-upload-design', blank=True)
    list_of_names = models.FileField(upload_to='bulk-order-lon', blank=True)
    additional_description = models.TextField()
    teeshood_designs_product = models.BooleanField()

    def __str__(self):
        return self.name


class CustomerContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
