# 上传到 GitHub 的具体步骤

目标仓库：

```text
https://github.com/pengjingjingjing/CityMind-AI-Research-Assistant
```

## 重要说明

GitHub 网页不会自动解压 ZIP。不要把 ZIP 文件直接上传后期待它变成网站。

请先在电脑上解压本项目，然后上传**解压后的全部文件和文件夹**。

## 方法一：直接覆盖现有仓库

1. 下载并解压修改版 ZIP。
2. 打开现有 GitHub 仓库。
3. 建议先保存旧版本：
   - 点击 **Code → Download ZIP**，备份原仓库；
   - 或新建一个分支 `backup-before-seo-update`。
4. 在仓库中删除旧的 `API.txt`。
5. 点击 **Add file → Upload files**。
6. 把解压后的文件拖入上传区。
7. 注意必须保留这些目录结构：
   - `.streamlit/`
   - `docs/`
   - `docs/articles/`
   - `docs/assets/`
8. Commit message 填写：
   `Reposition CityMind as SEO/GEO content project`
9. 点击 **Commit changes**。

### GitHub 网页可能看不到隐藏文件

`.gitignore`、`.env.example` 和 `.streamlit` 以点开头。某些系统拖拽时容易遗漏。

上传完成后，请在 GitHub 仓库首页检查：

- `.gitignore`
- `.env.example`
- `.streamlit/config.toml`
- `.streamlit/secrets.toml.example`

如果遗漏，可使用 **Add file → Create new file** 单独创建。

## 方法二：新建仓库测试

想保留旧仓库时，可以先新建：

```text
CityMind-SEO-GEO
```

上传并确认正常后，再决定是否替换旧仓库。

注意：如果改了仓库名，`docs` 中的 canonical、GitHub 链接、Sitemap 和 README 链接也要一起修改。

## 发布 GitHub Pages

上传完成后：

1. 打开仓库 **Settings**；
2. 点击左侧 **Pages**；
3. Build and deployment 选择 **Deploy from a branch**；
4. Branch 选择 `main`；
5. Folder 选择 `/docs`；
6. 点击 **Save**。

预期网站地址：

```text
https://pengjingjingjing.github.io/CityMind-AI-Research-Assistant/
```

通常需要等待片刻。GitHub Pages 页面显示绿色部署状态后再访问。

## 更新 Streamlit

在 Streamlit Community Cloud 中：

1. 选择当前 CityMind 应用；
2. 确认 Main file path 为 `app.py`；
3. 打开 **Settings → Secrets**；
4. 添加你重新生成的 API Key；
5. 不要把 Key 写进 GitHub 文件；
6. 重新部署应用；
7. 用无痕窗口测试 Demo 模式和真实 API 模式。

## 上传后检查清单

- GitHub 仓库中不存在 `API.txt`；
- 仓库搜索不到 `sk-` 等密钥片段；
- GitHub Pages 首页能打开；
- 页面内的 Demo 与 GitHub 链接能打开；
- Streamlit 默认 Demo 模式可以直接使用；
- 手机和无痕窗口能够访问；
- README 的三个链接正确；
- `sitemap.xml` 可以访问；
- Search Console 添加网站后再记录真实数据。
