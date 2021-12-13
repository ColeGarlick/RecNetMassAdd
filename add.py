import aiohttp
import asyncio
from recnetlogin import login_to_recnet
USER = ''
PASS = ''
async def main():
    x = 0
    async with aiohttp.ClientSession() as session:
        ah = {'Authorization' : login_to_recnet(USER,PASS).access_token}
        url = 'https://api.rec.net/api/relationships/v3/'
        for i in range(1, 5000000):
            async with session.post(url+str(i),headers=ah) as resp:
                statusCodeString = str(resp.status)

                if statusCodeString == "200":
                    print('Successfully added ' + str(x) + ' players!')
                    x = x+1

asyncio.run(main())
