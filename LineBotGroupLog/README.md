# Line Bot Group Log

## 使用方法
1. 進去 [Line develpo](https://developers.line.biz/en/) 官網，然後登入Line帳號。
   1. Create a new provider
   
   ![img.png](demo_images/img.png)
   2. Create a Messaging API channel 
   
   ![img_1.png](demo_images/img_1.png)
   3. Company or owner's country or region
   
   ![img_2.png](demo_images/img_2.png)
   4. Channel name、Channel description、Category、Subcategory
   
   ![img_3.png](demo_images/img_3.png)
   5. I have read and agree to the LINE Official Account Terms of Use 、I have read and agree to the LINE Official Account API Terms of Use 
   
   ![img_4.png](demo_images/img_4.png)
 
2. TOP > new provider > Channel name > Messaging API > LINE Official Account features

![img_6.png](demo_images/img_6.png)

3. TOP > new provider > Channel name > Messaging API > Channel access token 

設定 config.ini 
![img_7.png](demo_images/img_7.png)

4. 下載 ngrok

https://ngrok.com/

5. TOP > new provider > Channel name > Messaging API > Webhook settings

產生 webhook 並貼上
```
ngrok http 5000
```
![img_8.png](demo_images/img_8.png)

6. 運行 main.py