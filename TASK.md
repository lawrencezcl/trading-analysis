# 交易分析任务

## 目标
使用威科夫交易法和四度空间理论，结合期权期货数据分析当前标普500（SPX/SPY）和纳斯达克100（NDX/QQQ）指数走势，给出短期交易计划。

## 分析要求

### 1. 理论框架
- **威科夫交易法**: 识别 Accumulation（积累）、Markup（上涨）、Distribution（派发）、Markdown（下跌）阶段
  - 关键概念: Cause（因）和 Effect（果）、Effort vs Result（努力 vs 结果）
  - 等待关键信号: Springs（弹簧）、Sign of Strength（SOS）、Sign of Weakness（SOW）、Upthrust（向上突破）、Test（测试）

- **四度空间理论 (Market Profile)**:
  - 时间-价格机会分析
  - 识别价值区间（Value Area High/Low）、POC（Point of Control）
  - TPO (Time Price Opportunity) 分布形态
  - 初始平衡、价格区间扩展

### 2. 数据需求
- **实时市场数据**:
  - SPX, NDX 或 SPY, QQQ 当前价格
  - 1小时、4小时、日线、周线图表形态

- **期权数据**:
  - Put/Call Ratio (PCR)
  - 最大未平仓合约 Strike (Max Pain)
  - 隐含波动率 (IV) - VIX, CBOE Indices
  - 期权流向数据（大单异常）

- **期货数据**:
  - E-mini S&P 500 (ES) 和 E-mini NASDAQ-100 (NQ) 期货
  - 期货未平仓合约量变化
  - 期货升贴水（期货 vs 现货价差）

### 3. 技术分析
- **技术指标**:
  - 趋势指标: MA(20,50,200), EMA, MACD
  - 动能指标: RSI, Stochastic, ADX
  - 成交量分析: OBV, VWAP

- **图表形态识别**:
  - 支撑/阻力位
  - 趋势线、通道
  - 头肩形态、双底/双顶、楔形、三角形
  - 缺口（Gaps）

### 4. 市场情绪和宏观因素
- **最新市场消息**: 搜索最新财经新闻
- **美联储政策**: 利率预期、讲话内容
- **经济数据**: CPI, PCE, 就业数据, GDP
- **地缘政治风险**: 影响市场的重大事件

### 5. 输出要求
- **短期交易计划**:
  - 看多/看空/中性观点
  - 具体入场点位（Entry Price）
  - 止损位（Stop Loss）
  - 目标位（Target Price）
  - 风险收益比（Risk/Reward Ratio）
  - 期权策略建议（如适用）
  - 仓位管理建议

- **分析报告**:
  - 威科夫阶段分析（当前处于哪个阶段）
  - 四度空间价值区间分析
  - 关键支撑/阻力位
  - 风险因素和应对措施

### 6. 执行指令
使用最大算力，最大 token 输出。提供最详尽的分析。

---

## 注意事项
- 这只是市场分析，不构成投资建议
- 交易有风险，请自行评估
- 实时数据获取可能需要 API 调用
- 如果无法获取实时数据，使用最新可用的数据并说明
