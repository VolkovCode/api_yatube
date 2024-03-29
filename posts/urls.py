from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('v1/posts', PostViewSet, basename="posts")
router.register(r"v1/posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments")


urlpatterns = [
    path('', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]
