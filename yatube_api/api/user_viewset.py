from rest_framework import mixins
from rest_framework import viewsets


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    Вьюсет, который дает возможность обрабатывать Get и Post запросы`.
    """
    pass
