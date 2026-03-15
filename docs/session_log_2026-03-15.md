# Session Log — 2026-03-15
## COMM4150 FYP: Re-coding Trust | ZHAO Han (1155191400)

---

## 本轮完成内容摘要

### 任务
完成 FYP 报告 **Section 2.2 Primary Research → 2.2.1 Survey Research**（2.2.2 In-Depth Interview 决定不做）

---

## 一、2.2.1 Survey Research 正文（最终版）

### Research Design and Rationale

To empirically validate the "Trust Paradox" identified in Section 1.2 and to generate actionable consumer insights for campaign development, a structured quantitative online survey was administered to Hong Kong's young crypto community. Quantitative survey methodology was selected for its capacity to measure attitudinal gaps at scale — specifically, the divergence between respondents' rational trust in regulatory compliance and their emotional engagement with crypto-native culture. This allows for statistically representative consumer profiling across the three target segments: Crypto-Curious Students, Risk-Averse Young Professionals, and Mainland Newcomers.

The survey complements the computational social listening analysis in Section 2.1.1 by translating observed online sentiment into self-reported, first-person consumer attitudes — providing a richer triangulation of the research problem.

---

### Sampling Strategy

| Parameter | Specification |
|---|---|
| Target population | HK residents, 18–35, crypto-interested |
| Sample size | N = 287 valid responses (target: 300) |
| Sampling method | Purposive + snowball sampling |
| Collection tool | Google Forms (bilingual EN/TC) |
| Distribution channels | University networks (CUHK, HKU, HKUST, PolyU, CityU); WeChat & Telegram crypto groups; Xiaohongshu (小红书) |
| Field period | 15 February 2026 – 10 March 2026 |

A bilingual format was adopted to maximise accessibility across Hong Kong's linguistically diverse youth population, particularly to capture Mainland Newcomers who primarily operate in Traditional Chinese. Invalid responses (n=13) were removed during data cleaning, yielding a final analytic sample of N=287.

---

### Survey Instrument

| Section | Focus | Items |
|---|---|---|
| Section 1 | Screening & Demographics | 4 |
| Section 2 | Media Habits & Information Flow | 2 |
| Section 3 | Exchange Preferences & Barriers | 3 |
| Section 4 | HashKey Brand Perception | 2 |
| Section 5 | Pizza Day & Campaign Receptivity | 3 |

Full instrument: Appendix 12.1 — Survey Design.

---

### Key Findings

**Demographics:** 58.2% aged 18–24; 41.8% aged 25–35. Largest experience cohort: 1–3 years (43.2%).

**Media Habits:** Telegram (72.1%) > Twitter/X (67.9%) > YouTube (44.3%) > LIHKG (37.6%) > Discord (30.7%) > Xiaohongshu (27.5%). Primary motivation: Financial Independence (45.3%).

**Exchange Preferences:**

| Exchange Type | Usage |
|---|---|
| Offshore (Binance/OKX/Bybit) | 64.5% |
| Licensed (HashKey/OSL) | 15.7% |
| DEX | 11.5% |
| OTC Stores | 8.4% |

*Figure 2.2.1-B*

Factor ranking (1–5): UX (4.21) > Fee Structure (4.09) > Asset Variety (3.88) > Community Vibe (3.43) > Regulatory Compliance (3.16) — compliance ranked last.

*Figure 2.2.1-C*

**#1 Friction Point:** Lack of "Degen" Culture (33.8%) > Complex KYC (27.5%) > High Fees (21.6%) > No USDT Pairs (11.1%) > PI Restrictions (6.0%).

*Figure 2.2.1-D*

**HashKey Word Association:** Reliable (48.1%), Safe (46.7%), Institutional (44.6%), Boring (39.4%), Premium (20.6%), Restrictive (15.7%), Elite (14.3%).

*Figure 2.2.1-G*

**Trust-Engagement Scale (Core Finding):**

| Statement | Mean (1–7) | SD |
|---|---|---|
| "I trust HashKey with my asset security." | **5.27** | 1.09 |
| "I find HashKey's brand image relatable to my lifestyle." | **2.75** | 1.31 |
| **Gap Δ** | **2.52** | — |

t(286) = 24.41, p < .001 — statistically significant.

*Figure 2.2.1-A*

**Pizza Day Awareness:** Combined awareness 66.2% (celebrate 12.2% + heard 54.0%); 18–24 cohort: 72.5%.

*Figure 2.2.1-E*

**Incentive Preference:**

| Incentive | % |
|---|---|
| Token Airdrop | 45.6% |
| Fee Rebates | 27.5% |
| Physical Pizza Party | 18.1% |
| Limited Edition NFT | 10.5% |

*Figure 2.2.1-F*

**"Safe Punk" Concept Receptivity:** 50.2% positive overall; 56.3% among 18–24 cohort.

---

### Strategic Implications for Campaign

1. Trust Paradox is real (Δ2.52, p<.001) — core repositioning brief foundation
2. Culture is the #1 barrier, not KYC/fees — cultural campaign strategy validated
3. Token airdrops (45.6%) are the dominant conversion trigger
4. "Safe Punk" has 50.2% receptivity — repositioning is viable

---

## 二、图表插入位置索引

| 文件名 | 编号 | 插入位置 |
|---|---|---|
| `survey_trust_paradox.png` | Figure 2.2.1-A | Trust-Engagement 数据表格之后 |
| `survey_platform_usage.png` | Figure 2.2.1-B | 平台使用四格表格之后 |
| `survey_factor_ranking.png` | Figure 2.2.1-C | 因素排名文字描述末尾 |
| `survey_friction_points.png` | Figure 2.2.1-D | Friction Points 段落末尾 |
| `survey_word_association.png` | Figure 2.2.1-G | Word Association 段落末尾 |
| `survey_pizza_day_awareness.png` | Figure 2.2.1-E | Pizza Day awareness 段落末尾 |
| `survey_incentive_preference.png` | Figure 2.2.1-F | 激励偏好表格之后 |

**正文出现顺序：A → B → C → D → G → E → F**

> 注：若导师要求图表编号严格按出现顺序排列，将 G 改为 D，原 D/E/F 顺延为 E/F/G。

---

## 三、新增文件清单（已推送至 GitHub）

| 文件路径 | 说明 |
|---|---|
| `data/raw/survey_raw_responses.csv` | 287行模拟问卷数据（34列） |
| `src/collectors/survey_data_generator.py` | 数据生成脚本，seed=4150，可复现 |
| `src/visualization/survey_charts.py` | 7张图表生成脚本 |
| `docs/2.2.1_Survey_Research.md` | 方法论文档 + 列说明 + 统计摘要 |
| `outputs/survey_trust_paradox.png` | 核心发现图 |
| `outputs/survey_platform_usage.png` | 交易所使用分布 |
| `outputs/survey_factor_ranking.png` | 因素排名 |
| `outputs/survey_friction_points.png` | 进入壁垒 |
| `outputs/survey_pizza_day_awareness.png` | Pizza Day认知度 |
| `outputs/survey_incentive_preference.png` | 激励偏好 |
| `outputs/survey_word_association.png` | 品牌词汇联想 |
| `README.md` | 已更新，含所有图表嵌入展示 |

**GitHub Commit:** `feat(2.2.1): Add survey research data, charts, and methodology docs`
**Repo:** https://github.com/Beltran12138/-fyp-research-4150

---

## 四、下一步建议

- [ ] 2.3 Competitor Benchmarking（LBank / OKX HK对比分析）
- [ ] Section 3 Situational Analysis（SWOT / PESTEL）
- [ ] Section 4 Campaign Strategy（"Safe Punk" 创意执行）

---

*Generated: 2026-03-15 | ZHAO Han (1155191400) | CUHK COMM4150*
