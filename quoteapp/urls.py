from django.urls import path

from .views import *

urlpatterns = [
    # url for landing/home page
    path('', HomePageView.as_view()),
    path('createQuote/', CreateQuoteView.as_view()),
    path('quoteSummary/<int:quote_id>/', QuoteSummaryView.as_view()),
    path('customer/', CustomerView.as_view())
]