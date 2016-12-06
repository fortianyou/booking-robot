****

##<center>Booking Robot</center>
##### <center>Author: HouJP_NSD</center>
##### <center>E-mail: houjp1992@gmail.com</center>

****

###目录
*	[项目介绍](#intro)
*	[使用说明](#usage)
*	[版本更新](#version)

****

###<a name="intro">项目介绍</a>

恩，报了东方时尚驾校，发现网上约不到车，so，试试写个脚本来刷单吧。（如果在阿里估计已经被开除了，Orz）

醉了，发现查车也是需要验证码的，所以刷单这个思路行不通。

****

###<a name="usage">使用说明</a>

##### pytesseract安装

因为需要识别验证码的内容，这里借用了pytesseract库进行自动识别，必须先安装其依赖的PIL及tesseract-ocr（tesseract-ocr为google的ocr识别引擎）。

Pillow和pytesseract安装如下：

```
pip install Pillow
brew install tesseract
pip install pytesseract
```

****

###<a name="version">版本更新</a>

*	账号密码及验证码登录功能完成。

****


