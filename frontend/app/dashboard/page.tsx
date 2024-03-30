// <!-- text-orange-500 text-emerald-500 -->

async function getData() {
    const res = await fetch('http://localhost:8000/api/estudantes/?format=json')
    if (!res.ok) {
        throw new Error('Failed to fetch data')
    }
    return res.json()
}


export default async function Page() {

    const data = await getData();

    return <>
        <h1>Dashboard Page!</h1>
        <section className={'flex flex-row space-x-4 mt-10'}>
            <div className={'basis-1/4'}>
                <div className={'mb-5'}>
                    <h2>Informações</h2>
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
            <div className={'basis-1/2 '}>
                <div className={'mb-5'}>
                    <h2>Discentes</h2>
                </div>
                <div className={'rounded shadow p-4'}>

                </div>
            </div>
        </section>
    </>
}