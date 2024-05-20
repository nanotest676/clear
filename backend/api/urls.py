from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, TagViewSet, IngredientViewSet, RecipeViewSet, SelfUserView, SetPasswordView

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'recipes', RecipeViewSet, basename='recipe')

urlpatterns = [
    path('', include(router.urls)),
    path('self/', SelfUserView.as_view(), name='self-user'),
    path('set-password/', SetPasswordView.as_view(), name='set-password'),
]
