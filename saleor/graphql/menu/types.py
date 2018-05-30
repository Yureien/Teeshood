from graphene import relay

from ...menu import models
from ..core.types import CountableDjangoObjectType


class Menu(CountableDjangoObjectType):
    class Meta:
        description = """asd"""
        interfaces = [relay.Node]
        filter_fields = ['id', 'name']
        model = models.Menu


class MenuItem(CountableDjangoObjectType):
    class Meta:
        description = """asd"""
        interfaces = [relay.Node]
        filter_fields = ['id', 'name']
        model = models.MenuItem
