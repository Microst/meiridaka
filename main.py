import requests

_0x3a2b = [
    {"name": "我喜欢你", "namo": "9be4b894bfc35d3d98b48dce4d9a2656"},
    {"name": "枝两声", "namo": "0edfb14abd40d0e21edb1b9f7a68d850"},
    
    {"name": "和我在一起吧", "namo": "08d49590c20a11de4a02fc68a0a12f12"}
]

_0x5d7c = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 22081212C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.54 Mobile Safari/537.36 aweme/32.9.0 ToutiaoMicroApp/3.56.0 PluginVersion/32909009",
    "Content-Type": "application/json"
}

_0x8e1f = {
    "RecordId": "",
    "FormId": "TsAbb",
    "Number": 0,
    "RecordValues": [{"FieldId": "nAuxJ1", "Values": [], "Texts": ["I like you"], "HasValue": True}],
    "DateTarget": "",
    "IsNeedManualAudit": False,
    "MinuteTarget": -1,
    "IsNameNumberConfirm": False,
    "IsFillCheckIn": False
}

def _0xa3e9(_0xc4d2, _0xb7f1):
    _0xd3a6 = "https://ma5-normal-hl.zijieapi.com/api/apps/v3/login?appid=ttdd1daba04217a5b001&aid=1128"
    _0xe9b4 = {"X-Tma-Host-Sessionid": _0xc4d2}
    _0xf2c7 = requests.get(_0xd3a6, headers=_0xe9b4)
    _0xa1d8 = _0xf2c7.json()
    if _0xa1d8.get("err_no") != 0:
        raise Exception(f"{_0xb7f1}登录请求失败: {_0xa1d8.get('err_tips')}")
    _0xc9e3 = _0xa1d8["data"]["code"]
    print(f"成功获取{_0xb7f1}的code: {_0xc9e3}")
    _0xd8f1 = f"https://dy-api.jielong.com/api/User/Token?code={_0xc9e3}"
    _0xe4a2 = requests.get(_0xd8f1)
    _0xb5c7 = _0xe4a2.json()
    if _0xb5c7.get("Type") != "000001":
        raise Exception(f"{_0xb7f1} Token请求失败: {_0xb5c7.get('Description')}")
    _0xf9d3 = _0xb5c7["Data"]["Token"]
    print(f"成功获取{_0xb7f1}的Token: {_0xf9d3}")
    return _0xf9d3

def _0xb2d4(_0xc8e6):
    _0xa7f5 = "https://dy-api.jielong.com/api/CheckIn/EditRecord"
    for _0xd9b1 in _0xc8e6:
        _0xe3a8 = {**_0x5d7c, "authorization": _0xd9b1["authorization"]}
        _0xf4c2 = {**_0x8e1f, "Signature": _0xd9b1["name"]}
        _0xb6d9 = requests.post(_0xa7f5, headers=_0xe3a8, json=_0xf4c2)
        _0xc5e1 = _0xb6d9.json()
        if _0xc5e1.get("Type") == "000001":
            print(f"{_0xd9b1['name']} 签到成功")
        else:
            print(f"{_0xd9b1['name']} 签到失败: {_0xc5e1.get('Description', '未知错误')}")
        print(f"详细响应: {_0xb6d9.text}")

def _0xd3f8():
    try:
        _0xe7a2 = _0x3a2b.copy()
        for _0xf9b1 in _0xe7a2:
            _0xa8d3 = _0xa3e9(_0xf9b1["namo"], _0xf9b1["name"])
            _0xf9b1["authorization"] = f"Bearer {_0xa8d3}"
        _0xb2d4(_0xe7a2)
        print("\n所有用户签到请求已发送完成!")
    except Exception as _0xe4c7:
        print(f"程序执行出错: {_0xe4c7}")

if __name__ == "__main__":
    _0xd3f8()
