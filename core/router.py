from api.router import router
from core.views import LoginViewSet, RefreshViewSet

router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')


