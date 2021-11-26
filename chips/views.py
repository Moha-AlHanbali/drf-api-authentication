from rest_framework import generics
from .models import Chips
from .serializers import ChipsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsUserOrReadOnly

class ChipsListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Chips.objects.all()
    serializer_class = ChipsSerializer


class ChipsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsUserOrReadOnly, IsAuthenticatedOrReadOnly)
    queryset = Chips.objects.all()
    serializer_class = ChipsSerializer
