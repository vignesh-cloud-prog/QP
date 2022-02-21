from django.urls import path
from .views import *

urlpatterns = [

    path('create_eduation_type', create_eduation_type),
    path('create_governing_body', create_governing_body),
    # path('post/ajax/friend', postFriend, name = "post_friend"),
    
]