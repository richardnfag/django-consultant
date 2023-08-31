"use client"
import {
  Button,
  makeStyles,
  shorthands,
  Input,
  Label,
  Spinner,
  Body1,
} from "@fluentui/react-components";

import {Send24Regular} from "@fluentui/react-icons";

import { useEffect, useState, FormEvent } from 'react'

type Proposal = Array<CustomField>

type FormDataType = "number" | "search" | "time" | "text" | "date" | "tel" | "url" | "email" | "password" | "datetime-local" | "month" | "week" | undefined;

interface CustomField {
  name: string;
  value: string;
}

interface Field {
  name: string;
  label: string;
  data_type: string;
}


const useStyles = makeStyles({
  root: {
    display: "flex",
    flexDirection: "column",
    ...shorthands.gap("20px"),
    maxWidth: "400px",
    "> div": {
      display: "flex",
      flexDirection: "column",
      ...shorthands.gap("2px"),
    },

  },
  body: {
    textAlign: "center",
    flexDirection: "column",
    ...shorthands.gap("20px"),
    maxWidth: "400px",
    "> div": {
      display: "flex",
      flexDirection: "column",
      ...shorthands.gap("2px"),
    },
  }
});


export default function LoanProposalForm() {
  const styles = useStyles();
  const [data, setData] = useState<Array<Field>>([]);
  const [isLoading, setLoading] = useState(true);

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    let name_item = document.getElementById("name") as HTMLInputElement;
    if (name_item == null) return;

    const proposal: Proposal = [];

    data.forEach(field => {
      let item = document.getElementById(field.name) as HTMLInputElement;
      if (item == null) return;

      proposal.push({"name": field.name, "value": item.value});
    
    });

    const response = await fetch('http://localhost:8000/submit-proposal/', {
      method: 'POST',
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(proposal)
    });
 
    const res = await response.json()
    console.log("Submitted Response:");
    console.log(res);
  }

  useEffect(() => {
    fetch("http://localhost:8000/available-fields/", {
      mode: "cors",
      method: "GET",
      headers: {"Content-Type": "application/json"}
    })
    .then(res => res.json())
    .then(data => {
      setData(data)
      setLoading(false)
    })
    .catch(err => console.log(err));
  }, [])

  if (isLoading) return (
    <div className={styles.root}>
      <Spinner appearance="primary" label="Loading ..." />
    </div>
  );

  if (data.length === 0) return (
    <div className={styles.body}>
        <Body1>O Formulário para solicitação de empréstimo pessoal ainda não esta disponível. <br/> Tente entrar novamente mais tarde.</Body1>
    </div>
  );

  return (
      <form className={styles.root} onSubmit={onSubmit}>
      {data.map((field) => {
        return (
          <div key={field.name}>
            <Label htmlFor={field.name}>{field.label}</Label>
            <Input type={field.data_type as FormDataType} id={field.name} />
          </div>
        );
      })}
      <Button type="submit" appearance="primary" icon={<Send24Regular/>}>Enviar Proposta</Button>
      </form>
  );

};
