# aiohttp-demo
Демонстрация работы асинхронного кода на примере aiohttp
## Как запустить:
Для запуска либо прописать 
```bash
# Установка зависимостей
$ pip install -r requirements.txt

# Запуск сервера
$ uvicorn dummy:app

# Либо 
$ chmod +x run_server.sh
$ ./run_server.sh

# Далее запуск самого скрипта в другом терминале (!!!)
$ python asynchro.py