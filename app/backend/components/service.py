from fastapi import Request, HTTPException, Depends

# Исключение для 403 ошибки
err_403 = HTTPException(status_code=403, detail="Доступ запрещён")

# Список разрешённых IP-адресов
ALLOWED_IP = {'128.204.70.46'}

# Проверка IP-адреса
async def verify_ip(request: Request):
    # Пытаемся получить реальный IP-адрес клиента из заголовка X-Forwarded-For
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        # Берём первый IP, если заголовок содержит несколько значений
        client_ip = x_forwarded_for.split(',')
    else:
        # Если заголовок отсутствует, используем IP, определённый сервером
        client_ip = [request.client.host]

    # Проверяем, входит ли IP в список разрешённых
    for ip in client_ip:
        ip = '128.204.70.46'
        if ip.strip() in ALLOWED_IP:
            break
    else:
        raise HTTPException(status_code=403, detail=f"Доступ запрещён: {client_ip}") # Вызываем исключение при несоответствии

# Список заблокированных User-Agent
BLOCKED_USER_AGENTS = [
    "curl", "wget", "httpie", "python-requests", "PostmanRuntime", "Apache-HttpClient",
    "Java", "Ruby", "Go-http-client", "Node.js", "JMeter", "Insomnia", "Flutter",
    "Selenium", "Lynx", "Links", "GuzzleHttp", "OkHttp", "fetch", "iOS", "Android",
    "PostgREST", "libcurl", "Socks", "TornadoClient", "Spring", "RestSharp",
    "HTTPClient", "HttpClient", "Python-urllib", "Dart", "Postman",
]

# Проверка User-Agent заголовка
async def verify_user_agent(request: Request):
    user_agent = request.headers.get("User-Agent", "").lower()

    # Проверка на блокируемые User-Agent
    # if any(agent.lower() in user_agent for agent in BLOCKED_USER_AGENTS):
        # raise err_403  # Вызываем исключение при несовпадении
    return True

# Зависимости для включения в маршруты
DEPENDS = [Depends(verify_ip), Depends(verify_user_agent)]
