import type { Metadata } from "next";
import { Poppins } from "next/font/google";
import "./globals.css";

const font_ = Poppins({  weight: ['300', '500', '700'], subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Pé-de-meia",
  description: "Controle de qualidade dos dados.",
  authors: [{"name": "Instituto Federal de Sergipe", "url": "https://www.ifs.edu.br/"}],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-br">
      <body className={`${font_.className} mx-auto pt-10` }>{children}</body>
    </html>
  );
}
