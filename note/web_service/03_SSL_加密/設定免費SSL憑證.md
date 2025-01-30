如何在 Porkbun 使用免費 SSL 憑證（Let's Encrypt）：
如果你不想支付 SSL 憑證的費用，可以通過以下方式在 Porkbun 網域上啟用免費的 Let's Encrypt SSL：

## 使用 Cloudflare
將 Porkbun 的 DNS 記錄指向 Cloudflare，然後啟用 Cloudflare 提供的免費 SSL 憑證。

Cloudflare 支持全域名級別的 HTTPS，並且自動處理 SSL 憑證的續期。
手動設置 Let's Encrypt
如果你有自己的伺服器，可以使用 Let's Encrypt 的工具（例如 Certbot）來生成免費的 SSL 憑證。
在生成憑證後，將其安裝在你的伺服器或托管服務中。

## 驗證層級
使用 Domain Validation (DV) 憑證，僅驗證你擁有該網域。