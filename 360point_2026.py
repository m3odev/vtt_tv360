import requests

class TV360:
    def __init__(self):
        self.session = requests.Session()

        self.headers = {
            "lang": "vi",
            "User-Agent": "TV360/5 CFNetwork/3860.300.31 Darwin/25.2.0",
            "tz": "Asia/Ho_Chi_Minh",
            "devicetype": "WEB_IPHONE",
            "deviceName": "iPhone 15 Pro Max",
            "deviceid": "D159607B-0387-40DC-B102-5AE70B16A0F4",
            "devicedrmid": "T4YnFo+fjrcPYUihH209tmBE5IQ=",
            "osappversion": "5.6.2",
            "sessionid": "61AA090A-BE1E-4A16-96D0-E56E75D0FDC5",
            "zoneid": "1",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "osapptype": "IOS",
            "tv360transid": "1771131577_D159607B-0387-40DC-B102-5AE70B16A0F4",
        }

        self.device_info = {
            "osType": "IOS",
            "deviceId": "D159607B-0387-40DC-B102-5AE70B16A0F4",
            "deviceDrmId": "T4YnFo+fjrcPYUihH209tmBE5IQ=",
            "deviceName": "iPhone 15 Pro Max",
            "deviceType": "WEB_IPHONE",
            "osVersion": "26.2.1",
            "screenSize": "1290x2796"
        }

        self.token = None

    def login_with_4g(self):
        url = "http://api.tv360.vn/public/v1/auth/auto-login-http"

        payload = {
            "osappversion": "5.6.2",
            "devicedrmid": self.device_info["deviceDrmId"],
            "deviceid": self.device_info["deviceId"],
            "osapptype": "IOS",
            "osVersion": "26.2.1",
            "deviceName": "iPhone 15 Pro Max",
            "deviceType": "WEB_IPHONE",
            "deviceInfo": self.device_info,
            "screenSize": "1290x2796"
        }

        r = self.session.post(
            url,
            json=payload,
            headers=self.headers,
            timeout=5
        )

        print("Login status:", r.status_code)
        print("Cookies:", self.session.cookies.get_dict())

        if r.ok:
            result = r.json()
            print("Login result:", result)
            self.token = result.get("data", {}).get("accessToken")

    def mov_website(self):
        url = f"https://game-mov.tv360.vn/?token={self.token}"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {self.token}",
            "Referer": f"https://game-mov.tv360.vn/?token={self.token}"
        }
        result = self.session.get(url,
            headers=headers,
            timeout=5
        )
    def receiver_lucky_money(self):
        if not self.token:
            raise RuntimeError("Chưa login hoặc không có token")

        url = "https://game-mov.tv360.vn/api/f/receiver-lucky-money"

        headers = {
            **self.headers,
            "Authorization": f"Bearer {self.token}",
            "Referer": f"https://game-mov.tv360.vn/?token={self.token}"
        }

        r = self.session.post(
            url,
            headers=headers,
            timeout=5
        )

        print("Lucky status:", r.status_code)
        print(r.text)


if __name__ == "__main__":
    vtt = TV360()
    vtt.login_with_4g()
    vtt.mov_website()
    vtt.receiver_lucky_money()
