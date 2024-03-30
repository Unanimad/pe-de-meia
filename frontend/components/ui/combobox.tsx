"use client"

import * as React from "react"
import {Check, ChevronsUpDown} from "lucide-react"

import {cn} from "@/lib/utils"
import {Button} from "@/components/ui/button"
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
} from "@/components/ui/command"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"


export function EntidadesSelect({entidades}) {
  const [open, setOpen] = React.useState(false)
  const [value, setValue] = React.useState("")

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          role="combobox"
          aria-expanded={open}
          className="justify-between"
        >
          {value
            ? entidades?.find((entidade) => entidade?.nome.toLowerCase() === value.toLowerCase())?.nome
            : "Selecione uma unidade..."}
          <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50"/>
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-[200px] p-0">
        <Command>
          <CommandInput placeholder="Selecione uma unidade..."/>
          <CommandEmpty>Unidade não encontrada.</CommandEmpty>
          <CommandGroup>
            {entidades?.map((entidade) => (
              <CommandItem
                key={entidade?.id}
                value={entidade?.nome}
                onSelect={(currentValue) => {
                  setValue(currentValue)
                  setOpen(false)
                  console.log(`curso__campus_id=${entidade.campus}`)
                }}
              >
                <Check
                  className={cn(
                    "mr-2 h-4 w-4",
                    value === entidade?.nome ? "opacity-100" : "opacity-0"
                  )}
                />
                {entidade?.nome}
              </CommandItem>
            ))}
          </CommandGroup>
        </Command>
      </PopoverContent>
    </Popover>
  )
}
