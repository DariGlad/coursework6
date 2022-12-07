from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Ad, Comment
from ads.permissions import IsOwner, IsAdmin
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    default_serializer = AdDetailSerializer
    serializer_classes = {
        "list": AdSerializer
    }

    default_permission = [IsAuthenticated(), IsOwner() or IsAdmin()]
    permissions = {
        "retrieve": [IsAuthenticated()],
        "list": [AllowAny()]
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    @action(detail=False, methods=["get"])
    def me(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    default_permission = [IsAuthenticated()]
    permissions = {
        "update": [IsAuthenticated(), IsOwner() or IsAdmin()],
        "partial_update": [IsAuthenticated(), IsOwner() or IsAdmin()],
        "create": [IsAuthenticated(), IsOwner() or IsAdmin()],
        "destroy": [IsAuthenticated(), IsOwner() or IsAdmin()]
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        return ad_instance.comments.all()
