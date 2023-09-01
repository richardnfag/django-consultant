import "./globals.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import LoanProposalPanel from "./components/LoanProposalPanel";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Loan Proposal",
  description: "Loan Proposal Form",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <LoanProposalPanel>{children}</LoanProposalPanel>
      </body>
    </html>
  );
}
