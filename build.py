import os
import json
import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    # 打开文件以读取字节
    with open(file_path, "rb") as f:
        # 读取并更新哈希字符串值
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    # 返回SHA-256哈希值的十六进制表示
    return sha256_hash.hexdigest()

# 脚本路径
basePath = os.path.dirname(os.path.abspath(__file__))
# 输入路径
dataPath = basePath+os.sep+'data'+os.sep

fileList = os.listdir(dataPath)
sortedFileList = sorted(fileList)

res = {'providers':{}}
for fileName in sortedFileList:
    with open(dataPath + fileName, 'r', encoding='utf-8') as data_file:
        try:
            jsonobj = json.loads(data_file.read())
            res['providers'].update(jsonobj['providers'])
        except Exception as e:
            print(e)
            
with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(res, outfile, ensure_ascii=False, indent=4)
        
with open('data.hash', 'w', encoding='utf-8') as outfile:
    outfile.write(calculate_sha256('data.json')) 