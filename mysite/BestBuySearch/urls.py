from django.shortcuts import render

from django.urls import path

from . import views

# Create your urls here.

app_name = 'BestBuySearch'

urlpatterns = [
         #ex: /BestBuySearch/
         #path('', views.IndexView.as_view(), name='index'),
         #path('products/', views.ProductView.as_view(), name = "products"),
         
         #basic homepage + details:
         path('products/', views.ProductView.as_view(), name = "products"),
         path('products/<int:pk>/product_details/', views.ProductDetailsView.as_view(), name = "product_details"),
         #signups:
         path("customer_signup/", views.CustomerSignUpView.as_view(), name = "customer_signup"),
         path("vendor_signup/", views.VendorSignUpView.as_view(), name = "vendor_signup"),
         #search results:
         path('products/similar_search/', views.SimilarResultsView.as_view(), name = "similar_results"),
         path('products/exact_search/', views.ExactResultsView.as_view(), name = "exact_results"),
            #path('products/requirement_search/', views.RequirementResultsView.as_view(), name = "requirement_results"),
         path('products/requirement_search/MultipleSearch/', views.MultipleSearch, name = "MultipleSearch"),
            #path('products/requirement_search/<str:name>/<int:cost>/<int:category>/<int:payment_type>/', views.myfunct, name = "myfunct"),
         #product editing:
         path('products/add_product/', views.ProductCreateView.as_view(), name = 'add_product'),
         path('products/all_products/', views.AllProductsView.as_view(), name = 'all_products'),
         path('products/all_products/<int:pk>/update/', views.ProductUpdateView.as_view(), name = 'update_product'),
         path('products/all_products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name = 'delete_product'),
         #cart urls:
         path('products/checkout/', views.Cart.as_view(), name = 'checkout'),
         path('products/<int:pk>/add_to_cart/', views.add_to_cart, name = 'add_to_cart'),
         path('products/checkout/<int:pk>/rm_from_cart/', views.rm_from_cart, name = 'rm_from_cart'),
         
         #polls:
         #ex: /BestBuySearch/5/
         #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
         #ex: /BestBuySearch/5/results/
         #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
         #ex: /BestBuySearch/5/vote/
         #path('<int:question_id>/vote/', views.vote, name='vote')
       ]
