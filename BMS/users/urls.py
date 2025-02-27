from django.urls import path
from .views import (
    signup,
    logout_view,
    login_view,
    menu_list,
    create_menu,
    update_menu,
    create_order,
    get_orders,
    update_order,
    task_list, 
    task_detail,
    get_users,
    update_user,
    get_current_user
)

urlpatterns = [
        
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("users/", get_users, name="get_users"),
    path('user/<int:pk>/', update_user,name="update_user"),
    path('get_current_user/', get_current_user, name='get_current_user'),


    # --------------------------------------------------------------------

    path("create_menu/", create_menu, name="create_menu"),
    path("menus/", menu_list, name="menu_list"),
    path("menu/<int:pk>/", update_menu, name="update_menu"),
    # --------------------------------------------------------------------

    path("create_order/", create_order, name="create_order"),
    path("update_order/<int:order_id>/", update_order, name="update_order"),
    path("orders/", get_orders, name="get_orders"),

    # --------------------------------------------------------------------

    path('tasks/', task_list,name="task_list"),
    path('tasks/<int:pk>/', task_detail,name="task_detail"),
]
