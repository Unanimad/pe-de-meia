import './style.css'

export default function DashboardLayout({
  children, // will be a page or nested layout
}: {
  children: React.ReactNode
}) {
  return (
    <main className={'md:container md:mx-auto'}>
      {children}
    </main>
  )
}