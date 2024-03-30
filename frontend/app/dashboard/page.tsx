import {EntidadesSelect} from "@/components/ui/combobox";
import {DataTable} from "@/app/dashboard/data-table";
import {columns} from "./columns"

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

  // const entidade = searchParams['curso__campus_id'] ?? ""

  function filtraValidacao() {
    console.log('function')
  }

  const data = await getData(searchParams);

  return <>
    <h1>Pé-de-meia</h1>

    <section>
      <EntidadesSelect entidades={data['entidades']}/>
    </section>

    <section className={'flex flex-row space-x-20 mt-10'}>
      <div className={'basis-1/8'}>
        <div className={'mb-5'}>
          <h2>Informações</h2>
        </div>

        <div className={'p-4 mb-5 rounded-lg shadow info'}>
          <span>Discentes</span>
          <h3>{data['count']}</h3>
        </div>

        <div className={'divide-y rounded-lg shadow info'}>
          {data['info'] && Object.entries(data['info']).map(([key, value], i) => (
            <div key={i}>
              <span>{key}</span>
              <h3 className={value === 0 ? 'text-emerald-500' : 'text-orange-500'}>{value}</h3>
            </div>
          ))}
        </div>
      </div>
      <div className={'grow'}>
        <div className={'mb-5'}>
          <h2>Discentes</h2>
        </div>
        <DataTable columns={columns} data={data['results']}/>
      </div>
    </section>
  </>
}