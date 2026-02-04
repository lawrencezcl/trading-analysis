#!/bin/bash
# Claude Code + GLM MCP 配置验证脚本

echo "========================================"
echo "Claude Code + GLM MCP 配置验证"
echo "========================================"
echo ""

echo "1. 检查 Claude Code 版本..."
claude --version
if [ $? -eq 0 ]; then
    echo "✅ Claude Code 已安装"
else
    echo "❌ Claude Code 未安装或无法访问"
    exit 1
fi
echo ""

echo "2. 检查 MCP 服务器状态..."
claude mcp list
if [ $? -eq 0 ]; then
    echo "✅ MCP 服务器检查完成"
else
    echo "❌ MCP 服务器检查失败"
    exit 1
fi
echo ""

echo "3. 检查配置文件..."
if [ -f ~/.claude.json ]; then
    echo "✅ 配置文件存在: ~/.claude.json"
    
    # 检查 GLM 配置
    if grep -q "glm-4.7" ~/.claude.json; then
        echo "✅ GLM 模型配置正确"
    else
        echo "⚠️  GLM 模型配置可能有问题"
    fi
    
    # 检查 MCP 配置
    if grep -q "mcpServers" ~/.claude.json; then
        echo "✅ MCP 服务器配置存在"
        
        if grep -q "zai-mcp-server" ~/.claude.json; then
            echo "✅ 视觉 MCP 服务器已配置"
        fi
        
        if grep -q "web-search-prime" ~/.claude.json; then
            echo "✅ 搜索 MCP 服务器已配置"
        fi
    else
        echo "⚠️  MCP 服务器配置缺失"
    fi
else
    echo "❌ 配置文件不存在"
    exit 1
fi
echo ""

echo "4. 检查 Node.js 和 npx..."
if command -v npx &> /dev/null; then
    echo "✅ npx 可用: $(npx --version)"
else
    echo "❌ npx 不可用（视觉 MCP 服务器需要）"
fi
echo ""

echo "========================================"
echo "配置验证完成"
echo "========================================"
echo ""
echo "下一步："
echo "  1. 进入你的项目目录: cd /path/to/project"
echo "  2. 启动 Claude Code: claude"
echo "  3. 在 Claude Code 中输入: /status"
echo ""
echo "测试 MCP 功能："
echo "  - 视觉: 提供图片文件，说'分析这个图片'"
echo "  - 搜索: 说'搜索最新的 AI 新闻'"
echo ""
