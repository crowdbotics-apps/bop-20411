from rest_framework import authentication
from event.models import (
    Category,
    Faq,
    Favorites,
    Location,
    MySchedule,
    Presenter,
    Schedule,
    Sponsor,
    Vendor,
    VendorDetail,
)
from .serializers import (
    CategorySerializer,
    FaqSerializer,
    FavoritesSerializer,
    LocationSerializer,
    MyScheduleSerializer,
    PresenterSerializer,
    ScheduleSerializer,
    SponsorSerializer,
    VendorSerializer,
    VendorDetailSerializer,
)
from rest_framework import viewsets


class MyScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = MyScheduleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = MySchedule.objects.all()


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Schedule.objects.all()


class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Faq.objects.all()


class SponsorViewSet(viewsets.ModelViewSet):
    serializer_class = SponsorSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Sponsor.objects.all()


class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Vendor.objects.all()


class PresenterViewSet(viewsets.ModelViewSet):
    serializer_class = PresenterSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Presenter.objects.all()


class FavoritesViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Favorites.objects.all()


class VendorDetailViewSet(viewsets.ModelViewSet):
    serializer_class = VendorDetailSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = VendorDetail.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Location.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Category.objects.all()
