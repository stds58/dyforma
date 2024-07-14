from apptest.views import HeadView, PositionView, HeadList, PositionList  #, manage_children
from django.urls import path


urlpatterns = [
    path('head/', HeadList.as_view(), name= 'head_list'),
    path('head/create/', HeadView.as_view(), name='head_create'),
    path('position/', PositionList.as_view(), name= 'position_list'),
    path('position/create/', PositionView.as_view(), name='position_create'),
    #path('manage_children/create/', manage_children, name='manage_children_create'),
]
