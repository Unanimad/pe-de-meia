"use client";

import {useRouter, useSearchParams} from "next/navigation";

const Info = ({data}) => {
  const router = useRouter()
  const searchParams = useSearchParams()

  const urlSearchParams = new URLSearchParams(searchParams.toString())

  function filtraValidade(key, value) {
    const params = urlSearchParams
    params.set(key, value)
    router.replace(`/dashboard?${params.toString()}`)
  }

  return (
    <div className={'divide-y rounded-lg shadow info'}>
      {data['info'] && Object.entries(data['info']).map(([key, value], i) => (
        <div key={i} onClick={() => filtraValidade(value?.qs?.split('=')[0], value?.qs?.split('=')[1])}>
          <span>{value?.label}</span>
          <h3 className={value?.total === 0 ? 'text-emerald-500' : 'text-orange-500'}>{value?.total}</h3>
        </div>
      ))}
    </div>
  )
}

export default Info