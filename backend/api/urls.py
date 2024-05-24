from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TagViewSet, IngredientViewSet, RecipeViewSet, SelfUserView, SetPasswordView, UserMe

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'recipes', RecipeViewSet, basename='recipe')

urlpatterns = [
    path('', include(router.urls)),
    path('users/me/', SelfUserView.as_view(), name='self-user'),
    path('set_password/', SetPasswordView.as_view(), name='set_password'),
    # path("users/set_password/", set_password, name="set_password"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
