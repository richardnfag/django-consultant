from celery import shared_task
from loans.models import LoanProposal
import requests

@shared_task
def submit_proposal_task(proposal_id):
    try:
        proposal = LoanProposal.objects.get(id=proposal_id)
        proposal_data = {
            "document": proposal.document,
            "name": proposal.name,
        }

        print(proposal_data)
        response = requests.post('https://loan-processor.digitalsys.com.br/api/v1/loan/', json=proposal_data)

        if response.status_code == 200:
            result = response.json().get('approved')
            if result:
                proposal.auto_approved = 'approved'
                proposal.save()
                return "Proposal updated with approval status"

        return "Error verifying proposal approval"

    except Exception as e:
        return f"Error: {e}"
