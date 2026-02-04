# Claude Code GLM 配置指南

## 配置完成时间
2026-02-04 18:56

## 已配置内容

### 1. GLM 模型配置

Claude Code 现在使用智谱 GLM 模型：

- **Haiku**: `glm-4.5-air`
- **Sonnet**: `glm-4.7` (默认)
- **Opus**: `glm-4.7`

API 端点: `https://open.bigmodel.cn/api/paas/v4`

### 2. MCP 服务器配置

#### 视觉 MCP 服务器 (zai-mcp-server)

**状态**: ✅ 已连接

**功能**:
- `ui_to_artifact` - UI 截图转代码
- `extract_text_from_screenshot` - OCR 文字提取
- `diagnose_error_screenshot` - 错误诊断
- `understand_technical_diagram` - 技术图表理解
- `analyze_data_visualization` - 数据可视化分析
- `ui_diff_check` - UI 差异对比
- `image_analysis` - 通用图像理解
- `video_analysis` - 视频分析

#### 搜索 MCP 服务器 (web-search-prime)

**状态**: ✅ 已连接

**功能**:
- `webSearchPrime` - 网络搜索，返回网页标题、URL、摘要等

### 3. 验证命令

```bash
# 检查 Claude 版本
claude --version

# 检查 MCP 服务器状态
claude mcp list

# 查看当前模型状态
# 在 Claude Code 中输入: /status
```

## 使用示例

### 视觉功能使用

```bash
# 进入你的代码目录
cd /path/to/your/project

# 启动 Claude Code
claude

# 然后可以输入如下命令：
# "分析这个截图：screenshot.png"
# "从这个 UI 截图中生成代码 design.png"
# "提取错误信息 error_screenshot.png"
# "理解这个技术架构图 architecture.png"
```

### 搜索功能使用

```bash
# 在 Claude Code 中直接询问：
# "搜索最新的 AI 技术发展"
# "查找 Python 异步编程最佳实践"
# "查一下今天的市场新闻"
```

### GLM 模型切换

Claude Code 会自动使用 GLM-4.7 模型。如果需要手动切换：

在 `~/.claude.json` 中修改：
```json
{
  "env": {
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-4.7",  // 或其他模型
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-4.7"
  }
}
```

## 配置文件位置

- **配置文件**: `~/.claude.json`
- **API Key**: `e8a520aa939345ae952e38a09fef0f65.zHGQsjOkj0ftd7x0`

## 常见问题

### MCP 服务器无法连接

```bash
# 检查 npx 是否可用
which npx

# 检查网络连接
curl -I https://open.bigmodel.cn

# 重新检查 MCP 状态
claude mcp list
```

### 更新 MCP 服务器

```bash
# 如果需要重新安装视觉 MCP 服务器
claude mcp remove zai-mcp-server
claude mcp add -s user zai-mcp-server --env Z_AI_API_KEY=e8a520aa939345ae952e38a09fef0f65.zHGQsjOkj0ftd7x0 -- npx -y "@z_ai/mcp-server"
```

### 查看 Claude Code 日志

```bash
# 启动调试模式
claude --debug

# 查看详细日志
cat ~/.claude/debug/latest.log
```

## 升级 Claude Code

```bash
# 检查当前版本
claude --version

# 升级到最新版本
claude update
```

## 资源链接

- [Claude Code 官方文档](https://docs.anthropic.com/zh-CN/docs/claude-code/overview)
- [智谱 AI 文档](https://docs.bigmodel.cn/cn/coding-plan/overview)
- [MCP 官方文档](https://modelcontextprotocol.io/)

---

**配置状态**: ✅ 完全就绪
**最后更新**: 2026-02-04
