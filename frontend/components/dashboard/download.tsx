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

  return (
    <div className={'text-right'}>
        <span>
          <TooltipProvider>
            <Tooltip>
              <TooltipTrigger>
                <a href={`${api_url}/estudantes/download_csv/`}>
                  <CloudDownloadIcon size={22}/>
                </a>
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