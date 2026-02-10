# myapp Helm Chart

由 `demo.yaml` 拆分并模板化生成。

## 安装/渲染

```bash
# 渲染查看
helm template myapp ./charts/myapp

# 安装
helm install myapp ./charts/myapp
```

## 可配置 values

- `replicas`：Deployment 副本数（默认 1）
- `image`：镜像地址（默认 `harbor.cuiliangblog.cn/myapp/myapp:v3`）
- `hpa.minReplicas` / `hpa.maxReplicas`：HPA 最小/最大副本（默认 1/5）
- `ingressroute.match`：IngressRoute 路由匹配（默认 `Host(\`myapp.cuiliangblog.cn\`)`）

