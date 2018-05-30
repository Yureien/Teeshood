from ...menu import models


def resolve_menus(info):
    return models.Menu.objects.all().distinct()
