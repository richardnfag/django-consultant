from django.urls import path
from loans import views

urlpatterns = [
    path(
        "available-fields/",
        views.AvailableFieldsView.as_view(),
        name="available-fields",
    ),
    path(
        "submit-proposal/", views.SubmitProposalView.as_view(), name="submit-proposal"
    ),
]
