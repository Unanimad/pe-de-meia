import {EntidadesSelect} from "@/components/ui/combobox";
import {DataTable} from "@/app/dashboard/data-table";
import {columns} from "./columns"

import Info from "@/components/dashboard/info"
import Download from "@/components/dashboard/download";
// import {Toaster} from "@/components/ui/toaster"

const api_url = 'http://localhost:8000/api'

async function getData(searchParams) {
  let url = api_url + '/estudantes/?' + new URLSearchParams(searchParams)

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 3000);
  // const toast = useToast

  try {
    const response = await fetch(url, {
      signal: controller.signal
    });
    clearTimeout(timeoutId); // Cancela o timeout se a requisição for bem-sucedida
    return await response.json();
  } catch (error) {

    clearTimeout(timeoutId); // Cancela o timeout se ocorrer um erro
    // toast({
    //   description: "Não foi possível contactar o servidor. Aguarde alguns instantes.",
    // })
  }
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

        {(data["info"] !== undefined && data["info"] !== null) && <Info data={data["info"]}/>}

      </div>
      <div className={'grow'}>
        <div className={'mb-5'}>
          <div className={'grid grid-cols-2'}>
            <div>
              <h2>Discentes</h2>
            </div>
            <Download/>
          </div>
        </div>
        <DataTable columns={columns} data={data['results']}/>
      </div>
    </section>

  </>
}