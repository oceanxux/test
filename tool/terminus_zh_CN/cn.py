import os
from os import path, read


def decompressAsar():
    cmd = "asar extract /Applications/Termius\ Beta.app/Contents/Resources/app.asar /Applications/Termius\ Beta.app/Contents/Resources/app"
    os.system(cmd)


def pack2asar():
    cmd = 'asar p /Applications/Termius\ Beta.app/Contents/Resources/app /Applications/Termius\ Beta.app/Contents/Resources/app.asar --unpack-dir "{node_modules/@termius,out}"'
    os.system(cmd)


files: list[str] = []

files_cache: dict[str:str] = {}


def main():
    if not path.exists("/Applications/Termius Beta.app/Contents/Resources/app"):
        decompressAsar()

    # read chinese
    bg_progress = ""
    ui_progress = ""
    cnLang: list[str] = []

    with open("lang.txt") as lang:
        cnLang = [ll for ll in lang.read().splitlines() if len(ll) > 0]

    prefixLink = "/Applications/Termius Beta.app/Contents/Resources/app/js"
    lstFile = [prefixLink + "/" + ls for ls in os.listdir(prefixLink)]

    for file in lstFile:
        if path.exists(file):
            with open(file) as lang:
                files_cache[file] = lang.read()

    for lang in cnLang:
        mKey, mValue = lang.split("|")

        lastFile = ""
        for cache in files_cache:
            fileContent = files_cache[cache]
            inx = fileContent.find(mKey)
            if inx == -1:
                if lastFile != mKey:
                    lastFile = mKey
                    print("找不到", cache, mKey, mValue)
                continue
            else:
                print("替换了", cache, mKey, mValue)
                fileContent = fileContent.replace(mKey, mValue)
                files_cache[cache] = fileContent

    for fileOut in files_cache:
        with open(fileOut, "w", encoding="utf-8") as u:
            u.write(files_cache[fileOut])
    pack2asar()


os.system(
    "cp /Applications/Termius\ Beta.app/Contents/Resources/app.asar_副本 /Applications/Termius\ Beta.app/Contents/Resources/app.asar"
)
os.system("rm -rf /Applications/Termius\ Beta.app/Contents/Resources/app")
main()
