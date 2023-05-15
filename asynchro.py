import asyncio
from time import perf_counter

import aiohttp
import requests


# Sync function
def sync(urls):
    for url in urls:
        r = requests.get(f'http://127.0.0.1:8000/items/{url}')

# Creating tasks (task-function)
async def fetch(s, url):
    async with s.get(f'http://127.0.0.1:8000/items/{url}') as r: # Sending GET request in async context mode
        if r.status != 200:
            r.raise_for_status()
        return await r.text()

# Gathering tasks
async def fetch_all(s, urls):
    tasks = [] # Task list init
    for url in urls:
        tasks.append(asyncio.create_task(fetch(s, url))) # Appending taks to task list 
    res = await asyncio.gather(*tasks)
    return res

# Main fuction
async def main():
    urls = range(1, 500)
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session, urls)
        print(htmls)

if __name__ == '__main__':
    start = perf_counter()
    asyncio.run(main())
    # sync(range(1, 500))
    stop = perf_counter()
    print(f'Time: {stop-start}') 