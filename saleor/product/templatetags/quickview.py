import logging
import datetime
import json

from django import template

from ...core.utils import serialize_decimal
from ..utils import (
    collections_visible_to_user, get_product_images, get_product_list_context,
    handle_cart_form, products_for_cart, products_with_details)
from ..utils.attributes import get_product_attributes_data
from ..utils.availability import get_availability
from ..utils.variants_picker import get_variant_picker_data


logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag('product/_quickview.html', takes_context=True)
def product_details(context, product):
#    request = context['request']
    today = datetime.date.today()
    is_visible = (
        product.available_on is None or product.available_on <= today)
#    availability = get_availability(
#        product, discounts=request.discounts, taxes=request.taxes,
#        local_currency=request.currency)
    product_images = get_product_images(product)
#    variant_picker_data = get_variant_picker_data(
#        product, request.discounts, request.taxes, request.currency)
    product_attributes = get_product_attributes_data(product)
    # show_variant_picker determines if variant picker is used or select input
    show_variant_picker = all([v.attributes for v in product.variants.all()])
    ctx = {
        'is_visible': is_visible,
#        'form': form,
#        'availability': availability,
        'product': product,
        'product_attributes': product_attributes,
        'product_images': product_images,
        'show_variant_picker': show_variant_picker,
#        'variant_picker_data': json.dumps(
#            variant_picker_data, default=serialize_decimal)}
        }
    return ctx
