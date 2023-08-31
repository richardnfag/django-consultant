import pytest
from loans.models import LoanField, LoanProposal, CustomFieldValue


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    # db fixture manages the transactions
    pass


@pytest.fixture
def loan_field():
    return LoanField.objects.create(
        name="valor_da_proposta",
        label="Valor da Proposta",
        data_type="number",
        visible=True
    )

@pytest.fixture
def loan_proposal():
    return LoanProposal.objects.create(
        name="Richard",
        document="12340574558",
        approved="pending",
        auto_approved="pending",
    )

@pytest.fixture
def custom_field_value(loan_proposal, loan_field):
    return CustomFieldValue.objects.create(
        loan_proposal=loan_proposal,
        loan_field=loan_field,
        value="100000"
    )
