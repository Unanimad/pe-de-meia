import {EntidadesSelect} from "@/components/ui/combobox";
import {DataTable} from "@/app/dashboard/data-table";
import {columns} from "./columns"
import {api_url, getData} from "@/app/service"

import Info from "@/components/dashboard/info"
import Download from "@/components/dashboard/download";
import Ciclo from "@/components/dashboard/ciclos"


export default async function Page({searchParams}) {

  const data = await getData(`${api_url}/estudantes/?`, searchParams);

  return <>
    <h1>Pé-de-meia</h1>

    <section>
      {(data['entidades'] !== undefined && data['entidades'] !== null) &&
          <EntidadesSelect entidades={data['entidades']}/>}
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

        {(data["info"] !== undefined && data["info"] !== null) && <Info data={data["info"]}/>}

      </div>
      <div className={'grow'}>
        <div className={'mb-5'}>
          <div className={'grid grid-cols-2'}>
            <h2>Discentes</h2>
            <Download/>
          </div>
        </div>

        <DataTable columns={columns} data={data['results']}/>
      </div>
    </section>

  </>
}