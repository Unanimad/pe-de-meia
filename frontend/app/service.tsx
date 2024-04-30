export const api_url = 'http://localhost:8000/api'

export async function getData(url, searchParams) {
  url += new URLSearchParams(searchParams)

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