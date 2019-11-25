# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag
from ..scripts import registFileInfo
from qiniu import BucketManager


def active():
    filesInfo = registFileInfo.active(True)
    print(filesInfo)
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'fWDyTnj2bvRZNmlsZR9kLdfMtjswThPFGWXjbdoR'
    secret_key = 'ni4xK_1xCPGchgnr0HkDQi0B50xY3a8opyx3qHf5'
    # 要上传的空间
    bucket_name = 'afrss'
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)

    for i in range(len(filesInfo)):
        filename = filesInfo[i][1]
        ret, info = bucket.stat(bucket_name, filename)
        if filename!="filesInfo.json" and (str(ret) != "None"):
            print("file exists")
            continue
        if filename == "filesInfo.json":
            ret,info = bucket.delete(bucket_name, filename)
            print(ret)
            print(info)

        #上传后保存的文件名
        key = filename
        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)
        #要上传文件的本地路径
        localfile =filesInfo[i][0]+ '/'+filename
        print("Begin uploading file")
        ret, info = put_file(token, key, localfile)
        print("Upload file finished")
        print(info)
        assert ret['key'] == key
        assert ret['hash'] == etag(localfile)
# active()


