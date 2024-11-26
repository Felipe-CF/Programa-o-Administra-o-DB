from rest_framework.routers import DefaultRouter
from backend.view.FormaPagamentoView import FormaPagamentoViewSet

forma_pagamento_router = DefaultRouter()
forma_pagamento_router.register('forma_pagamento', FormaPagamentoViewSet, basename='forma_pagamento')