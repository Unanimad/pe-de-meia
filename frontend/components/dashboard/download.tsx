"use client";

import {CloudDownloadIcon} from "lucide-react";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"

import {api_url} from "@/app/service"

const Download = () => {

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

  return (
    <div className={'text-right'}>
        <span>
          <TooltipProvider>
            <Tooltip>
              <TooltipTrigger>
                <CloudDownloadIcon onClick={downloadCSV}
                  size={22}/>
              </TooltipTrigger>
              <TooltipContent>
                <p>Fazer download da planilha.</p>
              </TooltipContent>
            </Tooltip>
          </TooltipProvider>
        </span>
    </div>
  )
}

export default Download;