# Rogue Leisure: Implementation Plan

**Client:** Aidan, Rogue Leisure Ltd, The Point, Gatehouse Way, Aylesbury
**Consultant:** Tony Winyard, Winyard AI
**Date:** 6 February 2026
**Status:** Post-discovery meeting. Implementation starts Monday 10 Feb.

---

## What We Now Know (Meeting Findings Combined with Prior Research)

### Confirmed from today's meeting

**Origin story:** Rogue started as "Rogue Squadron" (Star Wars reference) go-kart team when Aidan worked at Waitrose. Evolved into Rogue Racing when he bought the MK go-kart track. Became Rogue Leisure when they moved to Aylesbury and added bowling/multi-activity.

**Social media is stronger than we thought:** ~8,800 Facebook followers (not the 952 Instagram figure from our research). Aidan is active on social media personally. Best engagement comes from real people/real stories (87-year-old lady karting, granddaughter bowling). He wants to move away from cartoony Canva graphics toward authentic content.

**Instagram not connected to Meta Business Suite:** Aidan hasn't been able to connect Instagram to the Meta Business account. You walked him through connecting it during the visit.

**Marketing person:** A young lady does bits of marketing on Canva and ChatGPT. She also works for a charity. Not a full-time marketing role.

**Website is NOT a blocker:** Jane (friend) built it on Webflow for £800. Jane is happy to make updates cheaply. Aidan just needs to tell her what to change. He can use your website analysis document as the brief for Jane. This is much simpler than we assumed.

**Aidan's stated priorities (in his own words):**
1. "I want me sorted" -- personal productivity tools, voice-to-text, talking to his computer
2. Central file storage with access levels (like an intranet) -- everyone can access what they need
3. Digital checklists on tablets replacing paper -- temp checks, kart checks, opening/closing routines
4. Automated alerts when checks are missed ("I expect five temp checks per week; if there's only four, alarm goes off")
5. Unsent sales emails he hasn't gotten to yet -- freeing him up means more revenue

**Ecosystem decision: Google Workspace (not Microsoft)**
- Aidan was positive about Google Workspace
- H&S guy already uses Google Shared Drive for compliance docs (cart maintenance reports, fire alarm checks)
- Currently on Exchange for email (10 accounts) but only using it for email, nothing else
- Google gives them Drive, Docs, Sheets, Gmail, Gemini AI, all under one roof
- Emails can be ported from Exchange to Gmail

**Alpha (karting timing system):** Was recommended to them (~£400) but never actually adopted. It has a garage/service record feature. Key concern: if you use Alpha and leave, you lose your documents unless you export first. Decision was that tablet-based digital records owned by Rogue (in Google Drive) are safer than being locked into Alpha.

**Hardware situation:**
- No tablets currently (only a couple of Kindles used for Crazy Cat Lady disclaimers)
- Aidan happy to buy Samsung tablets (£60-70 each) with cases
- Also has a touchscreen Windows machine somewhere

**Key staff:**
- **Dawn** -- manager, would receive alerts for missed compliance checks
- **Doris** -- bar staff, would do temperature checks
- **Pete** -- karting, would do kart maintenance checks
- Marketing lady (name unclear) -- does Canva/ChatGPT social content
- H&S person (internal) -- already using Google Shared Drive

**Paper processes observed on-site:**
- Fire/weekly alarm checks (currently scanned to Google Drive by H&S person, who is behind on scanning)
- Temperature checks (bar)
- Kart maintenance/service sheets (per kart number)
- Opening/closing routines
- Accident report forms (locked away in a cupboard, easy to lose)

**The scanning backlog problem:** H&S person and Dawn both have loads of paperwork to scan. They're behind. Accident reports are locked in a cupboard. Digital forms eliminate this entirely -- no scanning step, data goes straight to the folder.

---

## Implementation Plan

### Phase 1: Monday 10 Feb -- Full Day On-Site

#### 1A. Aidan's Personal Productivity Stack (Morning, ~2 hours)

**Install on Aidan's computer:**
- **Wispr Flow** (£10/month) -- voice-to-text everywhere. He specifically asked for this: "I want people to think I've gone mad and I'm talking to my computer but it's actually doing the work for me"
- **Granola** (£10/month) -- AI meeting notes. Captures calls and meetings automatically.
- **Claude Pro** (£18/month) -- AI assistant for emails, reports, thinking through problems. He specifically mentioned wanting help producing reports and dictating emails.

**Quick training:** Show Aidan how to dictate an email using Wispr Flow, demonstrate Granola on a test call, show Claude drafting a response to a customer complaint.

**Total: £38/month**

#### 1B. Google Workspace Setup (Morning/Early Afternoon, ~2-3 hours)

**What to set up:**
- Google Workspace Business Starter (£5.50/user/month) for management team
- Migrate Exchange emails to Gmail (can be done gradually; Exchange can run in parallel initially)
- Create shared Google Drive structure:

```
Rogue Leisure (Shared Drive)
├── Bowling/
│   ├── Lane maintenance/
│   ├── Bookings/
│   └── Party packages/
├── Karting/
│   ├── Kart service sheets/ (individual folder per kart number)
│   ├── Track maintenance/
│   └── Bookings/
├── Escape Room/
├── Compliance/
│   ├── Temperature checks/
│   ├── Fire alarm checks/
│   ├── Accident reports/
│   ├── Opening routines/
│   └── Closing routines/
├── Staff/
│   ├── Rotas/
│   ├── Training/
│   └── HR/
├── Finance/
├── Marketing/
└── Corporate/
```

**Access levels:** Aidan and Dawn get full access. Other managers get access to their areas. Staff get read-only where appropriate.

**Leverage existing:** H&S person already has a Google Drive with compliance docs. Migrate/link this into the shared structure so everything is in one place.

**Cost:** ~£5.50/user/month. For 5-7 management users = £27.50-38.50/month. Don't need to licence all 29 staff immediately.

#### 1C. Digital Checklists -- First Two Forms (Afternoon, ~2 hours)

**Build using Google Forms + Google Sheets** (free, already in Google Workspace):

**Form 1: Fridge & Freezer Temperature Check** (based on photographed paper form)
- Staff member name (dropdown: Doris, etc.)
- Date/time (auto-populated)
- AM or PM check (dropdown)
- **Slides Freezer** temp (number field; acceptable range: -18°C to -22°C)
- **Pizza Freezer** temp (number field; acceptable range: -18°C to -22°C)
- **Chest Freezer** temp (number field; acceptable range: -18°C to -22°C)
- **Main Fridge** temp (number field; acceptable range: 1°C to 5°C)
- **Slush Fridge** temp (number field; acceptable range: 1°C to 5°C)
- Auto-validation: flag if any reading is outside acceptable range
- Notes for the day (text field)
- Auto-saves to: `Compliance/Temperature checks/` in Google Drive
- Sheet calculates: daily AM/PM completion, weekly count (expect 10: 5 AM + 5 PM)

**Form 2: Bar & Reception Open Checklist** (based on photographed paper form, ~20 tasks)
- Staff member name (dropdown)
- Date (auto-populated)
- Checklist items (tick each as done):
  - Ice machine refilled
  - Slush machine refilled
  - Hot water urn on and refilled
  - AM fridge & freezer temp checks done (links to Form 1)
  - Postmix taps checked
  - Mints tray restocked
  - Wash machine checked
  - Dishwasher checked
  - Ovens, air fryers & microwaves checked
  - Food date labels checked, old stock reported to Duty Manager
  - Hot dogs & pizza boxes available for the day
  - Crisps, sweets and chocolates restocked
  - Cups and slush cups restocked behind bar
  - Pool table check (10 balls, 2 cue balls, tips checked)
  - Bowling lanes clean and set up
  - Photobooth cleaned and wiped
  - Emails checked and responded to
  - Deliveries signed for and put away
- Notes/issues field (e.g. "wash machine BROKEN")
- Signed off by (auto-captured from login)
- Auto-saves to: `Compliance/Opening routines/`

**Form 3: Kart Servicing / Maintenance** (based on photographed paper form)
- Kart number (dropdown)
- Date (auto-populated)
- Staff member name (dropdown: Pete, etc.)
- **Type of entry** (dropdown: Fault/Breakdown, Scheduled Maintenance, General Check/Service, Additional Work)
- Per-item checks (tick/cross/blank):
  - Brakes, Steering, Bodywork, Tyres, Engine, Chain/Belt, Bumpers, Seat, Harness
  - Tick = checked and OK / within tolerances
  - Cross = fault / repair / replaced
  - Blank = not checked
- **Service notes** (text field -- description of work done)
- **Fault number** (text field -- for tracking)
- **Parts needed/fitted** (text field)
- Photo upload option (damage/wear documentation)
- Auto-saves to: `Karting/Kart service sheets/`

**Form 4: Kart Fault Report** (based on photographed paper form -- separate from servicing)
- Kart number (dropdown)
- Date reported
- Reported by (dropdown)
- Fault details (text field)
- Parts needed / on order (text field)
- Fault resolution (text field)
- Parts fitted (text field)
- Date repaired
- Repaired by (dropdown)
- Auto-saves to: `Karting/Kart service sheets/` (same folder, different sheet)

**Why Google Forms first (not Trail or SafetyCulture):**
- Zero additional cost (included in Google Workspace)
- Staff can access from any device with a browser (tablets, phones, existing Kindles)
- Data goes directly into Google Sheets, which is already in the shared Drive
- Proves the concept before committing to paid tools
- Can upgrade to Trail (£38/month) later if they need more sophisticated scheduling, alerts, and AI features

**Tablet setup:** If Aidan has purchased Samsung tablets by Monday, configure them with:
- Google account
- Home screen shortcuts to each checklist form
- Lock the tablet to kiosk mode if appropriate (so staff just tap and fill)

#### 1D. Missed-Check Alerts (Afternoon, ~1 hour)

**Simple automation using Google Apps Script or Zapier:**
- At end of each day (or weekly summary), count entries in each compliance sheet
- If expected count not met, send email/notification to Aidan and Dawn
- Example: "Temperature checks: 4 of 5 expected this week. Missing: Wednesday."

**Aidan's exact words:** "I expect five temp checks per week. If there ain't five, can I have an alarm go off saying 'Aidan, you need to look at it' or 'Dawn, you need to look at this'?"

---

### Phase 2: Week of 17 Feb -- Additional Digital Forms + Website Brief

#### 2A. Remaining Compliance Forms
Build the same Google Forms pattern for:
- **Bar & Reception Close checklist** (~25 tasks including PM temp checks, dishwasher, slush machines off, spirit measures, ice bucket, glass wash, seating/tables, pool balls, postmix syrups, toilets, mopping, rubbish -- all captured from photographed form)
- **Fire/weekly alarm checks** (replacing the paper forms H&S person currently scans)
- **Accident report form** (replaces paper locked in cupboard; auto-files to Compliance/Accident reports/)

Note: Bar & Reception Open checklist is now in Phase 1 (Form 2). Each form auto-saves to the correct Google Drive folder. No more scanning. No more paper in cupboards.

#### 2B. Kart Service History Dashboard
- Google Sheet that pulls from all kart check submissions
- Per-kart view: "Kart 12 -- all checks and notes"
- Aidan's request: "I want a tablet where you go cart 12, it pulls up the service sheet"
- This replaces what Alpha would have provided, but Rogue owns the data

#### 2C. Website Brief for Jane
- Take your existing website-analysis-and-recommendations.md document
- Reformat as a clear brief for Jane (the Webflow developer)
- Prioritise: testimonials, facility photos, escape room page completion, FAQ section
- Include the corporate landing page specification
- Aidan said he'd happily email this to Jane: "If I can turn around and go through your consultancy piece, I'll go Jane"

---

### Phase 3: Weeks 3-4 -- Staff Scheduling + Email Migration

#### 3A. Staff Scheduling
Currently 4-5 hours/week manual roster building. Options:
- **RotaCloud** (from £29/month for 29 staff) -- UK-based, simple, drag-and-drop
- **Rotaready** (quote-based) -- leisure-specific, integrates with booking systems
- **Google Sheets + automation** -- lowest cost but less sophisticated

Recommend starting with RotaCloud trial (free for 14 days) since it's the simplest for a team that isn't tech-savvy.

#### 3B. Complete Email Migration (Exchange to Gmail)
- Migrate remaining Exchange mailboxes to Gmail
- Set up email signatures for the team
- Cancel Exchange plan once fully migrated (saves current Exchange cost)

#### 3C. Unsent Sales Emails
Aidan mentioned having emails that would generate sales but hasn't gotten to them. Once Wispr Flow is working:
- He dictates the emails using voice
- Claude helps polish them
- They go out

This is a direct revenue opportunity with zero tool cost (already covered by Phase 1 tools).

---

### Phase 4: Month 2+ -- Optimisation and Growth

#### 4A. Review Automation
Automated post-visit review requests via email/SMS. Builds Google reviews (currently 4.5+ stars but could be higher volume).

#### 4B. Social Media Strategy
Aidan's authentic content (real people, real stories) already gets the best engagement. Help systematise this:
- Content calendar
- Template for "customer story" posts
- Schedule using Meta Business Suite (now connected)

#### 4C. Chatbot (Medium-Term)
As discussed in pre-meeting research, this is a medium-term play:
- Build FAQ page on website first (via Jane) -- this is the knowledge base
- Add chatbot (likely Tidio or Botpress) once FAQ content exists
- Focus on after-hours coverage and corporate enquiry capture

#### 4D. Corporate Landing Page + Enquiry Process
Once Jane builds the corporate page:
- Add enquiry form that captures group size, date, budget, activities
- Auto-notification to Aidan
- Follow-up template in Claude

#### 4E. Booking System Investigation

**Confirmed systems** (names confirmed by Aidan via WhatsApp, 6 Feb 2026):

| Activity | System | Vendor |
|----------|--------|--------|
| Bowling | **QubicaAMF Conqueror X** | QubicaAMF Worldwide (Richmond VA / Bologna). Also manufactures Rogue's pinsetters and lanes. 10,000+ centres in 90 countries. |
| Escape Room | **Resova** | Resova Ltd (UK, est. 2015). Acquired by Clubspeed LLC in 2022. 2,000+ customers, 1,500+ escape rooms. |
| Go-Karting | **Book My Karting** | Smart Entertainment Limited (Lichfield, est. 1998). £73M+ bookings processed. ASP.NET stack. |

**API and integration research:**

- **Resova** -- Full REST API at developers.resova.com. Webhooks supported (transaction.created, booking.updated, etc.). Integrates with MailChimp, Google Calendar (two-way sync), Stripe, PayPal, Groupon. CSV/XML export (6-month date range limit). **Best integration potential of the three.**
- **QubicaAMF Conqueror X** -- Developer portal at developer.qubicaamf.com (requires authorisation from QubicaAMF rep). Software suite includes Conqueror XRM (CRM/loyalty) which may already be included but not activated. Integrates with QuickBooks, Square. QPortal cloud dashboards for reporting.
- **Book My Karting** -- No public API. Integrates with MailChimp, PayPal, WorldPay, Sage Pay. CSV/PDF export for reports. Would need direct contact with Smart Entertainment for any custom integration work.

**Practical short-term approach (before considering ROLLER or full unification):**
1. **Resova:** Set up webhooks to push escape room bookings to a Google Sheet automatically
2. **QubicaAMF:** Ask Rogue's QubicaAMF rep about API access and whether QPortal reports can be scheduled/emailed. Check if Conqueror XRM loyalty features are already included in their licence.
3. **Book My Karting:** Weekly CSV export to Google Sheet (manual for now; ask Smart Entertainment about API access later)
4. **Simple Google Sheet dashboard** pulling from these three sheets to show total bookings across all activities

**Current cost:** Aidan estimates ~£600/month total for the three systems. This is significant context for the ROLLER evaluation below.

**Manual Excel bookkeeping:** Every evening, staff manually enter all money received and booking details from the three systems into Excel columns. This duplicates data that already exists in the booking systems, is time-consuming and error-prone, and would be largely eliminated by either (a) automated exports from the current systems to Google Sheets, or (b) a unified platform with built-in reporting.

**Medium-term: Unified platform evaluation.** ROLLER (£310-825/month) or Clubspeed remain worth evaluating. At £600/month for three separate systems with no CRM, no loyalty, no unified reporting, and no dynamic pricing, ROLLER's mid-range pricing could actually be a cost saving while adding significant capability. Notably, Clubspeed acquired Resova in 2022, so there may be a natural consolidation path.

---

## Cost Summary

### Immediate (Phase 1 -- from Monday)

| Item | Monthly Cost | Notes |
|------|-------------|-------|
| Wispr Flow | £10 | Aidan's computer |
| Granola | £10 | Meeting capture |
| Claude Pro | £18 | AI assistant |
| Google Workspace (5-7 users) | £27.50-38.50 | Shared Drive, Gmail, Docs, Forms |
| **Total** | **£65.50-76.50/month** | |

### Hardware (One-Off)

| Item | Cost | Notes |
|------|------|-------|
| Samsung tablets x 2-3 | £120-210 | For bar and karting checklist stations |
| Tablet cases | £30-45 | Rugged, drop-proof |
| **Total** | **£150-255** | |

### Phase 3 Addition

| Item | Monthly Cost | Notes |
|------|-------------|-------|
| RotaCloud (29 staff) | ~£29 | Staff scheduling |
| **Running total** | **~£95-106/month** | |

### What Gets Cancelled

| Item | Saving |
|------|--------|
| Exchange email plan | TBC (depends on current plan cost) |
| Paper/printing for checklists | Minor but symbolic |

---

## Files to Create This Weekend

1. **Clean meeting notes** -- coherent version of today's Wispr Flow transcript (save to client folder)
2. **Proposal for Aidan** -- client-facing document summarising what you'll do, when, and what it costs. Use the proposal-generator skill. Format for audio (NotebookLM) since Aidan prefers listening.
3. **Website brief for Jane** -- reformatted version of website-analysis-and-recommendations.md as actionable instructions
4. **Google Workspace migration checklist** -- step-by-step for Monday
5. **Digital checklist templates** -- pre-build the Google Forms so Monday is install-and-go

---

## Key Decisions Still Needed

1. **Your pricing model** -- per-phase project fees, monthly retainer, or hybrid? Need to decide before creating Aidan's proposal.
2. **How many Google Workspace licences?** -- 5 (management only) or more? Need to know which staff members need access beyond email.
3. **Tablet quantity** -- 2 (one for bar, one for karting) or 3 (add one for opening/closing routines)?
4. **Exchange plan details** -- need to know the current cost to calculate savings from migration.

---

## What This Plan Does NOT Cover (Yet)

- Booking system unification (needs API investigation)
- Dynamic pricing (needs booking system understanding first)
- Loyalty programme (medium-term)
- Chatbot implementation (medium-term; FAQ page first)
- Gift card digitisation (quick win but not urgent)
- Staff scheduling beyond RotaCloud recommendation (needs trial)

These are all Phase 4+ items. The priority is getting Aidan's personal tools working, the central file system live, and paper checklists digitalised. Everything else builds on that foundation.
