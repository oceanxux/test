# QiuChenly 计算数据差值做特征码算法
# 部分网友提供了原始版本 虽然是用的Chatgpt写给我的 但是还是略表谢意
# 提供不定长度的多个十六进制汇编代码段 自动求出差值特征码

data = """
FD 7B BF A9 FD 03 00 91 28 2C 00 90 08 99 45 F9 1F 05 00 B1 A1 00 00 54 28 2C 00 90 00 9D 45 F9 FD 7B C1 A8 1E DB 0C 14 20 2C 00 90 00 C0 2C 91 41 25 00 F0 21 C0 24 91 4B D9 0C 94 F7 FF FF 17 28 2C 00 90 00 95 45 F9 15 DB 0C 14 F6 57 BD A9 F4 4F 01 A9 FD 7B 02 A9 FD 83 00 91 48 2B 00 D0 00 21 41 F9 6B F3 0C 94 FD 03 1D AA 0F DB 0C 94 F3 03 00 AA 9B C3 FF 97 FD 03 1D AA 0B DB 0C 94 F4 03 00 AA 55 27 00 D0 B5 02 08 91 1F 00 00 F1 A2 02 80 9A

FD 7B BF A9 FD 03 00 91 ?? ?? 00 ?? 08 ?? ?? F9 1F 05 00 B1 A1 00 00 54 08 2C 00 D0 00 ?? ?? F9 FD 7B C1 A8 ?? ?? 0C 14 00 2C 00 D0 00 ?? ?? 91 41 25 00 B0 21 C0 21 91 ?? ?? 0C 94 F7 FF FF 17
"""

data1 = []

for i in data.split("\n"):
    if i == "":
        continue
    else:
        data1.append(i)
        if len(data1) > 1:
            res = " ".join(
                [
                    d1 if d1 == d2 else "??"
                    for d1, d2 in zip(data1[0].split(), data1[1].split())
                ]
            )
            data1 = [res]

print(data1[0])
