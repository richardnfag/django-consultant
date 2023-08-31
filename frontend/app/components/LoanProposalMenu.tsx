'use client'
import { MoneyHand24Regular, BuildingBank24Regular } from "@fluentui/react-icons";
import { FluentProvider, webDarkTheme } from "@fluentui/react-components";

export default function LoanProposalMenu() {
    return (
        <header>
            <FluentProvider theme={webDarkTheme}>
            <h1><BuildingBank24Regular /> Loans For Good</h1>
            </FluentProvider>
            <h2><MoneyHand24Regular />Loan Proposal</h2>
        </header>
    )
}
