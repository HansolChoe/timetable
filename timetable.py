import os
import httpx
import asyncio
import dotenv

dotenv.load_dotenv()

async def fetch_cookie(username, password):
    login_url = "https://gw.suresofttech.com/api/login"
    payload = {
        "username": username,
        "password": password,
        "captcha": "",
        "keepLoginStatus": True,
        "returnUrl": "",
    }

    async with httpx.AsyncClient() as client:
        try:
            # 로그인 요청
            response = await client.post(login_url, json=payload, follow_redirects=False)
            response.raise_for_status()

            # Set-Cookie 헤더에서 쿠키 추출
            set_cookie = response.headers.get("set-cookie")
            gosso_cookie = ""
            if set_cookie:
                parts = set_cookie.split(",")
                for part in parts:
                    if part.strip().startswith("GOSSOcookie="):
                        gosso_cookie = part.strip().replace("GOSSOcookie=", "")
                        # print("GOSSOcookie:", gosso_cookie)
            if not gosso_cookie:
                print("GOSSOcookie not found.")
            return gosso_cookie

        except httpx.RequestError as error:
            print("Error fetching cookie:", error)
            return None


async def get_time_table(username, password):
    # 쿠키 가져오기
    cookie = await fetch_cookie(username, password)
    if not cookie:
        print("Failed to retrieve cookie.")
        return

    api_url = "https://gw.suresofttech.com/api/ehr/timeline/month"
    headers = {
        "Cookie": f"GOSSOcookie={cookie}",
    }

    async with httpx.AsyncClient() as client:
        try:
            # API 요청
            response = await client.get(api_url, headers=headers)
            response.raise_for_status()
            dailyList = response.json()['standardWeek']['dailyList']
            for daily in dailyList:
                print(daily)
            response.content

        except httpx.RequestError as error:
            print("Error fetching data with cookie:", error)


if __name__ == "__main__":
    username = os.getenv("ID","")
    password = os.getenv("PASSWORD", "")
    asyncio.run(get_time_table(username, password))
