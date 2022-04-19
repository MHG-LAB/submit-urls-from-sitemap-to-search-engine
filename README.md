# submit-urls-from-sitemap-to-search-engine

## 它可以干嘛

提取 sitemap 中的链接，利用百度、必应、谷歌 API **自动**推送至搜索引擎，提升网站收录速度。

## 它要怎么用

请不要 fork 此仓库！！ 使用模板导入 [Use this template](https://github.com/MHG-LAB/submit-urls-from-sitemap-to-search-engine/generate) !! 瞎点fork按钮发送垃圾 PR 将直接提交到 GitHub 黑名单中）

修改 [Actions](https://github.com/MHG-LAB/submit-urls-from-sitemap-to-search-engine/blob/main/.github/workflows/push.yml#L12)

将 `generate.py` 文件中 `site` 的值修改为你的博客地址， `sitemaps` 变量的值修改为你的 sitemap.xml 地址，请确保你的 sitemap 为正常格式。

```py
site = 'https://blog.xxx.cn'
sitemaps = ['/sitemap1.xml','/sitemap2.xml']
```

### 百度

先前往百度资源搜索平台获取 `token`，就是 API 提交中，接口调用地址 `http://data.zz.baidu.com/urls?site=xxx&token=xxx`，`token=` 之后的那一串。

`fork` 本仓库，`Settings > Secrets > new New secret`，`Name` 中填写 `BAIDUTOKEN`，`Value` 即刚刚获取的。（放入 Secrets 中能防止 token 泄露）。再新建一个 secret，`name` 为 `site`，`Value` 为你的博客地址，需要协议头，结尾不能有 `/`

好了，大功告成，接下来每天 GitHub 便会自动帮你推送链接至百度。

#### 配额

每天前 50 个 URL + 随机 50 个 URL

### 必应

前往 <https://www.bing.com/webmasters>，`设置 -> API 访问 -> API 密钥 -> 新建`

`Settings > Secrets > new New secret`，`Name` 中填写 `BINGTOKEN`，`Value` 填入刚刚新建的密钥

#### 配额

每天前 5 个 URL + 随机 5 个 URL

### 谷歌

首先，您需要在 Google Cloud Platform 中设置对 Indexing API 的访问权限 - 按照以下说明进行操作。

https://developers.google.com/search/apis/indexing-api/v3/prereqs

一旦您有权访问索引 API，您就可以下载公钥/私钥对 JSON 文件，其中包含您的所有凭据，并应保存为“service_account.json”。

`Settings > Secrets > new New secret`，`Name` 中填写 `GOOGLE_SERVICE_ACCOUNT`，`Value` 填入刚刚新建的密钥

#### 在 Search Console 中验证网站所有权以提交网址以编制索引

在此步骤中，您将验证您是否可以控制您的网络资产。

要验证您网站的所有权，您需要添加您的服务帐户电子邮件地址（请参阅 service_account.json - client_email）并将其添加为 Search Console 中网络媒体资源的所有者（“委托”）。

您可以在两个地方找到您的服务帐号电子邮件地址：

- 您在创建项目时下载的 JSON 私钥中的 client_email 字段。
- 开发者控制台中服务帐户视图的服务帐户 ID 列。
- 电子邮件地址的格式类似于以下内容：
例如，“ my-service-account@test-project-42.google.com.iam.gserviceaccount.com ”。

然后...

- 1.转到Google 网站管理员中心

- 2.点击您经过验证的资源

- 3.向下滚动并单击“添加所有者”。

- 4.将您的服务帐号电子邮件地址作为资源的所有者添加到该资源中。

#### 配额

每天前 50 个 URL + 随机 50 个 URL

---

Enjoy it!

---
