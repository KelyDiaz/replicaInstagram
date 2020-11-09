from django.urls import path

from posts import views

# from appInstagram.views import

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Aplicación de instagram",
#         default_version='v1',
#         description="Esta es una imitación de instagram"
#     ),
#     public=True,
#
# )
urlpatterns = [
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0))
    path('posts/', views.list_posts),
]
