# 安全提醒

原始压缩包中的 `API.txt` 包含明文 API Key。

修改版已经删除该文件，并且不会把密钥写入代码或 GitHub。

但是，**删除文件并不能让已经暴露的密钥重新安全**。请立即：

1. 登录对应模型/API 服务商控制台；
2. 撤销或删除原密钥；
3. 创建一个新密钥；
4. 检查旧密钥最近的调用记录和费用；
5. 在 Streamlit Community Cloud 的 **App settings → Secrets** 中保存新密钥；
6. 不要将 `.streamlit/secrets.toml`、`.env` 或密钥截图提交到 GitHub。

代码通过以下顺序读取密钥：

1. Streamlit Secrets；
2. 环境变量；
3. 页面中的临时会话输入。

`.gitignore` 已包含：

```text
.env
.streamlit/secrets.toml
```
