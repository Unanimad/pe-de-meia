"use client";

import React from "react";

import type {DateRange} from "react-day-picker"
import { ptBR } from 'date-fns/locale';

import {Calendar} from "@/components/ui/calendar"

const Ciclo = ({data}) => {

  const ranges: DateRange[] = Object.entries(data.results).map(([key, value], i) => ({
    from: value?.data_inicio,
    to: value?.data_fim,
  }))

  return (<div>

    <Calendar
      mode="range"
      selected={ranges}
      locale={ptBR}
      className="rounded-md border"
    />

  </div>)
}

export default Ciclo