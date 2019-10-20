import random
import hashlib
import urllib
import http.client
import json
import config


myurl = "/api/trans/vip/translate"

class Translation:
    #获得翻译主类的属性
    #百度云申请的appid和key，可以在config.py中设置
    appid = ""
    secretkey =""

    #翻译的语言选择
    T_from = "auto"
    T_to = "zh"

    myurl = "/api/trans/vip/translate"

    def __init__(self,tFrom,tTo,appId,secretKey):
        self.appid = appId
        self.secretkey = secretKey
        self.T_from = tFrom
        self.T_to = tTo
    #Get the string which need to translate 
    def GetString(self,transString):
        return transString
   
   
    #制作访问API的url
    def MakeSign(self,get_string):
        #获得随机整数
        salt = random.randint(32768, 65536)
        sign = self.appid + get_string + str(salt) + self.secretkey
        #获得MD5编码
        sign = hashlib.md5(sign.encode()).hexdigest()

        #self.myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
#salt) + '&sign=' + sign
        
        #拼接翻译请求的url
        self.myurl = myurl + "?appid=" + str(self.appid) + "&q=" + urllib.parse.quote(get_string) + "&from=" + str(self.T_from) +"&to="+str(self.T_to) +"&salt=" + str(salt) +"&sign=" +sign
        return self.myurl

 
    #翻译请求的client客户端
    def transhttps(self,myurl):
        httpClient = None
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            return result
        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()

    def print_info(self):
        #用来输出调试信息的方法
        print("appid:%s\n" % (self.appid))
        print("url:%s\n" % self.myurl)
        print("secretkey:%s\n" % self.secretkey)



def returnback(tranString):

    tstring = tranString
    #TODO(dhzzy88@163.com):对字符串进行处理，需要优化处理，将字符串中的符号比如‘{’，‘}’，‘，’
    #等标点符号提取出来，在翻译结束后插回相应位置
    if tstring[0] in ["\t","\n","\r","\v"]:
        return tstring

    Trans = Translation("auto","zh",config.appid,config.sercekey)
    url  = Trans.MakeSign(Trans.GetString(tstring))
    result  = Trans.transhttps(url)
    if  result.get("trans_result")!= None :
         returnstring = result.get("trans_result")[0].get("dst")
    else:
         returnstring = ""

    return returnstring
    



if __name__ == "__main__" :

    
    string = "\tdf \t\n"
    print(config.appid,config.sercekey)
    #Trans = Translation("en","zh",config.appid,config.sercekey)
    #url  = Trans.MakeSign(Trans.GetString(string))
    #result  = Trans.transhttps(url)
    #print(result)
    print(returnback(string))
    #print(result.get("trans_result")[0].get("dst"))
   