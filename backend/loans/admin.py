from typing import List
from django.contrib import admin
from django.db import models
from django.urls.resolvers import URLPattern
from loans.models import LoanField, LoanProposal
from django import forms
from django.utils.html import format_html
from django.urls import reverse
from django.template.response import TemplateResponse
from django.urls import path
from django.shortcuts import redirect, get_object_or_404

admin.site.site_header = "Loans For Good"
admin.site.site_title = "Loans For Good Admin"
admin.site.index_title = "Loans For Good Admin"


class LoanFieldInline(admin.TabularInline):
    model = LoanProposal.custom_fields.through


@admin.register(LoanField)
class LoanFieldAdmin(admin.ModelAdmin):
    list_display = ["name", "label", "data_type"]


@admin.register(LoanProposal)
class LoanProposalAdmin(admin.ModelAdmin):
    inlines = [LoanFieldInline]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<str:object_id>/approve/",
                self.approve_proposal,
                name="approve_proposal",
            ),
            path("<str:object_id>/deny/", self.deny_proposal, name="deny_proposal"),
        ]
        return custom_urls + urls

    def approve_proposal(self, request, object_id):
        proposal = get_object_or_404(LoanProposal, pk=object_id)
        proposal.approved = "approved"
        proposal.save()
        return redirect("admin:loans_loanproposal_changelist")

    def deny_proposal(self, request, object_id):
        proposal = get_object_or_404(LoanProposal, pk=object_id)
        proposal.approved = "denied"
        proposal.save()
        return redirect("admin:loans_loanproposal_changelist")

    def approval_buttons(self, obj):
        approve_url = reverse("admin:approve_proposal", args=[obj.pk])
        deny_url = reverse("admin:deny_proposal", args=[obj.pk])

        match obj.auto_approved, obj.approved:
            case "approved", "pending":
                return format_html(
                    f'<a class="button" href="{approve_url}">Aprovar</a> '
                    f'<a class="button" href="{deny_url}">Negar</a>'
                )
            case "approved", "approved":
                return format_html(f'<a class="button" href="{deny_url}">Negar</a>')
            case "approved", "denied":
                return format_html(
                    f'<a class="button" href="{approve_url}">Aprovar</a>'
                )
            case _, _:
                return "N/A"

    approval_buttons.short_description = "Aprovar/Desaprovar Proposta"
    approval_buttons.allow_tags = True

    actions = [approve_proposal, deny_proposal]

    @admin.display(description="Status")
    def status_display(self, obj):
        if obj.auto_approved == "denied":
            return "Negado pelo provedor"

        status = {
            "approved": "Aprovado",
            "denied": "Negado",
            "pending": "Pendente",
        }

        return status.get(obj.approved, "N/A")

    @admin.display(description="CPF")
    def cpf_display(self, obj):
        return obj.document

    readonly_fields = ["name", "cpf_display", "status_display", "approval_buttons"]
    list_display = ["name", "cpf_display", "status_display"]
    list_filter = [
        "approved",
    ]

    search_fields = ["name", "document"]

    fieldsets = (
        (
            None,
            {
                "fields": ("name", "cpf_display", "status_display", "approval_buttons"),
            },
        ),
    )
