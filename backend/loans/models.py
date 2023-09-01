from django.db import models


class LoanField(models.Model):
    DATA_TYPE_CHOICES = [
        ("text", "text"),
        ("number", "number"),
        ("date", "date"),
        ("email", "email"),
        ("tel", "tel"),
    ]

    REQUIRED_FIELDS = [
        {"name": "name", "label": "Nome Completo", "data_type": "text"},
        {"name": "document", "label": "CPF", "data_type": "text"},
    ]

    name = models.CharField(max_length=100, unique=True)
    label = models.CharField(max_length=100)
    data_type = models.CharField(max_length=20, choices=DATA_TYPE_CHOICES)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.label

    @classmethod
    def static_fields_names(cls):
        return [field["name"] for field in cls.REQUIRED_FIELDS]

    @classmethod
    def get_available_fields(cls):
        available_fields = LoanField.REQUIRED_FIELDS.copy()
        dynamic_fields = list(
            cls.objects.values("name", "label", "data_type").filter(visible=True)
        )
        available_fields.extend(dynamic_fields)
        return available_fields


class LoanProposal(models.Model):
    APPROVAL_CHOICES = [
        ("approved", "approved"),
        ("pending", "pending"),
        ("denied", "denied"),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    document = models.CharField(max_length=100, null=False, blank=False)
    approved = models.CharField(max_length=100, choices=APPROVAL_CHOICES)
    auto_approved = models.CharField(max_length=100, choices=APPROVAL_CHOICES)
    custom_fields = models.ManyToManyField(LoanField, through="CustomFieldValue")

    def __str__(self):
        return self.name


class CustomFieldValue(models.Model):
    loan_proposal = models.ForeignKey(LoanProposal, on_delete=models.CASCADE)
    loan_field = models.ForeignKey(LoanField, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.loan_proposal} - {self.loan_field}: {self.value}"
