# Section 9 — Measurement & Evaluation Framework
## COMM4150 FYP: Re-coding Trust | ZHAO Han (1155191400)

---

## 9.1 Evaluation Architecture

Colley's (1961) DAGMAR framework establishes that advertising objectives must be measurable against a defined baseline, within a fixed time period, to allow systematic evaluation of communications performance. The thirteen objectives defined in Section 4.4 are each written to this standard — baseline established, target specified, deadline fixed, measurement instrument identified. This section specifies the infrastructure, methodology, and procedures through which those thirteen objectives will be evaluated.

Schultz and Schultz (2004) argue that IMC evaluation must extend beyond immediate campaign metrics to assess whether the campaign has produced durable changes in brand relationships — specifically, whether converted users exhibit sustained behavioural engagement rather than transactional one-off responses. The evaluation framework is therefore structured across two measurement horizons: a **real-time operational layer** (tracking campaign mechanics as they execute) and a **post-campaign outcome layer** (measuring brand health shifts after the campaign concludes).

The framework consolidates what were previously conceived as separate KPI (Section 4.7) and evaluation (Section 9) components into a single integrated measurement architecture. This reflects the evaluative logic of integrated campaigns: awareness, engagement, and conversion metrics are not independent silos but points on a single conversion journey, and their evaluation must be structured to trace audience movement across the full funnel rather than optimising individual metrics in isolation.

---

## 9.2 Measurement Infrastructure

Four measurement instruments will be deployed across the campaign window:

### 9.2.1 Platform Analytics (Real-Time)

| Platform | Tool | Metrics Captured |
|---|---|---|
| X/Twitter @HashKeyExchange | Twitter Analytics + Brandwatch social listening | Impressions, reach, engagement rate, quote-tweet volume, RIB thread reply count, "Still Here" thread amplification |
| Telegram @HashKey0xU | Telegram channel analytics | Member count, daily active users, message reactions, forward rate, /confess submission count |
| Laszlo Bot | Custom bot analytics dashboard | Unique session count, session depth (exchanges per session), /confess submissions, quiz completion rate, KYC redirect clicks |
| hashkey.com/hkx | Google Analytics 4 + UTM tracking | Unique visitors, developer onboarding conversions, CLI downloads, referral source breakdown |

### 9.2.2 Campaign UTM / QR Attribution

All offline-to-online conversion pathways are instrumented with unique tracking parameters:

| Conversion Source | Tracking Method | Objective Attributed |
|---|---|---|
| OOH QR codes (MTR, CWB, SSP) | QR scan → unique UTM landing page | C2 (net-new registrations) |
| KOL post links | Individual UTM per KOL partner | C2 (net-new registrations); A1 (reach verification) |
| Pizza Day event QR kiosks | Event-specific QR → KYC flow | C1 (airdrop-eligible accounts) |
| TG /confess → KYC CTA | Bot session ID → account registration | C1 and C2 (attributed registrations) |

### 9.2.3 Mid-Campaign Pulse Survey (April 2026)

**Design:** N≥100, online panel, same demographic screening as Section 2.2.2 (HK crypto-interested, 18–35). Administered in April 2026, after Phase 1 community formation mechanics are active but before the Pizza Day conversion moment.

**Purpose:** Measure progress toward awareness objectives (A2, A3) at midpoint; enable course correction if awareness targets are tracking below pace.

**Instruments:**
- Unaided HashKey × Bitcoin Pizza Day brand association (Objective A2)
- "Safe Punk" aided recall (Objective A3 — show visual/descriptor, measure recognition)
- Top-of-mind crypto exchange brand associations (competitive context)
- Laszlo Bot awareness and interaction (proxy for Objective E3)

### 9.2.4 Post-Campaign Tracking Survey (July 2026)

**Design:** N≥287, same screening as Section 2.2.2, same instrument as baseline survey. Administered in July 2026 to allow adequate time for brand memory consolidation after the May 22 peak event.

**Purpose:** Measure all primary (P1–P4) and awareness (A3) objectives. This is the definitive instrument for evaluating campaign success against the strategic mandate.

**Core Battery (mirroring Section 2.2.4 baseline):**
1. Brand trust scale (same 7-point items as baseline; produces Asset Security Trust score)
2. Brand relatability scale (same 7-point items; produces Brand Relatability score)
3. Brand word association (open-ended then prompted; measures "Boring" association rate)
4. "Safe Punk" concept recognition (aided)
5. HashKey × Bitcoin Pizza Day association (unaided)
6. Exchange usage and intent (competitive context)

The Trust-Engagement Gap (Δ) is calculated as: Δ = Asset Security Trust score − Brand Relatability score. Target: Δ ≤ 1.75 (from baseline Δ = 2.52; *t*(286) = 18.73, *p* < .001; Section 2.2.4).

---

### 9.2.5 Measurement Calendar

| Instrument | Period | Objectives covered |
|---|---|---|
| Platform analytics (X/Twitter, Telegram, Bot, GA4) | Daily: Feb 1 – Jun 30 | A1, E1, E2, E3, C1, C2 |
| UTM / QR attribution tracking | Continuous: Feb 1 – Jun 30 | C2 |
| Go/No-Go Gate 1 review | Mar 28 | Leading indicators for A1, E1, E2 |
| Mid-campaign pulse survey (N≥100) | Apr 15–30 | A2, A3 (interim) |
| Go/No-Go Gate 2 review | May 14 | C1, E1 + logistics readiness |
| Post-event qualitative interviews (N=10–15) | May 23 – Jun 7 | Q1–Q4 |
| 30-day retention measurement (C3) | Jun 22 | C3 |
| Post-campaign tracking survey (N≥287) | Jul 1–14 | P1, P2, P3, P4, A3 |
| Evaluation report | Jul 31 | All objectives |

---

## 9.3 Quantitative KPI Dashboard

### Campaign Verdict Criteria

The campaign is declared a **strategic success** if all three of the following conditions are simultaneously met:

| # | Condition | Rationale |
|---|---|---|
| 1 | **P1 met:** Trust-Engagement Gap Δ ≤ 1.75 | Primary strategic objective — the gap must narrow for repositioning to be evidenced |
| 2 | **C1 met:** KYC-verified airdrop accounts ≥ 10,001 | Primary conversion objective — community formation must translate to measurable acquisition |
| 3 | **P3 not breached:** Asset Security Trust M ≥ 5.00 | Floor constraint — Safe Punk positioning must not erode the trust advantage that is HashKey's sole existing brand equity |

Meeting P1 and C1 while breaching P3 constitutes a **partial success with strategic risk**: the campaign acquired users but damaged the compliance credibility on which the brand's positioning depends. Meeting only C1 (conversion without repositioning) constitutes a **tactical success but strategic failure**: the campaign function as an acquisition promotion rather than a cultural repositioning.

All thirteen objectives are tracked below. The three verdict conditions above take precedence in any overall campaign assessment.

---

All thirteen campaign objectives (Section 4.4.6) are measured against defined targets by the deadlines specified:

| Code | Category | Objective | Baseline | Target | Deadline | Measurement Instrument |
|---|---|---|---|---|---|---|
| **P1** ★ | Brand Health | Trust-Engagement Gap (Δ) | 2.52 | ≤ 1.75 | 31 Jul 2026 | Post-campaign tracking survey (N≥287) |
| **P2** | Brand Health | Brand Relatability | M = 2.75/7 | M ≥ 3.50/7 | 31 Jul 2026 | Post-campaign tracking survey |
| **P3** ★ | Brand Health | Asset Security Trust (floor) | M = 5.27/7 | M ≥ 5.00/7 | 31 Jul 2026 | Post-campaign tracking survey |
| **P4** | Brand Health | "Boring" word association | 39.4% | < 25% | 31 Jul 2026 | Post-campaign word association battery |
| **A1** | Awareness | Unique impressions (TG + X combined) | ~0 | 500,000 | 21 May 2026 | Platform analytics |
| **A2** | Awareness | HashKey × Pizza Day brand association | ~0% | ≥ 40% | 22 May 2026 | Mid-campaign pulse survey (N≥100) |
| **A3** | Awareness | "Safe Punk" concept recognition | ~0% | ≥ 50% (18–24 cohort) | 31 May 2026 | Post-campaign tracking survey |
| **E1** ★ | Engagement | @HashKey0xU members (40% active) | 0 | 5,000 | 22 May 2026 | Telegram channel analytics |
| **E2** | Engagement | Pizza Persona UGC pieces | 0 | 2,000 | 31 May 2026 | Social listening (Brandwatch) + manual audit |
| **E3** | Engagement | Laszlo Bot unique sessions (≥3 exchanges avg.) | 0 | 15,000 | 31 May 2026 | Bot analytics dashboard |
| **C1** ★ | Conversion | KYC-verified airdrop accounts | 0 | 10,001 | 22 May 2026 | HashKey KYC account data |
| **C2** | Conversion | Net-new campaign-attributed registrations | TBD | 3,000 | 30 Jun 2026 | UTM + QR + referral code tracking |
| **C3** | Conversion | 30-day post-acquisition active trading rate | TBD | ≥ 40% | 22 Jun 2026 | Platform trading data |

*★ = verdict condition objective (see Campaign Verdict Criteria above). E1 is included as a leading indicator for C1: without community formation, KYC conversion cannot reach the 10,001 cap (Section 6, Finding 4).*

### Simulation Benchmark Comparison

The simulation (Section 6) produced the following Base scenario predictions against which actual campaign performance can be benchmarked:

| Metric | Simulation Prediction (Base) | Campaign Target | Note |
|---|---|---|---|
| TG members by May 22 | ≥10,000 | 5,000 (Objective E1) | Simulation suggests demand-driven ceiling; target is conservative |
| RIB total submissions | 43,392 | Not directly targeted | Directional indicator for organic community engagement |
| /confess unique submissions | 62,522 | Not directly targeted | Directional indicator for Telegram community depth |
| KYC airdrop accounts | 10,001 | 10,001 (Objective C1) | Simulation confirms achievability under Base conditions |
| Trust-Engagement Gap | 1.00 | ≤ 1.75 (Objective P1) | Simulation optimistic; conservative campaign target preserved |
| "Boring" association | 18.9% | < 25% (Objective P4) | Simulation and campaign target aligned |

---

## 9.4 Qualitative Evaluation

Quantitative KPI attainment is necessary but not sufficient for evaluating whether the campaign has achieved its strategic mandate. The "Re-coding Trust" campaign's primary intervention is a cultural repositioning — moving HashKey's brand meaning from "Reliable but Boring" to "Safe Punk." This shift is, at its core, a qualitative change in how the target audience narrates the brand to itself and to others. Schultz and Schultz (2004) and Muniz and O'Guinn (2001) both identify the quality of brand community discourse — not just its volume — as the definitive indicator of repositioning success.

Four qualitative dimensions will be evaluated through social listening analysis conducted during and after the campaign:

### Q1 — Discourse Quality: From "Boring" to "Safe Punk"

**Method:** Brandwatch thematic analysis of organic X/Twitter and LIHKG mentions of HashKey across Phase 1–3, categorised against the brand attribute framework from Section 2.2.4.

**Evaluation question:** Does "Safe Punk" language — specifically references to HashKey's SFC licence as a *positive cultural signal* rather than a bureaucratic barrier — appear in organic community discourse without brand prompting?

**Success indicator:** "Safe Punk" framing adopted by Cultural Native accounts (Section A) in quote-tweets, LIHKG posts, and TG discussions that do not originate from @HashKeyExchange or KOL partners. Brand language that has been internalised by the community does not need to be sponsored to spread.

### Q2 — RIB Community Authorship

**Method:** Qualitative content analysis of the top 100 RIB tombstone submissions (by community engagement score) and the top 50 /confess entries (surfaced in Laszlo's Weekly Verdict).

**Evaluation question:** Do the community's contributions to the memorial wall demonstrate genuine emotional investment in the campaign's narrative frame — or do they read as performative compliance with a brand mechanic?

**Success indicator:** Tombstone submissions that reference personal financial loss, name specific exchanges with emotional detail, and contextualise the submission within the community's shared experience of crypto market history. Ogden (2019) identifies depth and specificity of community contribution as the marker that distinguishes genuine cultural resonance from manufactured participation in memorial site mechanics.

### Q3 — Segment B Conversion Narrative Quality

**Method:** Post-event interviews with a purposive sample (N=10–15) of Pizza Day event attendees who completed KYC on-site (Segment B profile).

**Evaluation question:** What is the stated decision narrative of Cautious Explorers who converted at the event? Does it reference the campaign's community mechanics (RIB, /confess, Personas) — indicating genuine cultural repositioning — or does it reduce to incentive-driven acquisition ("I came for the airdrop")?

**Success indicator:** Converted Segment B users who articulate a shift in brand perception specifically grounded in the Safe Punk positioning — referencing the community's emotional credibility, not solely the airdrop value. Purely incentive-driven conversion narratives indicate that the cultural repositioning has not penetrated Segment B's decision-making, even where conversion metrics are met.

### Q4 — KOL Sentiment Quality

**Method:** Qualitative review of all KOL deliverables against Safe Punk positioning criteria; analysis of audience response sentiment (reply thread quality, not just reaction volume).

**Evaluation question:** Do KOL posts read as genuine peer endorsement (the standard for Cautious Explorer credibility) or as detectable paid promotion?

**Success indicator:** KOL audience replies that engage substantively with the Safe Punk narrative content rather than responding to the promotional mechanic. High reply/impression ratios with substantive discourse are the qualitative signal; high like/impression ratios with low reply depth indicate passive reception without community formation.

---

## 9.5 Evaluation Limitations

**Survey instrument limitations.** The post-campaign tracking survey measures self-reported brand perceptions using the same Likert-scale battery as the baseline. Self-report measures of brand relatability are subject to social desirability effects and recall bias: respondents may adjust reported perceptions toward what they believe is expected, or may conflate their memory of campaign exposure with genuine attitude change. Test-retest reliability of the Trust-Engagement Gap measure is not formally established, as the baseline survey was conducted once; Δ changes at the margin of the target threshold (e.g., reported Δ = 1.78 versus target Δ ≤ 1.75) should be interpreted with appropriate statistical caution.

**Attribution limitations.** Campaign UTM and QR tracking provides directional attribution for registered accounts, but cannot fully isolate campaign causality from background market conditions (BTC price movements, competitor incidents, media coverage). The post-campaign evaluation will report attributed registrations as a lower bound on campaign-influenced registrations, not as a complete account.

**Qualitative sample limitations.** The post-event interview sample (N=10–15) is too small for statistical generalisation; findings will be presented as illustrative rather than representative. The social listening analysis using Brandwatch is bounded by the platform's lexical coverage of Cantonese-language discourse on LIHKG and Telegram, which may undercount community adoption of Safe Punk framing in code-switched or emoji-heavy crypto community vernacular.

**Simulation forecast comparison.** The Section 6 simulation predictions are used as directional benchmarks, not performance targets. The simulation's Base scenario predictions were generated from a model with significant population-scaling limitations (Section 6.5); over-performance against simulation predictions does not indicate success, and under-performance does not indicate failure, without reference to the primary campaign objectives (P1–P4).

---

*Sources: Colley, R. H. (1961). Defining advertising goals for measured advertising results. Association of National Advertisers; HSJMC. (2026, March). Measurement matters: Using KPIs and dashboards to evaluate campaign success. Hubbard School of Journalism and Mass Communication. https://hsjmc.umn.edu/news/2026-03-16/using-kpis-dashboards-evaluate-campaign-success; Muniz, A. M., & O'Guinn, T. C. (2001). Brand community. Journal of Consumer Research, 27(4), 412–432. https://doi.org/10.1086/319618; Ogden, C. (2019). Killed by Google. https://killedbygoogle.com/; Schultz, D. E., & Schultz, H. F. (2004). IMC, the next generation. McGraw-Hill; Section 2.2.4 (survey baseline data); Section 4.4 (campaign objectives); Section 6 (simulation findings); Section 7 (execution timeline, measurement calendar, and Go/No-Go gate criteria).*

*Section 9 | ZHAO Han (1155191400) | CUHK COMM4150 | Supervisor: Prof. Donna Chu*
