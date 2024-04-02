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
import {Toaster} from "@/components/ui/toaster"
import {useToast} from "@/components/ui/use-toast"
import {Button} from "@/components/ui/button";

const api_url = 'http://localhost:8000/api'

async function getData(searchParams) {
  let url = api_url + '/estudantes/?' + new URLSearchParams(searchParams)

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 3000);
  const {toast} = useToast()

  try {
    const response = await fetch(url, {
      signal: controller.signal
    });
    clearTimeout(timeoutId); // Cancela o timeout se a requisição for bem-sucedida
    return await response.json();
  } catch (error) {

    clearTimeout(timeoutId); // Cancela o timeout se ocorrer um erro
    toast({
      description: "Não foi possível contactar o servidor. Aguarde alguns instantes.",
    })
  }
}

function downloadCSV() {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 3000);
  const url = api_url + '/estudantes/download_csv/'

  try {
    const response = fetch(url, {
      signal: controller.signal
    });
    clearTimeout(timeoutId); // Cancela o timeout se a requisição for bem-sucedida
    return response;
  } catch (error) {
    clearTimeout(timeoutId); // Cancela o timeout se ocorrer um erro
    throw error;
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
            <div className={'text-right'}>
              <span>
                <TooltipProvider>
                  <Tooltip>
                    <TooltipTrigger>
                      <Button onClick={downloadCSV}><CloudDownloadIcon
                        size={22}/></Button></TooltipTrigger>
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

    <Toaster/>
  </>
}