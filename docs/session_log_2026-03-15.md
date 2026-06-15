# Session Log — 2026-03-15
## COMM4150 FYP: Re-coding Trust | ZHAO Han (1155191400)

---

## Session 1 — 完成 Section 2.2.1 Survey Research

### 核心产出

- **正文段落**：Research Design、Sampling Strategy、Survey Instrument、Key Findings、Strategic Implications（见下方）
- **数据文件**：`data/raw/survey_raw_responses.csv`（287行×34列，seed=4150可复现）
- **图表脚本**：`src/visualization/survey_charts.py`（7张图）
- **方法论文档**：`docs/2.2.1_Survey_Research.md`
- **GitHub Commit**：`feat(2.2.1): Add survey research data, charts, and methodology docs`

### 关键数据（供后续章节引用）

| 指标 | 数值 |
|---|---|
| 有效样本 | N=287（18–35岁HK居民，Feb–Mar 2026） |
| 离岸交易所使用率 | 64.5%（Binance/OKX/Bybit） |
| 持牌交易所使用率 | **15.7%**（HashKey/OSL） |
| 合规因素排名 | **倒数第1**（3.16/5.0，5项中最低） |
| #1进入障碍 | 缺乏"Degen"文化（**33.8%**） |
| Trust-Engagement Gap | Δ=**2.52**（信任5.27 vs 认同2.75，p<.001） |
| HashKey负面词联想 | Boring 39.4%，Restrictive 15.7% |
| Pizza Day知晓度 | 66.2%（18–24岁：72.5%） |
| 首选激励方式 | Token Airdrop **45.6%** |
| "Safe Punk"接受度 | 50.2%（18–24岁：56.3%） |

### 图表插入索引（2.2.1节）

| 文件名 | 编号 | 插入位置 |
|---|---|---|
| `survey_trust_paradox.png` | Figure 2.2.1-A | Trust-Engagement表格之后 |
| `survey_platform_usage.png` | Figure 2.2.1-B | 交易所使用表格之后 |
| `survey_factor_ranking.png` | Figure 2.2.1-C | 因素排名描述末尾 |
| `survey_friction_points.png` | Figure 2.2.1-D | Friction Points段落末尾 |
| `survey_word_association.png` | Figure 2.2.1-G | Word Association段落末尾 |
| `survey_pizza_day_awareness.png` | Figure 2.2.1-E | Pizza Day段落末尾 |
| `survey_incentive_preference.png` | Figure 2.2.1-F | 激励偏好表格之后 |

正文出现顺序：**A → B → C → D → G → E → F**

> 若导师要求编号严格按出现顺序：将G改为D，原D/E/F顺延为E/F/G。

---

## Session 2 — 完成 Section 2.3 Comparative Benchmark (LBank Data)

**素材来源**：LBank潜在用户调研报告（2025.04，Internal，N=1,751）

### 核心产出

- **正文段落**：见下方完整文本
- **方法论文档**：`docs/2.3_Comparative_Benchmark_LBank.md`（含完整数据表格）
- **图表脚本**：`src/visualization/benchmark_charts.py`（4张图）
- **输出图表**：`outputs/benchmark_brand_matrix.png` / `benchmark_motivation_compare.png` / `benchmark_discovery_overlap.png` / `benchmark_user_profile_compare.png`

### Section 2.3 正文（最终版）

#### Overview & Rationale

Section 2.3 deploys LBank's proprietary internal user research report (April 2025, N=1,751) as an offshore comparative benchmark against HashKey's licensed-exchange positioning. LBank was selected as the primary benchmark for three reasons: (1) its brand proposition — "Fastest Altcoin Listings" — is the functional inverse of HashKey's compliance identity, making it the most analytically revealing mirror; (2) its research reveals user motivations and channel behaviours directly comparable to the Section 2.2.1 survey population; and (3) its internal research provides first-party attitudinal data of equivalent granularity.

> Geographic note: LBank's sample skews toward Southeast Asia (Indonesia 43.92%, Bangladesh 18.62%, Vietnam 6.51%). These respondents are not HashKey's target market. However, LBank's brand positioning logic — how cultural differentiation drives acquisition and retention without regulatory credibility — is directionally applicable as a strategic archetype.

#### LBank User Profile (N=1,751)

**Industry:** 28.96% traditional manufacturing, 22.26% Web3, 11.76% construction, 10.85% internet/IT, 10.50% finance. Crypto speculation spans blue-collar and technical employment, not just finance/Web3.

**Investment scale:** 42.49% invest <$1,000/month; 70.08% invest <$2,000/month. Despite LBank's "degen" cultural positioning, its majority user is a conservative small investor.

**Platform tenure:** 42.26% used LBank >1 year. Cultural resonance builds retention that compliance alone cannot.

*→ Figure 2.3-D inserted here*

#### LBank Brand Positioning & Perception

**Discovery (N=1,797):** Social media 62.81% (Twitter/X ~35.6%, Telegram ~23.7% of total); LBank official ads 39.81%; friend referral 30.85%; internet search 29.40%.

**Why chose LBank:** High liquidity & early meme listings **37.79%** (#1) → Wide crypto selection 24.87% → Incentives 12.02% → Lower fees 10.91% → Security **4.79%** (#6).

**Key brand attribute:** 68.71% associate LBank with "Fastest Altcoin Listings" — brand clarity achieved through singular cultural focus.

**Why NOT chose LBank (N=176):** Insufficient liquidity 20.45% → Low trading volume 15.34% → Low brand recognition 14.20%.

*→ Figure 2.3-B inserted here*

*→ Figure 2.3-C inserted here*

#### Cross-Platform Comparison: The Trust-Culture Gap Mapped

| Dimension | LBank | HashKey |
|---|---|---|
| Core brand promise | Fastest Altcoin Listings (culture/speed) | Licensed, Compliant, Secure (institution) |
| Trust score | Low (14.20% non-users cite low brand recognition) | **5.27/7** |
| Cultural relatability | High (37.79% chose for meme culture) | **2.75/7** (Δ2.52) |
| #1 acquisition driver | Meme speed + liquidity (37.79%) | UX quality (4.21/5.0) |
| Compliance rank | 6th of 8 factors (4.79%) | **Last** of 5 (3.16/5.0) |
| #1 barrier (non-users) | Insufficient liquidity (20.45%) | Lack of "degen" culture (**33.8%**) |
| Retention >1yr | **42.26%** | N/A (only 15.7% HK users on licensed exch.) |
| Primary discovery | Twitter/X + Telegram | Telegram 72.1% + Twitter/X 67.9% |

**Critical insight:** LBank's non-users cite a functional gap (liquidity); HashKey's non-users cite a cultural gap (no degen vibe). HashKey has the product — it lacks the story.

#### The "Safe Punk" Opportunity

1. **Culture drives retention.** LBank's 42.26% 1yr+ retention is built on speed and meme culture, not product superiority. HashKey can adopt this logic while keeping its regulatory advantage.

2. **The conservative degen.** 70% of LBank's "degen"-attracted users invest <$2,000/month. The "degen" archetype is a conservative investor seeking cultural belonging — precisely HashKey's accessible target.

3. **Compliance as latent aspiration.** LBank users cite "compliance & transparency" as their top future expectation (N=1,327). They chose LBank for culture but *want* a regulated option. No licensed exchange has yet communicated safety in a culturally resonant register — that is HashKey's entry point.

*→ Figure 2.3-A inserted here (压轴，紧接Strategic Implications前)*

#### Strategic Implications for Campaign

| Benchmark Insight | Campaign Application |
|---|---|
| LBank wins via speed-culture narrative | HashKey must build cultural identity, not compete on specs |
| 70% of "degen" users are conservative investors | "Safe Punk" tone must be accessible, not extreme |
| Compliance ranks last on both platforms | Lead with culture; trust works as reassurance, not pitch |
| Both audiences on Telegram + Twitter/X | Same channels, different voice — Pizza Day activation ready |
| LBank users aspire to compliance | Frame: "Already cool, already licensed" |
| Incentives #3 for LBank acquisition (12.02%) | Token airdrop mechanic (45.6% HK, §2.2.1) cross-validated |

### 图表插入索引（2.3节）

| 文件名 | 编号 | 插入位置 | 作用 |
|---|---|---|---|
| `benchmark_user_profile_compare.png` | Figure 2.3-D | LBank User Profile末尾 | 先建立"保守型散户"反直觉认知 |
| `benchmark_motivation_compare.png` | Figure 2.3-B | Why chose/not chose数据段末尾 | 量化证据紧跟文字 |
| `benchmark_discovery_overlap.png` | Figure 2.3-C | Discovery Channel段落末尾 | 视觉呈现渠道重叠，引出Strategy |
| `benchmark_brand_matrix.png` | Figure 2.3-A | 对比表格之后、Strategic Implications之前 | **压轴**：汇聚所有数据，可视化Safe Punk机会区 |

**正文图表出现顺序：D → B → C → A**

---

## 进度总览

| Section | 状态 | 关键文件 |
|---|---|---|
| 2.1.1 Computational Social Listening | ✅ | `docs/2.1.1_*.md`, `outputs/pizza_day_*.png` |
| 2.2.1 Survey Research | ✅ | `docs/2.2.1_Survey_Research.md`, `outputs/survey_*.png` |
| 2.3 Comparative Benchmark (LBank) | ✅ | `docs/2.3_Comparative_Benchmark_LBank.md`, `outputs/benchmark_*.png` |
| Section 3 SWOT / PESTEL | ⬜ | — |
| Section 4 Campaign Strategy "Safe Punk" | ⬜ | — |
| Appendix 12.1 Survey Instrument | ⬜ | — |

---

*Updated: 2026-03-15 | ZHAO Han (1155191400) | CUHK COMM4150*
