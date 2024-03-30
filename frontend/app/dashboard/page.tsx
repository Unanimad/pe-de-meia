// <!-- text-orange-500 text-emerald-500 -->


export default function Page() {
    return <>
        <h1>Dashboard Page!</h1>
        <section className={'flex flex-row space-x-4 mt-10'}>
            <div className={'basis-1/4 rounded  '}>
                <div className={'mb-5'}>
                    <h2>Informações</h2>
                </div>
                <div className={'p-4 divide-y shadow-xl info'}>
                    <div>
                        <span>ljkadsjlks</span>
                        <h3>0</h3>
                    </div>
                    <div>
                        <span>ljkadsjlks</span>
                    </div>
                    <div>
                        <span>ljkadsjlks</span>
                    </div>
                </div>
            </div>
            <div className={'basis-1/2'}>
                <div className={'rounded shadow p-4'}>
                    <h2>Discentes</h2>
                </div>
            </div>
        </section>
    </>
}