from .models import Code
from .serializer import CodeSerializer
from rest_framework import filters, generics, mixins, permissions

# Create your views here.


class AllCodes(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["=icd10_code", "category", "diagnosis"]
    ordering_fields = ["icd10_code", "category", "diagnosis"]
    ordering = ["icd10_code"]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SingleCode(generics.GenericAPIView, mixins.RetrieveModelMixin):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    lookup_field = "icd10_code"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UpdateCode(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin
):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    lookup_field = "icd10_code"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteCode(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin
):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    lookup_field = "icd10_code"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
