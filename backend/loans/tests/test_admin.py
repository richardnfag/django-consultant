import pytest
from django.urls import reverse


class TestAdminLoanProposal:

    @pytest.mark.django_db
    def test_approve_proposal(self, admin_client, loan_proposal):
        change_url = reverse('admin:loans_loanproposal_change', args=[loan_proposal.pk])
        response = admin_client.get(change_url)
        assert response.status_code == 200

        approve_url = reverse('admin:approve_proposal', args=[loan_proposal.pk])
        response = admin_client.post(approve_url, follow=True)
        assert response.status_code == 200

        loan_proposal.refresh_from_db()
        assert loan_proposal.approved == 'approved'


    @pytest.mark.django_db
    def test_deny_proposal(self, admin_client, loan_proposal):
        change_url = reverse('admin:loans_loanproposal_change', args=[loan_proposal.pk])
        response = admin_client.get(change_url)
        assert response.status_code == 200

        deny_url = reverse('admin:deny_proposal', args=[loan_proposal.pk])
        response = admin_client.post(deny_url, follow=True)
        assert response.status_code == 200

        loan_proposal.refresh_from_db()
        assert loan_proposal.approved == 'denied'
    