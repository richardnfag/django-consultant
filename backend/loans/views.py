from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from loans.models import LoanField, LoanProposal
from loans.tasks import submit_proposal_task
from django.shortcuts import get_object_or_404, redirect

class AvailableFieldsView(APIView):
    def get(self, request, format=None):
        fields = LoanField.get_available_fields()
        return Response(fields, status=status.HTTP_200_OK)


class SubmitProposalView(APIView):
    def post(self, request, format=None):
        try:
            custom_fields = []
            static_fields = {}

            static_fields_names = LoanField.static_fields_names()

            for field in request.data:
                for static_field_name in static_fields_names:
                    if field['name'] == static_field_name:
                        static_fields.update({field['name']: field['value']})

                if field['name'] not in static_fields_names:
                    custom_fields.append(field)

            if sorted(static_fields.keys()) != sorted(static_fields_names):
                raise ValueError('required fields are missing')
            
            proposal = LoanProposal.objects.create(**static_fields, approved='pending', auto_approved='pending')

            for field in custom_fields:
                loan_field = LoanField.objects.get(name=field['name'])
                value = field['value']
                proposal.custom_fields.add(loan_field,through_defaults={'value': value})

            submit_proposal_task.delay(proposal.id)
            return Response({'message': 'Proposal submitted successfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

