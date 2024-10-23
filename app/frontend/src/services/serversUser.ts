import axios from "axios"

const tg = window.Telegram.WebApp

// Получает id и username из Telegram
export function getUserInfo(): string {
  return JSON.stringify({
    id: tg.initDataUnsafe.user?.id,
    username: tg.initDataUnsafe.user?.username,
  })
}



export async function playRoulette(): Promise<any> {
  try {
    const response = await axios({
      method: "post",
      url: `https://locback.nl.tuna.am/game/presents?id=${tg.initDataUnsafe.user?.id}&username=${tg.initDataUnsafe.user?.username}`,
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    });

    return response.data; // Возвращаем данные от сервера
  } catch (error: any) {
    if (error.code == "ERR_NETWORK") {
      throw new Error("Сервер не доступен!")
    } else if (error.code == "ERR_BAD_REQUEST") {
      throw "Не прошло 24 часа!"

    }
  }}


export async function getTimeUser() {
  
  try {
    const response = await axios({
      method: "get",
      url: `https://locback.nl.tuna.am/game/time?id=${tg.initDataUnsafe.user?.id}`,
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      }, 
    });

    return response.data;
  } catch (error: any) {
    throw error
  }
}
