from django.urls import path
# project library
from Api import views

urlpatterns = [
    # vendor urls

    path('post/vendor/', views.VendorAPI.as_view()),
    path('get/vendor/', views.VendorAPI.as_view()),
    path('get/vendor/<int:vendor_id>/', views.EditVendorAPI.as_view()),
    path('Put/vendor/<int:vendor_id>/', views.EditVendorAPI.as_view()),
    path('delete/vendor/<int:vendor_id>/', views.EditVendorAPI.as_view()),
    
    # purchase Order Urls

    path('post/purchase_orders/', views.PurchaseOrderAPI.as_view()),
    path('get/purchase_orders/', views.PurchaseOrderAPI.as_view()),
    path('get/purchase_orders/<int:po_id>/', views.EditPurchaseOrderAPI.as_view()),
    path('put/purchase_orders/<int:po_id>/', views.EditPurchaseOrderAPI.as_view()),
    path('delete/purchase_orders/<int:po_id>/', views.EditPurchaseOrderAPI.as_view()),
    
    # performance Url
    
    path('vendors/<int:vendor_id>/performance', views.VendorPerformanceAPI.as_view()),

]