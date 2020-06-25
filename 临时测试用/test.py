from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.vod.v20180717 import vod_client, models 
try: 
    cred = credential.Credential("AKIDoRowpfXeXFivwijCBSVbS3asLZbQgIK5", "g6aooYCdp68WeW2IRJyNYUAtNo0xudJl") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "vod.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = vod_client.VodClient(cred, "ap-chongqing", clientProfile) 

    req = models.DescribeMediaInfosRequest()
    params = '{"FileIds":["5285890800386497677"]}'
    req.from_json_string(params)

    resp = client.DescribeMediaInfos(req) 
    print(resp.to_json_string()) 

except TencentCloudSDKException as err: 
    print(err) 