from loans.models import LoanField


class TestModelLoanField:
    def test_str(self, loan_field):
        assert str(loan_field) == "Valor da Proposta"

    def test_static_fields_names(self):
        assert LoanField.static_fields_names() == ["name", "document"]

    def test_get_available_fields(self, loan_field):
        assert LoanField.get_available_fields() == [
            {"name": "name", "label": "Nome Completo", "data_type": "text"},
            {"name": "document", "label": "CPF", "data_type": "text"},
            {
                "name": "valor_da_proposta",
                "label": "Valor da Proposta",
                "data_type": "number",
            },
        ]


class TestModelLoanProposal:
    def test_str(self, loan_proposal):
        assert str(loan_proposal) == "Richard"


class TestModelCustomFieldValue:
    def test_str(self, custom_field_value):
        assert str(custom_field_value) == "Richard - Valor da Proposta: 100000"
