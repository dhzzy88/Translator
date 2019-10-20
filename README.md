### 文献翻译初测版本

#### 依赖的库：python-docx,urllib等，使用前请安装

#### 使用方法：

<p>在百度翻译api中申请开发者，将申请的appid和key赋值给config中的变量中，在config.py中将需要翻译的文献的完整路径赋值给path

```python

#请将在百度翻译开发平台上申请的appid和key粘贴在下面的变量中
appid = "20190116000257169"
sercekey = "uOVITuz1JBG3b5iWpg_v"
#将需要翻译的文件路径赋值给path变量，也可以使用PaperTranslator的对象的Setpath方法设置路径
path = "c:\\Users\\zhaozhiyi\\Desktop\\woo03.docx"

```

<p>然后在cmd中使用
  
```
python PaperTranslator.py
```
#### 关于文件结构
<p> ClassDocument.py是文档处理模块，主要读取文献格式以及处理新文档的格式设置
<p> BaiduTranslation.py是百度翻译api的调用和包装
<p> config.py配置文件
<p> PaperTranslator.py 文献翻译主类以及实例化
  
### TODO：
1. 后续将加入其他翻译平台api（使用模块化，加入新平台比较容易）
2. 需要在翻译字符中进行优化，如：不传标点符号给api，调用结束后重新将标点符
3. 后续加入简单的GUI界面，更加方便使用
4. 文档格式优化问题

#### note:
1. 由于百度翻译api对调用频率有限制，因此每次调用使用了time.sleep(1)设置了一秒钟的等待，不能超过1次/秒
2. 长度过长的文献可能会出现访问超时问题，建议将翻译前的文档删除不必要的部分，比如文献引用

#### 关于申明
1. 本程序翻译结果仅供参阅，了解速览等使用，不代表结果的准确性
2. 希望大家在使用过程中尊重文献作者，不要歪曲或者传播本程序的处理文档

#### 招募
1. 大家可能有更好的想法想整合进来，敬请·联系我dhzz88@163.com
2. 关于其他建议的翻译平台可以通过邮件告知我，我尽力将推荐平台的api调用加入进来
3. 可以git clone或者直接下载zip在本页面
