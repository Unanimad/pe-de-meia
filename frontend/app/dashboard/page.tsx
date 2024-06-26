import {EntidadesSelect} from "@/components/ui/combobox";
import {DataTable} from "@/app/dashboard/data-table";
import {columns} from "./columns"
import {CloudDownloadIcon} from "lucide-react";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"
import Info from "@/components/dashboard/info"
import Link from 'next/link'

async function getData(searchParams) {
  let url = 'http://localhost:8000/api/estudantes/?' + new URLSearchParams(searchParams)

  console.log(url)

  const res = await fetch(url)
  if (!res.ok) {
    throw new Error('Failed to fetch data')
  }
  return res.json()
}


export default async function Page({searchParams}) {

  const data = await getData(searchParams);

  return <>
    <h1>Pé-de-meia</h1>

    <section>
      <EntidadesSelect entidades={data['entidades']}/>
    </section>

    <section className={'flex flex-row space-x-20 mt-10'}>
      <div className={'basis-1/8'}>
        <div className={'mb-5'}>
          <h2>Geral</h2>
        </div>

        <div className={'p-4 mb-5 rounded-lg shadow info'}>
          <span>Discentes</span>
          <h3 className={'text-blue-500'}>{data['count']}</h3>
        </div>

        <Info data={data}/>

      </div>
      <div className={'grow'}>
        <div className={'mb-5'}>
          <div className={'grid grid-cols-2'}>
            <div>
              <h2>Discentes</h2>
            </div>
            <div className={'text-right'}>
              <span>
                <TooltipProvider>
                  <Tooltip>
                    <TooltipTrigger>
                       <Link href="http://localhost:8000/api/estudantes/download_csv/"> <CloudDownloadIcon
                         size={22}/></Link></TooltipTrigger>
                    <TooltipContent>
                      <p>Fazer download da planilha.</p>
                    </TooltipContent>
                  </Tooltip>
                </TooltipProvider>
              </span>
            </div>
          </div>
        </div>
        <DataTable columns={columns} data={data['results']}/>
      </div>
    </section>

  </>
}