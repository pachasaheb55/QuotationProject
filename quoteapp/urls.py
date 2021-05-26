""" URL's for quote application """
from django.urls import path
from quoteapp.views import HomePageView, CreateQuoteView, \
    QuoteSummaryView, CustomerView

urlpatterns = [
    # url for landing/home page
    path('', HomePageView.as_view()),
    path('createQuote/', CreateQuoteView.as_view()),
    path('quoteSummary/<int:quote_id>/', QuoteSummaryView.as_view()),
    path('customer/', CustomerView.as_view())
]
