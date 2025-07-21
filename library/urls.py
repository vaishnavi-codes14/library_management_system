from django.contrib import admin
from django.urls import path
from library.views import BookView, home_view, student_view, admin_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/signup/', admin_signup, name='admin_signup'),
    path('books/', BookView.as_view(), name='book_list_create'),  # Use BookView for /books/
    path('books/<int:pk>/', BookView.as_view(), name='book_detail'),  # For individual book operations
    path('student/', student_view, name='student_view'),
    path('', home_view, name='home'),  # Root URL
]