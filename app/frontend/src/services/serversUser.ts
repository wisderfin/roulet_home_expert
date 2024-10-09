import axios from "axios"

const tg = window.Telegram.WebApp

// Получает id и username из Telegram
export function getUserInfo(): string {
  return JSON.stringify({
    id: tg.initDataUnsafe.user?.id,
    username: tg.initDataUnsafe.user?.username,
  })
}

// Регестрирует пользователя в базе данных
export async function registerUser(): Promise<any> {

  try {
    const response = await axios({
      method: "post",
      url: "https://locback.ru.tuna.am/user/create",
      data: getUserInfo(),
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + btoa('login:password')
      }
    });

    return response.data; // Возвращаем данные от сервера
  } catch (error: any) {
    // Обработка ошибки
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data.message || 'An error occurred during registration');
    } else {
      throw new Error('An unexpected error occurred');
    }
  }
}


export async function playRoulette(bid: number): Promise<any> {
  try {
    const response = await axios({
      method: "post",
      url: "https://locback.ru.tuna.am/game/presents",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + btoa('login:password')
      },
      data: {
        "deposit": {
          "deposit": bid
        },
        "user": {
          "id": JSON.parse(getUserInfo()).id
        }
      }
    });

    return response.data; // Возвращаем данные от сервера
  } catch (error: any) {
    if (error.code == "ERR_NETWORK") {
      throw new Error("Сервер не доступен!")
    } else {
      throw new Error(error)

    }
  }}
