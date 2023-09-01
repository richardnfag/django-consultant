from rest_framework import status
import pytest


class TestAvailableFieldsView:
    @pytest.mark.django_db
    def test_get_available_fields(self, client, loan_field):
        response = client.get("/available-fields/")
        expected_fields = [
            {"name": "name", "label": "Nome Completo", "data_type": "text"},
            {"name": "document", "label": "CPF", "data_type": "text"},
            {
                "name": "valor_da_proposta",
                "label": "Valor da Proposta",
                "data_type": "number",
            },
        ]

        assert response.status_code == status.HTTP_200_OK

        print(f"response.data: {response.data}")
        print(f"expected_fields: {expected_fields}")
        assert response.data == expected_fields


class TestSubmitProposalView:
    @pytest.mark.django_db
    def test_submit_proposal(self, client, loan_field):
        data = [
            {"name": "name", "value": "Richard do Nascimento Fagundes"},
            {"name": "document", "value": "47635245769"},
            {"name": "valor_da_proposta", "value": "20000"},
        ]

        response = client.post(
            "/submit-proposal/", data=data, content_type="application/json"
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data == {"message": "Proposal submitted successfully."}

    @pytest.mark.django_db
    def test_submit_proposal_with_invalid_data(self, client, loan_field):
        invalid_data = [{"invalid_key": "invalid_value"}]

        response = client.post(
            "/submit-proposal/", data=invalid_data, content_type="application/json"
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.django_db
    def test_submit_proposal_without_name(self, client, loan_field):
        data = [
            {"name": "document", "value": "47635245769"},
            {"name": "valor_da_proposta", "value": "20000"},
        ]

        response = client.post(
            "/submit-proposal/", data=data, content_type="application/json"
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {"message": "required fields are missing"}
