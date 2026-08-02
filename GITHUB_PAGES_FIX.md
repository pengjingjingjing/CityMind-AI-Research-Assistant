# GitHub Pages 构建错误修复

## 报错原因

日志出现 `jekyll-theme-primer` 和 `assets/css/style.scss`，说明 GitHub Pages 正在把本项目当作 Jekyll 主题站点构建。本项目已经是纯 HTML + CSS，不需要 Jekyll。

## 正确目录

```text
仓库根目录/
├── app.py
├── README.md
├── docs/
│   ├── .nojekyll
│   ├── index.html
│   ├── how-it-works.html
│   ├── accuracy-and-limitations.html
│   ├── seo-geo-case-study.html
│   ├── assets/
│   │   └── styles.css
│   ├── articles/
│   ├── robots.txt
│   └── sitemap.xml
```

不能只上传 ZIP；不能形成 `docs/docs/index.html`。

## 删除旧 Jekyll 文件

仓库中如有以下文件或目录，请删除：

```text
docs/_config.yml
docs/Gemfile
docs/Gemfile.lock
docs/assets/css/style.scss
docs/_layouts/
docs/_includes/
docs/index.md
.github/workflows/jekyll-gh-pages.yml
```

本项目正确的样式文件是：

```text
docs/assets/styles.css
```

## GitHub Pages 设置

```text
Settings → Pages
Source: Deploy from a branch
Branch: main
Folder: /docs
```

保存后提交一次修改，或在 Actions 中重新运行 Pages build and deployment。

## 手动创建 .nojekyll

若上传后 GitHub 中看不到 `docs/.nojekyll`：

1. 进入仓库；
2. 点击 Add file → Create new file；
3. 文件名填写 `docs/.nojekyll`；
4. 内容填写 `Disable Jekyll`；
5. Commit 到 main 分支。
