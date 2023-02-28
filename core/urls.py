from django.urls import path, include
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularRedocView,
    SpectacularAPIView,
)

from core import api

router = SimpleRouter()
router.register("todo-lists", api.views.ToDoListViewSet, "todo-lists")
router.register("todos", api.views.ToDoItemViewSet, "todos")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-docs/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api-docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api-docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
