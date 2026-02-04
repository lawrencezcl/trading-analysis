#!/usr/bin/env python3
"""
使用智谱GLM-4.7 API进行深度交易分析
不使用subprocess，直接调用API
"""

import requests
import json
from datetime import datetime
import time

# API配置
API_KEY = "e8a520aa939345ae952e38a09fef0f65.zHGQsjOkj0ftd7x0"
BASE_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# 输出文件
OUTPUT_FILE = "/root/.openclaw/workspace/trading-analysis/CLAUDE_ANALYSIS_REPORT.md"

print("=" * 80)
print("智谱GLM-4.7 深度交易分析")
print("=" * 80)
print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"输出文件: {OUTPUT_FILE}")
print("=" * 80)
print()

# 构建提示词
system_prompt = """你是一位世界顶级的交易分析师，拥有30年以上的交易经验，精通以下理论和方法：

1. 威科夫交易法 (Wyckoff Method) - 市场周期四阶段分析
2. 四度空间理论 (Market Profile) - TPO和价值区间分析
3. 技术分析 - 所有主流技术指标（MA、MACD、RSI、ADX、OBV、VWAP等）
4. 期权分析 - PCR、Max Pain、VIX、IV Skew、Options Flow
5. 期货分析 - 升贴水、未平仓合约、期货流向
6. 宏观经济分析 - 美联储政策、经济数据、地缘政治

你的分析特点：
- 深入透彻，不浅尝辄止
- 数据驱动，逻辑严密
- 风险意识强，严格控制风险
- 提供可执行的具体建议
- 使用最大token输出，最详细的推理

请使用你的最大算力和最大token输出进行深度分析。"""

user_prompt = """
请执行以下深度交易分析任务：

## 任务目标
使用威科夫交易法和四度空间理论，结合期权期货数据分析当前标普500（SPX/SPY）和纳斯达克100（NDX/QQQ）指数走势，给出短期交易计划（1-5天）。

## 分析要求

### 1. 威科夫分析
- 识别当前市场处于哪个阶段（Accumulation, Markup, Distribution, Markdown）
- 分析关键信号：Spring, Upthrust, SOS, SOW, Test
- 评估供需关系和 Effort vs Result
- 分析成交量变化

### 2. 四度空间（Market Profile）分析
- 计算价值区间（Value Area High/Low）
- 识别 POC（Point of Control）
- 分析 TPO 分布形态
- 判断交易日类型（Trend Day, Double Distribution, Neutral Day, etc.）

### 3. 多时间框架分析
- **1小时图**: 短期趋势和交易机会
- **4小时图**: 中期趋势确认
- **日线图**: 主要趋势方向
- **周线图**: 长期趋势背景

### 4. 技术指标分析
- **趋势指标**: MA(20,50,200), MACD
- **动能指标**: RSI(14), Stochastic, ADX
- **成交量指标**: OBV, VWAP

### 5. 期权数据
- Put/Call Ratio（PCR）
- 最大痛苦点（Max Pain）
- VIX 隐含波动率
- IV Skew（Put IV vs Call IV）
- 期权流向（大单分析）

### 6. 期货数据
- E-mini S&P 500 (ES) 和 NASDAQ-100 (NQ) 期货
- 期货升贴水
- 未平仓合约（Open Interest）变化

### 7. 市场消息和宏观因素
- 最新市场新闻
- 美联储政策预期
- 经济数据（CPI, PCE, 就业等）
- 地缘政治风险
- 企业盈利季报

### 8. 短期交易计划
**对每个指数（SPX和NDX）分别给出：**

- **观点**: 看多 / 看空 / 中性
- **入场点位**: Entry Price
- **止损位**: Stop Loss
- **目标位1/2/3**: Target Prices
- **风险收益比**: Risk/Reward Ratio
- **建议仓位**: Position Size (% of portfolio)
- **期权策略建议**:（如适用）
- **时间框架**: 1-5天

### 9. 风险管理
- 主要风险因素
- 对冲策略
- 止损执行纪律
- 仓位管理原则

## 输出要求

- 使用最大算力进行深度分析
- 使用最大token输出详细报告（建议8000+ tokens）
- 报告应包含数据表格、清晰的分析逻辑
- 明确说明数据来源、分析局限性、风险提示
- 提供可执行的具体交易建议
- 使用Markdown格式，包含表格、代码块、标题等
- 报告长度应尽可能长，提供最详尽的分析

## 重要提示

- 这只是分析，不构成投资建议
- 市场有风险，投资需谨慎
- 根据可获得的最新数据进行分析
- 明确说明数据来源和分析局限性
- 提供详细的风险提示

开始深度分析吧！请输出最详尽的交易分析报告。
"""

# 构建请求
payload = {
    "model": "glm-4.7",
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    "temperature": 0.3,
    "max_tokens": 8000,
    "stream": False
}

# 发送请求
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("正在发送请求到智谱GLM-4.7...")
print("使用最大token输出（8000 tokens）")
print("这可能需要1-3分钟...")
print()

start_time = time.time()

try:
    response = requests.post(
        BASE_URL,
        headers=headers,
        json=payload,
        timeout=300  # 5分钟超时
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"请求完成，耗时: {elapsed_time:.2f} 秒")
    print(f"响应状态码: {response.status_code}")
    print()

    if response.status_code == 200:
        result = response.json()

        # 提取回复
        content = result['choices'][0]['message']['content']
        usage = result.get('usage', {})

        completion_tokens = usage.get('completion_tokens', 0)
        prompt_tokens = usage.get('prompt_tokens', 0)
        total_tokens = usage.get('total_tokens', 0)

        print("✅ 分析完成！")
        print(f"📊 输出tokens: {completion_tokens}")
        print(f"📊 输入tokens: {prompt_tokens}")
        print(f"📊 总tokens: {total_tokens}")
        print(f"📝 报告长度: {len(content)} 字符")
        print()

        # 保存报告
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ 报告已保存到: {OUTPUT_FILE}")
        print()
        print("=" * 80)
        print("报告预览（前1500字符）:")
        print("=" * 80)
        print(content[:1500])
        print("=" * 80)
        print()
        print("=" * 80)
        print("✅ 深度交易分析完成！")
        print("=" * 80)
        print(f"完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"总耗时: {elapsed_time:.2f} 秒")

    else:
        print(f"❌ 请求失败")
        print(f"状态码: {response.status_code}")
        print(f"错误响应:")
        print(response.text)
        exit(1)

except requests.exceptions.Timeout:
    print("❌ 请求超时（5分钟）")
    exit(1)
except Exception as e:
    print(f"❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
