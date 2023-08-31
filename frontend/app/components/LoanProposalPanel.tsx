
'use client'
import { FluentProvider, webLightTheme } from "@fluentui/react-components";
import LoanProposalMenu from "./LoanProposalMenu";
import React, { ReactNode } from "react";

interface Props {
    children?: ReactNode
}

export default function LoanProposalPanel({ children, ...props }: Props) {
    return (
        <FluentProvider theme={webLightTheme}>
            <LoanProposalMenu />
            {children}
        </FluentProvider>
    )
}
