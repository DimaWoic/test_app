from rest_framework import routers
from .views import ArticleView


router = routers.SimpleRouter()
router.register('articles', ArticleView)

urlpatterns = router.urls
