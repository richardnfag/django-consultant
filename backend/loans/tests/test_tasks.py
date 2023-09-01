from loans.tasks import submit_proposal_task
from unittest.mock import patch


class TestTaskLoanProposal:
    @patch("loans.tasks.requests.post")
    def test_submit_proposal_task_approved(self, mock_post, loan_proposal):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"approved": True}

        response = submit_proposal_task(loan_proposal.id)
        expected_response = "Proposal updated with approval status"

        assert response == expected_response

    @patch("loans.tasks.requests.post")
    def test_submit_proposal_task_denied(self, mock_post, loan_proposal):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"approved": False}

        response = submit_proposal_task(loan_proposal.id)
        expected_response = "Proposal updated with approval status"

        assert response == expected_response

    @patch("loans.tasks.requests.post")
    def test_submit_proposal_task_http_error(self, mock_post, loan_proposal):
        mock_post.return_value.status_code = 404

        response = submit_proposal_task(loan_proposal.id)
        expected_response = "Error: verifying proposal approval"

        assert response == expected_response

    @patch("loans.tasks.requests.post")
    def test_submit_proposal_task_with_bad_response(self, mock_post, loan_proposal):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"error": "error"}

        response = submit_proposal_task(loan_proposal.id)
        expected_response = "Error: bad api response"

        assert response == expected_response

    @patch("loans.tasks.requests.post")
    def test_submit_proposal_task_with_invalid_id(self, mock_post, loan_proposal):
        response = submit_proposal_task(999)
        expected_response = "Error: LoanProposal matching query does not exist."

        assert response == expected_response
