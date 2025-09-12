import requests

url = "https://dy-api.jielong.com/api/CheckIn/EditRecord"

# 用户配置列表
users = [
    {
        "name": "Coco",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb0NvIiwidW5pb25JZCI6IjNiZjNiMzE2LWM2MTYtNTFkNC1hM2VmLTI3NTY0YzA1ZWRhNCIsImlkIjo0MzIzMDgyOTQxNTczLCJkYXRlQ3JlYXRlZCI6IjIwMjUtMDktMTJUMTM6Mzg6MTQuMTcyMzM0OCswODowMCIsImlzcyI6ImFwaS5qaWVsb25nLmNvIiwiYXVkIjoiY2xpZW50LmppZWxvbmcuY28iLCJpYXQiOjE3NTc2NTU0OTQsImV4cCI6MTc1NzkxNDY5NH0.77bjejpmaxZekBrR8XgPG7Byvm1P4exDi5fnty1kZao"
    },
    {
        "name": "枝两声",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiLmnp3kuKTlo7Dwn4y_IiwidW5pb25JZCI6IjgxMmEzYjU4LTExNDgtNTBmOC1hYTQ0LTM1NThiNjhhNDRjZCIsImlkIjo0MzIzMTI1MTY3Mzk0LCJkYXRlQ3JlYXRlZCI6IjIwMjUtMDktMTJUMTQ6NDg6MzYuNzU1ODAxKzA4OjAwIiwiaXNzIjoiYXBpLmppZWxvbmcuY28iLCJhdWQiOiJjbGllbnQuamllbG9uZy5jbyIsImlhdCI6MTc1NzY1OTcxNiwiZXhwIjoxNzU3OTE4OTE2fQ.X_b1Z_cK15INiIvZOixNQPlJGg5d9foHoHWRguYpSIY"
    }
]

# 公共请求头和请求体模板
common_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 22081212C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.54 Mobile Safari/537.36 aweme/32.9.0 ToutiaoMicroApp/3.56.0 PluginVersion/32909009",
    "Content-Type": "application/json"
}

data_template = {
    "RecordId": "",
    "FormId": "TsAbb",
    "Number": 0,
    "RecordValues": [
        {
            "FieldId": "nAuxJ1",
            "Values": [],
            "Texts": ["I like you"],
            "HasValue": True
        }
    ],
    "DateTarget": "",
    "IsNeedManualAudit": False,
    "MinuteTarget": -1,
    "IsNameNumberConfirm": False,
    "IsFillCheckIn": False
}

# 为每个用户发送请求
for user in users:
    # 准备特定用户的请求头和请求体
    headers = {**common_headers, "authorization": user["authorization"]}
    data = {**data_template, "Signature": user["name"]}
    
    # 发送请求
    response = requests.post(url, headers=headers, json=data)
    print(f"{user['name']} Response: {response.text}")
