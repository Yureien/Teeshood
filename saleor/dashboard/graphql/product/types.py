import graphene
from graphene import relay

from ....graphql.core.types import TaxedMoneyRange
from ....graphql.product.types import Product
from ....product import models
from ....product.utils import get_product_costs_data


class GrossMargin(graphene.ObjectType):
    start = graphene.Int()
    stop = graphene.Int()


class ProductDashboard(Product):
    purchase_cost = graphene.Field(TaxedMoneyRange)
    gross_margin = graphene.List(GrossMargin)

    class Meta:
        model = models.Product
        interfaces = [relay.Node]
        skip_registry = False

    def resolve_purchase_cost(self, info):
        purchase_cost, _ = get_product_costs_data(self)
        return purchase_cost

    def resolve_gross_margin(self, info):
        _, gross_margin = get_product_costs_data(self)
        return [GrossMargin(gross_margin[0], gross_margin[1])]

    def resolve_price_range(self, info):
        return self.get_price_range()
