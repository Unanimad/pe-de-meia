"use client"

import {ColumnDef} from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Estudante = {
    cpf: number
    nome: string
    data_nascimento: string
    nome_mae: string
    etapa_ensino: number
}

export const columns: ColumnDef<Estudante>[] = [
    {
        accessorKey: "cpf",
        header: "CPF",
    },
    {
        accessorKey: "nome",
        header: "Nome do discente",
    },
    {
        accessorKey: "data_nascimento",
        header: "Data de nascimento",
    },
    {
        accessorKey: "nome_mae",
        header: "Nome da mãe",
    },
    {
        accessorKey: "etapa_ensino",
        header: "Etapa de ensino",
    },
]
