import '@/app/ui/global.css';

import { inter } from '@/app/ui/fonts';

export default function RootLayout({ children }) {
  return (
    <html lang="pt-br">
      <body className={`${inter.className} antialiased`}>{children}</body>
    </html>
  );
}
