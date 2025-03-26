from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial UPdate
    delete -> destroy 
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default


class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View 
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default

    
    def get_queryset(self):
        queryset = Product.objects.all()
        query = self.request.GET.get("q")  # Get search query from URL params
        if query:
            queryset = Product.objects.search(query)  # Apply your custom search method
        return queryset


# product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
# product_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})