# Section 7 — Execution Timeline
## COMM4150 FYP: Re-coding Trust | ZHAO Han (1155191400)

---

## 7.1 Timeline Architecture

The campaign executes across three phases and a post-campaign evaluation window, spanning February to July 2026. The timeline is structured to ensure that each pillar is operationally ready before its audience-facing activation, that the Phase 1 community formation mechanics are sufficiently mature to support Phase 2 conversion, and that the Phase 2 peak event (Bitcoin Pizza Day, May 22) arrives with maximum community momentum and minimum execution risk.

All dates are fixed relative to the May 22 Pizza Day anchor. The Phase 1 launch date of 1 February is determined by two external constraints: (1) the RAVE topicality window (Section 6, Finding 1) requires the RIB thread to launch while RAVE crash salience remains elevated, estimated at 3–5 weeks post-April-crash; and (2) the 5,000-member Telegram community objective (Section 4.4.4, Objective E1) requires approximately three months of sustained recruitment to achieve critical mass before the Pizza Day conversion moment.

Two Go/No-Go gates are built into the timeline (Section 7.5). These are explicit decision points at which campaign leadership reviews leading indicators and decides whether to proceed, adjust, or pause the subsequent phase. Marketing Gantt best practice identifies these gates as essential for complex campaigns where later phases depend on community-formation outcomes from earlier phases (Workamajig, 2025).

---

## 7.1.1 Campaign Timeline — Visual Overview

```mermaid
gantt
    title Re-coding Trust Campaign Timeline 2026
    dateFormat  YYYY-MM-DD
    axisFormat  %b %d

    section Phase 0 · Production
    OOH artwork + media buy          :done,  p0a, 2026-01-05, 2026-01-31
    Hero Film shoot + post           :done,  p0b, 2026-01-12, 2026-01-31
    Laszlo Bot development           :done,  p0c, 2026-01-05, 2026-01-31
    RIB microsite build              :done,  p0d, 2026-01-05, 2026-01-31
    GEO infrastructure deploy        :done,  p0e, 2026-01-26, 2026-01-31
    KOL contracts signed             :done,  p0f, 2026-01-26, 2026-01-31

    section Phase 1 · Narrative Seeding
    Hero Film live                   :active, p1a, 2026-02-01, 2026-05-22
    RIB thread + wall open           :active, p1b, 2026-02-01, 2026-05-22
    @HashKey0xU Telegram live        :active, p1c, 2026-02-01, 2026-05-22
    OOH MTR Central                  :        p1d, 2026-02-01, 2026-05-21
    OOH Causeway Bay DOOH            :        p1e, 2026-02-08, 2026-05-21
    OOH Sham Shui Po flypost         :        p1f, 2026-02-22, 2026-05-21
    KOL activation (4 partners)      :        p1g, 2026-02-15, 2026-05-22
    Pizza Personas quiz live         :        p1h, 2026-02-28, 2026-05-31
    Go/No-Go Gate 1                  :crit,   g1,  2026-03-28, 1d
    RAVE crash + RIB surge           :crit,   p1i, 2026-04-01, 2026-04-14
    Mid-campaign pulse survey        :        p1j, 2026-04-15, 2026-04-30
    "Still Here" counter-thread      :crit,   p1k, 2026-05-01, 2026-05-07
    14-day countdown                 :        p1l, 2026-05-08, 2026-05-21
    Go/No-Go Gate 2                  :crit,   g2,  2026-05-14, 1d

    section Phase 2 · Pizza Day Peak
    Pizza Day Event — Central HK     :crit,   p2a, 2026-05-22, 1d
    Airdrop 20:10 HKT trigger        :crit,   p2b, 2026-05-22, 1d

    section Phase 3 · Sustain
    Community sustain (TG + Dev)     :        p3a, 2026-05-23, 2026-06-30
    30-day retention measurement     :        p3b, 2026-05-23, 2026-06-22

    section Evaluation
    Post-campaign tracking survey    :        e1,  2026-07-01, 2026-07-14
    Analysis + reporting             :        e2,  2026-07-15, 2026-07-31
```

---

## 7.2 Master Timeline

### Phase 0: Production (January 2026)

| Week | Dates | Workstream | Deliverable |
|---|---|---|---|
| W1 | 5–11 Jan | Creative Production | OOH artwork brief finalised; MTR/CWB formats confirmed with media buyers |
| W1 | 5–11 Jan | Technology | Laszlo Bot v1 development begins (Telegram + X/Twitter integration) |
| W1 | 5–11 Jan | Technology | RIB microsite (beltran12138.github.io/hkx/rib/) architecture scoped |
| W2 | 12–18 Jan | Creative Production | Hero Film script locked; director briefed; casting for 60-second graveyard film |
| W2 | 12–18 Jan | Technology | Pizza Personas quiz logic + 5 persona result cards developed |
| W3 | 19–25 Jan | Creative Production | Hero Film shoot |
| W3 | 19–25 Jan | Technology | Laszlo Bot v1 internal testing; /confess command QA |
| W3 | 19–25 Jan | Technology | RIB microsite tombstone-generation logic built and tested |
| W4 | 26 Jan – 1 Feb | Creative Production | Hero Film post-production (edit, colour grade, music clearance) |
| W4 | 26 Jan – 1 Feb | Technology | Pizza Personas web app QA; Telegram sticker pack submitted to Telegram store |
| W4 | 26 Jan – 1 Feb | Partnerships | KOL contracts signed; briefing decks delivered |
| W4 | 26 Jan – 1 Feb | OOH | MTR Central and Causeway Bay booking confirmed; artwork submitted |
| W4 | 26 Jan – 1 Feb | Technology | **GEO infrastructure deployed**: `llms.txt` at beltran12138.github.io/hkx/llms.txt; Event + FAQPage JSON-LD injected into RIB microsite; Organization schema into SkillHub; Quick Answer blocks published (Section 5.8) |

---

### Phase 1: Narrative Seeding (February 1 – May 21, 2026)

#### February 2026: Launch

| Week | Dates | Workstream | Action |
|---|---|---|---|
| W1 | 1–7 Feb | **LAUNCH** | Hero Film published on @HashKeyExchange (X/Twitter + Telegram) |
| W1 | 1–7 Feb | **LAUNCH** | RIB thread posted on X/Twitter: "We're building a memorial wall. Reply with any crypto exchange, protocol, or fund that no longer exists." |
| W1 | 1–7 Feb | **LAUNCH** | @HashKey0xU Telegram channel opens; Laszlo Bot deployed; /confess command live |
| W1 | 1–7 Feb | **LAUNCH** | hashkey.com/hkx Developer Infrastructure beta launch (SkillHub + hkx CLI) |
| W1 | 1–7 Feb | OOH | MTR Central Station lightboxes live |
| W2 | 8–14 Feb | Social | RIB tombstone curation begins; community submissions rolling in; HashKey team curates and verifies weekly |
| W2 | 8–14 Feb | Community | TG: first Laszlo's Weekly Verdict post (best confession of the week) |
| W2 | 8–14 Feb | OOH | Causeway Bay DOOH 15-second loop begins |
| W3 | 15–21 Feb | Social | KOL #1 and #2 post RIB participation and TG join CTA to their audiences |
| W3 | 15–21 Feb | Community | TG community first milestone: 500 members target |
| W4 | 22–28 Feb | Social | Pizza Personas quiz link goes live; first UGC screenshots begin circulating |
| W4 | 22–28 Feb | OOH | Sham Shui Po flyposting and sticker placement begins |

#### March 2026: Community Formation

| Week | Dates | Workstream | Action |
|---|---|---|---|
| W1–W2 | Mar 1–14 | Social | RIB wall approaches 1,000 tombstones; community debate on CT intensifies |
| W1–W2 | Mar 1–14 | Community | TG: second Laszlo's Weekly Verdict; /confess unique submissions tracked toward 10,000 |
| W1–W2 | Mar 1–14 | Technology | hkx CLI v1.0 public release; developer community seeding begins |
| W3–W4 | Mar 15–31 | Social | KOL #3 and #4 post; Pizza Personas UGC volume target: 500 pieces cumulative |
| W3–W4 | Mar 15–31 | Community | TG: 2,000-member milestone target |
| W3–W4 | Mar 15–31 | Measurement | Mid-Phase 1 internal metrics review: RIB submissions, TG growth rate, UGC volume |

#### April 2026: Acceleration (RAVE Crash Context)

| Week | Dates | Workstream | Action |
|---|---|---|---|
| W1 | Apr 1–7 | Environment | RaveDAO (RAVE) crash: $6B market cap wiped; ZachXBT investigation published |
| W1 | Apr 1–7 | Social | RIB wall update: RAVE added to memorial; community submissions surge |
| W2 | Apr 8–14 | Social | X/Twitter: RAVE tombstone generates earned media spike; no paid amplification |
| W2 | Apr 8–14 | Community | TG: RAVE-specific /confess wave; airdrop queue builds rapidly |
| W3–W4 | Apr 15–30 | Social | Pizza Personas UGC target: 1,500 pieces cumulative |
| W3–W4 | Apr 15–30 | Community | TG: 4,000-member milestone target |
| Apr | Throughout | Research | Mid-campaign pulse survey conducted (N≥100); HashKey × Pizza Day association measured |

#### May 2026: Final Countdown

| Week | Dates | Workstream | Action |
|---|---|---|---|
| W1 | May 1–7 | Social | **"Still Here" counter-thread deployed** at peak RIB engagement: @HashKeyExchange replies to its own thread: "Still here. SFC Type 1 + Type 7. HashKey Exchange, 2018–" |
| W1 | May 1–7 | Community | TG: 5,000-member milestone target (Objective E1 deadline: May 22) |
| W2 | May 8–14 | Social | 14-day countdown begins: daily provocation posts on X/Twitter |
| W2 | May 8–14 | Social | Airdrop scarcity mechanic activated: "10,001 slices. After that: it's history." |
| W3 | May 15–21 | Social | D-7 to D-1 countdown; KOL final posts; OOH final week of display |
| W3 | May 15–21 | Event | Physical event final logistics: Central venue, KYC kiosk setup, pizza catering, RIB physical installation |
| May 21 | Eve of Pizza Day | Event | **All systems live check**: KYC kiosks, Laszlo Bot, airdrop smart contract, RIB installation, event staff briefed |

---

### Phase 2: Pizza Day Peak (May 22, 2026)

| Time (HKT) | Workstream | Action |
|---|---|---|
| 08:00 | Social | Final pre-event post: "Today. Central. 20:10." |
| 10:00 | Event | Venue opens; RIB physical installation (Wall of the Fallen) visible to attendees |
| 10:00–18:00 | Event | On-the-spot KYC registration kiosks operational; attendees register and queue for airdrop |
| 14:00 | Event | Pizza service begins |
| 18:00 | Community | Laszlo Bot in-event activation: /confess at the event earns bonus airdrop priority |
| 20:10 | **AIRDROP** | BTC price trigger: "10,001st Slice" airdrop executes; 10,001 KYC-verified accounts receive HKX tokens |
| 20:10+ | Social | Attendees post airdrop receipt to X/Twitter → earned media loop activates |
| Post-event | Social | @HashKeyExchange thread update: "The wall still stands. You're still here." |

---

### Phase 3: Community Sustain (May 23 – June 30, 2026)

| Week | Dates | Workstream | Action |
|---|---|---|---|
| W1 | May 23–29 | Community | TG: post-event community debrief; Laszlo's Weekly Verdict continues |
| W1 | May 23–29 | Measurement | C3 retention clock starts: 30-day active trading rate tracking begins |
| W2 | May 30 – Jun 5 | Technology | Developer Infrastructure: SkillHub post-event content; hkx CLI v1.1 update |
| W2–W4 | Jun 6–30 | Community | Ongoing TG moderation; monthly Laszlo's Weekly Verdict; developer community engagement |
| Jun 30 | Measurement | C2 deadline: net-new account attributions compiled; C3 30-day retention measured (by Jun 22) |

---

### Post-Campaign Evaluation (July 2026)

| Week | Dates | Workstream | Action |
|---|---|---|---|
| W1–W2 | Jul 1–14 | Research | Post-campaign tracking survey fielded (N≥287, same screening criteria as Section 2.2.2) |
| W3 | Jul 15–21 | Analysis | Survey data processed; Trust-Engagement Gap (Δ) calculated; "Boring" association measured |
| W4 | Jul 22–31 | Reporting | Evaluation report compiled; all 13 objectives assessed against targets (Section 9) |

---

## 7.3 Critical Path

Three milestones define the campaign's critical path — delays in any of these directly threaten Phase 2 conversion:

| Milestone | Deadline | Risk if Missed |
|---|---|---|
| RIB thread launch | February 1 | RAVE topicality window closes; Phase 1 seeding momentum lost |
| "Still Here" counter-thread | May 1–7 (at peak RIB engagement) | Early reveal reduces RIB submissions by ~31% (Section 6, Finding 3); late reveal produces diminishing returns |
| KYC airdrop accounts: 10,001 | May 22, 20:10 HKT | C1 objective fails; airdrop trigger event loses scarcity and cultural significance |

The OOH media buy (4-week production lead) and Laszlo Bot development (6-week build) are the longest-lead production items and drive the January production schedule. Both must be complete before February 1 to support the Phase 1 launch sequence.

---

## 7.4 Pillar Activation Summary

| Pillar | Production Complete | Audience-Facing Launch | Active Through |
|---|---|---|---|
| Hero Film | Jan 31 | Feb 1 | May 22 (event) |
| OOH (MTR + CWB) | Jan 31 | Feb 1 | May 21 |
| OOH (Sham Shui Po) | Feb 21 | Feb 22 | May 21 |
| RIB Microsite + Social Thread | Jan 31 | Feb 1 | Permanent |
| Telegram @HashKey0xU | Jan 31 | Feb 1 | Ongoing |
| Laszlo Bot | Jan 31 | Feb 1 | Ongoing |
| Pizza Personas Quiz | Jan 31 | Feb 28 | May 31 |
| KOL Partnerships | Feb 14 (contract) | Feb 15 | May 22 |
| Developer Infrastructure | Jan 31 | Feb 1 | Permanent |
| Pizza Day Event | May 21 (final check) | May 22 | May 22 |

---

---

## 7.5 Go/No-Go Decision Gates

Two formal decision gates are embedded in the Phase 1 timeline. Each gate requires a review of the leading indicators listed below before the subsequent phase is authorised to proceed. The gate structure follows the standard campaign management practice of building phase-conditional logic into complex community-formation campaigns, where later phases depend critically on community density achieved in earlier phases (Workamajig, 2025).

### Gate 1 — End of March 2026 (Go/No-Go: Phase 1 Acceleration)

**Date:** March 28, 2026  
**Reviews:** RIB tombstone volume; TG membership growth rate; Pizza Personas UGC output; KOL amplification performance  
**Go criteria:**
- RIB tombstones submitted ≥ 500 (on track for Base scenario's 43,392 by May 22)
- @HashKey0xU membership ≥ 1,500 (on track for 5,000 objective)
- Pizza Personas UGC ≥ 300 pieces circulating organically

**No-Go action:** If fewer than two of three Go criteria are met, Phase 1 Acceleration (April KOL #3/#4 posts, Personas push) is paused for two weeks and the campaign team reviews whether the RIB mechanic requires editorial intervention (e.g., seeded tombstone content, community moderator posts) to restart organic submission momentum.

---

### Gate 2 — May 14, 2026 (Go/No-Go: Phase 2 Pizza Day Event)

**Date:** May 14, 2026 (8 days before event)  
**Reviews:** Total KYC-verified accounts; "Still Here" counter-thread engagement; event registration headcount; logistics readiness  
**Go criteria:**
- KYC-verified airdrop accounts ≥ 5,000 (50% of cap; airdrop is viable at partial fill)
- @HashKey0xU membership ≥ 4,500
- Physical event registration ≥ 300 confirmed attendees
- KYC kiosk, airdrop smart contract, and Laszlo Bot event mode all QA-verified

**No-Go action:** If KYC accounts < 5,000 AND event registration < 200, campaign leadership may postpone the airdrop trigger from the Pizza Day event to a follow-up digital-only event (May 29). Physical event proceeds as planned — the RIB installation and community gathering have independent value regardless of airdrop fill rate.

---

## 7.6 Dependency Map

The following dependencies govern sequencing and must not be reordered:

| Upstream deliverable | Dependent action | Consequence of reordering |
|---|---|---|
| RIB tombstone volume (Phase 1, Round 1) | "Still Here" counter-thread (Phase 1, Round 3) | Counter-thread without accumulated RIB context loses emotional resonance; simulation Finding 3 shows 1.63× reduction in stance impact |
| TG community formation (/confess mechanic) | KYC conversion at event | Community belonging must precede conversion CTA; simulation Finding 4 shows Cautious Explorer KYC probability peaks at 0.38 only in Round 3 after Rounds 1–2 community formation |
| GEO infrastructure (Phase 0) | AI-referred traffic throughout Phase 1 | JSON-LD crawl lag is 2–4 weeks; deploying in Phase 1 rather than Phase 0 loses the first month of AI search citation |
| RAVE crash salience (external; April 2026) | Phase 1 seeding momentum | Not controllable — but GEO infrastructure and RIB wall must be live before crash to capture the surge; post-crash deployment would miss the peak |

---

*Sources: Section 4.1.3 (campaign architecture and three-phase structure); Section 4.4 (campaign objectives and deadlines); Section 4.5 (channel strategy and media mix); Section 5.8 (GEO infrastructure deployment); Section 6 (simulation findings informing launch timing and gate criteria); Sections 5.1–5.7 (execution pillar production requirements); Workamajig. (2025). Building a marketing campaign timeline. https://www.workamajig.com/marketing-guide/campaign-timeline.*

*Section 7 | ZHAO Han (1155191400) | CUHK COMM4150 | Supervisor: Prof. Donna Chu*
