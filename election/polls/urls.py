from django.urls import path
from rest_framework.routers import DefaultRouter

# from .views import polls_list, polls_detail
from .apiviews import ChoiceList, VoteCreate, PollViewSet, VoteList, UserCreate, LoginView

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    # path('', PollList.as_view(), name="polls_list"),
    # path('<int:pk>/', PollDetail.as_view(), name="polls_detail"),
    path('<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('<int:pk>/choices/<int:choice_pk>/vote/', VoteCreate.as_view(), name='create_vote'),
    path('votes/', VoteList.as_view(), name='vote_list'),
    path('user_create/', UserCreate.as_view(), name="user_create"),
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += router.urls