# Rogue Leisure Pre-Meeting Research Briefing

**For:** Tony Winyard (Winyard AI)
**Meeting with:** Aidan (Owner, Rogue Leisure Ltd, Aylesbury)
**Date:** 6 February 2026

---

## Table of Contents
1. [Chatbot: Pros and Cons](#1-chatbot-pros-and-cons)
2. [Top 3 Chatbot Recommendations for Webflow](#2-top-3-chatbot-recommendations)
3. [Additional Chatbot Considerations](#3-additional-chatbot-considerations)
4. [Competitor Analysis](#4-competitor-analysis)
5. [ICP Analysis](#5-icp-analysis)
6. [Market Trends](#6-uk-indoor-leisure-market-trends)
7. [Booking System Integration Research](#7-booking-system-integration)
8. [Staff Scheduling Solutions](#8-staff-scheduling)
9. [Compliance Digitisation](#9-compliance-digitisation)
10. [Revenue Optimisation Opportunities](#10-revenue-optimisation)
11. [Additional Discovery Meeting Questions](#11-additional-meeting-questions)
12. [Suggested Meeting Agenda Items](#12-suggested-meeting-agenda)

---

## 1. Chatbot: Pros and Cons

### PROS

**Staff time recovery on repetitive enquiries**
Rogue fields calls across two numbers for questions with fixed answers: what to wear karting, parking, age/height requirements, cancellation policies, pricing. Industry data shows chatbots handle up to 80% of routine enquiries at roughly £0.50 per interaction vs £6 for a human call. With 22 zero-hour staff already stretched thin, absorbing 30-40 calls per week through a chatbot frees meaningful capacity.

**After-hours coverage (closed Monday and Tuesday)**
Significant advantage. Families planning weekend visits often research midweek. Corporate event planners research during office hours, which may not overlap with Rogue's opening times. A chatbot catches these visitors instead of losing them.

**Corporate and group enquiry capture**
No corporate landing page currently exists. Corporate bookers (PAs, HR teams, team leads) research multiple venues quickly. A chatbot acts as a guided enquiry form: "How many people? Which activities? What date?" This turns a cold website visit into a warm lead that Aidan can follow up on.

**Multi-activity cross-selling**
Rogue's unique advantage is bowling + karting + escape room + arcades + karaoke under one roof. But the website silos these. A chatbot can actively cross-sell: "Looking at bowling? Did you know you can add karting?" Particularly valuable for the escape room (only 5% of revenue) which is under-promoted.

**Booking routing**
Three separate booking systems (Cubicle, bespoke karting, Resolver) confuse customers. A chatbot acts as a routing layer: "What would you like to book?" then directs to the correct link.

**Social proof injection**
4.5+ star reviews on Google/TripAdvisor but none on the website. A chatbot can surface testimonials contextually at the moment of decision.

**ADHD-friendly for Aidan**
Reduces volume of interruptions requiring immediate attention. Enquiries get captured; Aidan only deals with complex or high-value ones.

**Content gap bridge**
No FAQ section, thin escape room page, no corporate page. A chatbot immediately answers questions those missing pages would answer, while proper content gets built.

### CONS

**Risk of bad experience if poorly configured**
Wrong information about age restrictions, pricing, or session times is worse than no chatbot. Keeping the knowledge base current requires ongoing attention, which is a concern given Aidan's ADHD challenges.

**Three booking systems create integration complexity**
No chatbot will natively integrate with all three. The chatbot answers questions and directs to booking links, but it is not a booking engine without custom API work.

**Local business personality risk**
Reviews consistently mention staff warmth and personal touch. An overly corporate or robotic chatbot could undermine what customers value. Tone must match Rogue's vibe: fun, welcoming, slightly irreverent.

**Cost sensitivity**
At £80k/month breakeven, even £50-100/month needs to demonstrably earn its keep through saved staff time or attributable bookings.

**Maintenance burden**
Someone needs to review conversations weekly, update the knowledge base when prices change, and handle escalations. If Aidan is the only person doing this and he's already stretched, the chatbot could go stale.

**Segment-specific risks**
- *Families*: Parents want quick, definitive answers ("Can my 7-year-old do karting?"). Vague responses are frustrating.
- *Young adults*: Low patience for clunky chatbots. They'll close it in seconds.
- *Corporate bookers*: High-value enquiries. If the chatbot gives a generic response instead of capturing details, that's a missed opportunity worth thousands.

---

## 2. Top 3 Chatbot Recommendations

### Recommendation 1: Tidio (with Lyro AI) -- Best if Aidan self-manages

| Detail | Info |
|--------|------|
| **Realistic cost** | £29-68/month (Starter + Lyro AI add-on) |
| **Conversation limits** | Capped per plan (100+ on Starter) |
| **Webflow integration** | JS embed, copy-paste into custom code section |
| **AI quality** | Strong (Lyro AI, stays within knowledge base) |
| **WhatsApp** | Higher plans only |
| **Live chat + bot** | Yes |
| **Ease of use** | Best of the three (9.4/10) |

**Why for Rogue:** Lowest barrier to entry, Lyro AI handles routine questions well, visual flow builder for guided paths ("Bowling / Karting / Escape Room / Corporate"), live chat handoff when AI can't handle something. Zapier integration for sending corporate leads to email/sheets.

**Limitation:** Real cost often higher than headline once you add Lyro conversations. No native WhatsApp on lower plans.

### Recommendation 2: Crisp -- Best if WhatsApp is priority

| Detail | Info |
|--------|------|
| **Realistic cost** | £80-250/month (Essentials for AI + WhatsApp) |
| **Conversation limits** | Unlimited (all plans) |
| **Webflow integration** | JS embed |
| **AI quality** | Moderate |
| **WhatsApp** | Native integration (WhatsApp Business Solution Provider) |
| **Live chat + bot** | Yes |
| **Built-in knowledge base** | Creates FAQ section AND powers chatbot |

**Why for Rogue:** Aidan prefers WhatsApp. Crisp handles WhatsApp, Instagram DMs, Facebook Messenger, and website chat in ONE inbox. Unlimited conversations (no volume surprises). Built-in knowledge base serves double duty as FAQ page and chatbot brain. Flat, predictable pricing.

**Limitation:** AI chatbot requires Essentials plan (£80/month), which is pricier than Tidio's entry point.

### Recommendation 3: Botpress -- Best if Tony builds and maintains it

| Detail | Info |
|--------|------|
| **Realistic cost** | £0-50/month (pay-as-you-go, 500 free messages) |
| **AI quality** | Strongest (uses GPT-4/Claude, most customisable) |
| **Webflow integration** | JS embed |
| **WhatsApp** | Yes (all plans) |
| **Live chat** | No (bot only, needs separate tool for human handoff) |
| **Ease for owner** | Weakest (designed for builders) |

**Why for Rogue:** Most powerful and flexible. Pay-as-you-go suits tight budgets (quiet months cost less). If Tony is maintaining it as part of a retainer, he gets full control over conversation design, AI behaviour, and integrations.

**Limitation:** Steeper learning curve. Aidan cannot easily self-maintain. No built-in live chat handoff. When message limits are reached, bots stop responding entirely.

### Summary Recommendation

- **Short-term / quick win:** Tidio (Aidan can manage, low cost, good AI)
- **If WhatsApp is non-negotiable:** Crisp (omnichannel inbox, WhatsApp native)
- **If Tony maintains as part of retainer:** Botpress (most powerful, cheapest per message)

---

## 3. Additional Chatbot Considerations

### Voice AI / AI Receptionist (Potentially Higher ROI Than Website Chatbot)

Rogue has two phone numbers. An AI phone answering service could:
- Answer calls 24/7, including closed days
- Handle routine questions (parking, pricing, age requirements)
- Transfer complex calls to humans during opening hours
- Capture caller details for callback when closed

UK providers: ClearCall, Flamingo Digital, Moneypenny -- from ~£30/month. ClearCall tests with UK regional accents. UK law (Data Use and Access Act 2025) requires "right to human" option.

**Worth discussing with Aidan:** If phone calls consume more staff time than web enquiries, an AI receptionist might solve the problem more directly than a website chatbot.

### WhatsApp and Messenger Integration

Arguably more important than the website chatbot. Aidan already said WhatsApp is his preferred channel. A WhatsApp chatbot answers "How much is bowling for 6 on Saturday?" instantly with pricing and a booking link. No staff involvement.

### Multilingual Support

Aylesbury has a diverse population (South Asian, Eastern European communities). AI chatbots respond in Polish, Urdu, Hindi, Romanian automatically because the underlying LLMs are multilingual. Essentially a free feature.

### Chatbot Data as Business Intelligence

After 3 months of operation, Rogue would have clear data on:
- Top 10 customer questions (content gaps on website)
- Which activities generate most enquiries vs. bookings (conversion intelligence)
- When enquiries peak (staffing decisions)
- What stops people booking (common objections)
- Corporate enquiry patterns (who's asking, typical group sizes)

### Birthday and Event Reminder Automation

Capture birthday dates through chatbot, build database for automated reminders 6 weeks before: "Hi, [child]'s birthday is coming up! Would you like to book a party?" Same for annual corporate events. A company that booked Christmas 2025 gets an October 2026 nudge.

### Start with FAQ Page First

A well-structured FAQ page costs nothing, improves SEO, and reduces both phone calls and chatbot load. The FAQ content becomes the knowledge base you feed into the chatbot anyway. Recommend: FAQ page first, chatbot as phase two.

---

## 4. Competitor Analysis

### Direct Competitors

#### Bowling
| Venue | Distance | Lanes | Key Advantage Over Rogue |
|-------|----------|-------|-------------------------|
| **Hollywood Bowl MK** | ~30 min | 19 (4 VIP) | £450k refurb, VIP lanes with table service, dynamic pricing, cashless arcade app, at-lane drink ordering |
| **Hollywood Bowl Reading** | ~45 min | Modern | Brand new fit-out |

**Key threat:** Hollywood Bowl is publicly listed (LSE: BOWL, £250.7m revenue). Their spend per game is up 9.2% despite volumes declining 7.5% -- they extract more per customer through premiumisation. They've converted 97% of their estate to Pins on Strings technology.

#### Go-Karting
| Venue | Distance | Track | Key Advantage Over Rogue |
|-------|----------|-------|-------------------------|
| **TeamSport Dunstable** | ~30 min | 500m, dual-level, 16 petrol karts | 4-tier membership (£7.99-34.99/yr), loyalty points (600 = free session), app, 37 UK venues, Race Academy for kids 8-15 |
| **TeamSport Reading** | ~45 min | Similar | Same franchise features |
| **K1 Speed (formerly Capital Karts)** | 40+ min | Electric | Acquired Jan 2025, pushing electric internationally |

**Key threat:** TeamSport's 500m track vs Rogue's 350m. Their membership, loyalty, and Race Academy programmes drive repeat visits. But Rogue's banked corner and flyover are locally unique.

#### Escape Rooms
| Venue | Location | Rooms |
|-------|----------|-------|
| **VIRE Aylesbury** | Town centre | 3 rooms (Medieval Doom, Forbidden Church, Haunted House) |
| **Aylesbury Escape Rooms** | Town centre | 6 rooms |
| **Escape Hunt MK** | Xscape | Multiple rooms |
| **High Wycombe Escape Rooms** | 20 min | 3 rooms (4.9/5 Google) |

**Key weakness:** Rogue has only ONE escape room ("Crazy Cat Lady"), which is a Know Escape franchise room available at multiple other locations. Not unique. Dedicated operators in Aylesbury offer 3-6 rooms.

### Indirect Competitors -- The Real Threat

#### Within Aylesbury
| Venue | Type | Notable |
|-------|------|---------|
| **Flip Out Aylesbury** | Adventure park | UK's FIRST "Super Centre". Ice skating, mini golf, laser quest, ninja tag, drift trikes, bumper cars, toddler soft play. From £5.50. |
| **VRXtra Aylesbury** | VR experiences | 15+ VR escape rooms, free-roam VR. Competes for same leisure spend. |
| **The Pin** | Indoor golf bar | 2 golf simulators, cocktails, casual vibe |
| **Aylesbury Adventure Golf** | Outdoor mini golf | Brand new 12-hole course |
| **ODEON Luxe Aylesbury** | Cinema | 6-screen, iSense 4K |
| **Zoomania** | Soft play + laser tag | Large play frame, climbing wall |
| **Stay & Play** | Soft play | New equipment, role play area |

#### Milton Keynes (Xscape) -- The Day-Out Destination
This is Rogue's single biggest competitive challenge. Under one roof at Xscape MK:

| Attraction | Type |
|------------|------|
| Hollywood Bowl MK | 19-lane bowling + VIP |
| Gravity Active | Trampolines, climbing, dodgeball |
| Snozone | UK's longest indoor slope (180m) |
| iFLY | Indoor skydiving |
| Volcano Falls | 3 themed crazy golf courses + bars + karaoke |
| Escape Hunt | Multiple escape rooms |
| Cineworld | Superscreen + 4DX |

A family going to Xscape can do bowling, trampolining, skiing, golf, escape rooms, skydiving, and eat at multiple restaurants in one trip. Rogue cannot compete on breadth but CAN compete on convenience (closer for Aylesbury residents), price, and personalised service.

### What Competitors Do Better

| Area | Competitors | Rogue |
|------|------------|-------|
| **Loyalty/Membership** | Hollywood Bowl VIP, TeamSport 4-tier membership | None |
| **Technology** | Cashless arcades, at-lane ordering, dynamic pricing, apps | Traditional, no evidence of tech upgrades |
| **VIP/Premium tier** | Hollywood Bowl VIP lanes (£2pp/game upsell) | No VIP tier |
| **Food & Beverage** | Full menus, at-lane ordering, themed bars | Pizzas, hot dogs, nachos (reviews: "limited", "overpriced") |
| **Digital presence** | Professional social media, large followings | 952 Instagram followers |
| **Corporate packages** | Dedicated pages, case studies, account management | Buried, no visible corporate page |
| **Junior programmes** | TeamSport Race Academy (ages 8-15) | No equivalent |

### Rogue's Genuine Strengths to Build On

1. **Only multi-activity leisure venue in Aylesbury** -- no other single venue offers bowling + karting + escape room + karaoke + arcade + bar
2. **Go-kart track uniqueness** -- longest indoor circuit in Bucks, dual-level with banked corner and flyover
3. **Local convenience** -- Aylesbury residents don't need to drive to MK
4. **Staff praise** -- multiple reviews highlight friendly, helpful staff
5. **Growing catchment** -- Aylesbury Vale projected for 14.2% population increase (5th highest of all 326 English local authority districts)

---

## 5. ICP Analysis

### Confirmed ICPs

#### ICP 1: Families (Kids Parties & Weekend Activities)
- **Demographics:** Parents 30-45, children 5-15
- **What they value:** Convenience (don't want to drive to MK), value for money (29% actively seek leisure discounts), multiple activities in one place, easy party packages, safety
- **Who's winning this ICP:** Hollywood Bowl MK, Flip Out Aylesbury, Gravity Active MK
- **What Rogue could do differently:** Streamlined party booking automation, post-party follow-up with rebooking incentive, birthday reminder automation

#### ICP 2: Corporates (Team Building & Events)
- **Demographics:** Local businesses, London commuter employers with Aylesbury offices, 10-50 person groups
- **What they value:** Professional booking process, bespoke packages, dietary catering, convenient location with parking
- **Market context:** Hybrid working has made in-person team building MORE important. 19% of escape room bookings are corporate.
- **Who's winning:** TeamSport, Escape Hunt MK, Xscape MK
- **What Rogue could do differently:** Corporate enquiry chatbot, automated proposal generation, corporate CRM, dedicated landing page with case studies

#### ICP 3: Young Adults (18-28, Groups & Date Nights)
- **Demographics:** Groups of 4-8 friends, couples
- **What they value:** Instagram-worthy experience, good bar, competitive socialising, modern well-maintained venue
- **Who's winning:** Volcano Falls MK, The Pin, Hollywood Bowl VIP
- **What Rogue could do differently:** Social media content automation, dynamic off-peak pricing targeting students, loyalty/points system

### Additional ICPs to Consider

#### ICP 4: Teenagers (13-17)
Too old for soft play, too young for bars. Karting and bowling are among the few activities available. Underserved segment with low competitor intensity.
- **Opportunity:** Teen-specific Friday/Saturday evening sessions, group discounts, "grown-up" birthday packages
- **Automation:** TikTok campaigns, digital consent forms for parents

#### ICP 5: Stag & Hen Parties
Aylesbury's affordability vs London is attractive. Multi-activity venue ideal for this.
- **Opportunity:** Pre-built tiered packages (Bronze/Silver/Gold), drinks packages, partnerships with local restaurants/bars for evening continuation
- **Automation:** Enquiry-to-booking automation, group payment splitting, automated itinerary generation

#### ICP 6: Schools and Youth Groups
Weekday revenue driver during term time. Schools need affordable, team-building outings.
- **Opportunity:** Schools packages with educational framing ("STEM through karting", "problem-solving through escape rooms"), youth club rates
- **Automation:** Automated risk assessment document provision, bulk booking management

#### ICP 7: Seniors / Daytime Leisure
Bowling is low-impact social activity. Daytime slots likely underutilised.
- **Opportunity:** Weekday morning bowling leagues, coffee + bowling combos, community group marketing

### ICP Priority Matrix

| Segment | Revenue Potential | Current Strength | Competitor Intensity | Automation Value |
|---------|-------------------|-----------------|---------------------|-----------------|
| Families | HIGH | MEDIUM | HIGH | HIGH |
| Corporates | HIGH (per booking) | LOW | MEDIUM | VERY HIGH |
| Young Adults 18-28 | HIGH (frequency + bar) | LOW-MEDIUM | HIGH | HIGH |
| Teenagers 13-17 | MEDIUM | MEDIUM | LOW (underserved) | MEDIUM |
| Stag/Hen | MEDIUM-HIGH | MEDIUM | MEDIUM | HIGH |
| Schools/Youth | MEDIUM (weekday fill) | LOW | LOW | MEDIUM |
| Seniors | LOW-MEDIUM | LOW | LOW | LOW-MEDIUM |

---

## 6. UK Indoor Leisure Market Trends

### What's Growing
- **Multi-activity venues** -- competitive socialising market grew ~40% in venues 2018-2023
- **Competitive socialising** -- bowling 15% popularity, mini golf 11%, pool/snooker 10%. Axe-throwing venues grew 162%, mini golf 96%. 41% of visitors now go monthly.
- **Premium/experiential** -- Hollywood Bowl's spend per game up 9.2% despite volume declining 7.5%
- **Electric go-karting** -- projected 44% of karting market by 2035, growing at 9.2% CAGR
- **Technology-led experiences** -- cashless arcades, at-lane ordering, dynamic pricing, RFID tracking

### Consumer Spending Context
- Only 13% say discretionary spending will be higher in 2026
- 54% concerned about cost of living
- BUT: experiences remain a priority. Entertainment/travel viewed as "new essentials"
- Consumers are MORE selective but still spending on leisure; they demand better value and more memorable experiences

---

## 7. Booking System Integration

### Current Systems -- Key Discovery Meeting Questions

**"Cubicle" (bowling):** Could not find this as a recognised bowling booking platform. May be niche, white-labelled, or slightly different name. Ask Aidan to show you the admin dashboard. Could be Bowling Vision, BMI Leisure, or AlleyTrak.

**"Resolver" (escape rooms):** Not found as a recognised escape room platform. Could be Resova (has API, connects with MailChimp/Google Analytics), Lockme (open API), or Bookeo. Again, ask to see the dashboard.

**Bespoke karting system:** Need to determine if this was built by a developer or is an off-the-shelf product with a custom front-end.

### Potential Unified Platform: ROLLER
- Trusted by 2,000+ attractions, London UK office
- Handles ticketing, POS, CRM, waivers, gift cards, memberships, cashless wallets
- Supports bowling, karting, and multiple activity types
- Dynamic pricing built in
- Launched AI assistant (ROLLER iQ) Nov 2025
- **Pricing:** ~£310-825/month (significant investment, phase 3/4 recommendation)

### Alternative: Clubspeed
- Designed specifically for family entertainment centres with karting and bowling
- Documented API for custom integrations
- Integrates with MyLaps timing for karting
- 24/7 phone support

---

## 8. Staff Scheduling

| Platform | UK Pricing | Best Feature |
|----------|-----------|-------------|
| **RotaCloud** | From £1/employee/month (min £10) | UK-based, drag-and-drop, real-time labour cost visibility |
| **Deputy** | From £1/user/month (min £20) | AI-powered auto-scheduling, entertainment venue specialism |
| **Planday** | From £2.99/user/month | ISO 27001, strong hospitality features |
| **Rotaready** | Quote-based | Purpose-built for leisure, integrates with EPOS and booking systems |

**Top pick:** Rotaready -- specifically built for leisure venues, integrates with booking/reservation systems (could auto-adjust staffing based on booking volumes). At 29 staff, cost would be roughly £30-175/month.

---

## 9. Compliance Digitisation

### Key Regulations
- H&S records: 5 years minimum
- Accident records: 3 years (RIDDOR)
- Equipment examination reports: until next examination or 2 years
- Go-kart specific: HSE regulations, ADIPS safety standards, documented maintenance schedules

### Digital Tools

**Trail** (£38/site/month) -- purpose-built for hospitality/leisure. Digital checklists, smart scheduling, real-time alerts, AI assistant for staff questions. 14-day free trial.

**SafetyCulture/iAuditor** -- free for 5 users, premium ~£20/user/month. Convert paper checklists to digital in minutes.

**Selling point for Aidan:** If there's ever an HSE inspection or insurance claim after an accident, digital records with timestamps, photos, and audit trails are far more defensible than paper. The go-kart maintenance documentation is especially critical.

---

## 10. Revenue Optimisation

### Dynamic Pricing
ROLLER, ActiveBooker, and Booklux all offer dynamic pricing for bowling/leisure. With bowling at 70% of revenue, even modest yield management (higher Friday/Saturday evening, lower midweek) could meaningfully impact the bottom line.

### Gift Card Digitisation
**VoucherCart** (~$40/month) -- sell services as vouchers, gift cards, or tickets. eVouchers, QR codes, NFC readers. Connects to POS and CRM. Quick win, especially around Christmas.

### Post-Visit Review Automation
Send review request 2-4 hours after visit completion. Can be done with existing email tools or through booking system if it supports it.

### Loyalty Programme
VoucherCart, Reward-it, or built into ROLLER if they adopt that platform. Physical + digital cards, QR scanning, custom app.

---

## 11. Additional Meeting Questions

### GDPR (Critical Blind Spot)
Three separate booking systems = customer data in three places. Ask:
- Unified privacy policy covering all three systems?
- Registered with ICO?
- How long is customer data retained?
- Explicit consent for marketing?

### Insurance
- Are premiums impacted by lack of documented safety procedures?
- Digital compliance records could potentially reduce premiums

### Microsoft 365 Quick Win
They have Exchange email but no SharePoint. Upgrading to M365 Business Standard (~£9.40/user/month) for management users gives central file storage, Teams, version control. ~£65-94/month for 7-10 users.

### Seasonal Patterns
- Revenue month-by-month?
- Could they open Mon-Tue for pre-booked corporate events?
- School holiday programmes?

### Partnerships
- Local restaurants (dinner + bowling packages)
- Hotels (guest recommendations)
- Schools (holiday clubs, end-of-term rewards)

### ADHD-Aware Approach for Aidan
- Visual aids over text-heavy documents
- Break into small, discrete wins
- Prioritise ruthlessly -- one "start here", not 20 options
- Written follow-ups (verbal agreements get lost)
- Quick wins first to demonstrate value
- Dashboard-driven tools, not spreadsheets

---

## 12. Suggested Meeting Agenda Items

Based on all this research, here's what to cover in the discovery meeting beyond what you'd already planned:

1. **See the booking system dashboards** -- identify the actual vendors (Cubicle, Resolver, bespoke karting), check for APIs
2. **Walk the venue** -- observe the paper checklists in situ, note which are most critical
3. **Ask about phone call volume** -- how many routine calls per week? This determines whether AI receptionist or chatbot has higher ROI
4. **Ask about corporate enquiries** -- how many per month? How are they handled? What's the close rate?
5. **Seasonal revenue patterns** -- which months are strongest/weakest? This informs dynamic pricing and marketing automation priorities
6. **Marketing current state** -- who does social media? How much time? What's the email list size?
7. **GDPR status** -- is there a privacy policy? ICO registration?
8. **Insurance** -- who's the insurer? What documentation do they require?
9. **Mon-Tue closure** -- business decision or demand-driven? Would Aidan open for guaranteed corporate bookings?
10. **Food & beverage plans** -- any plans to improve the menu? This affects dwell time and revenue per visit
11. **Escape room expansion** -- any plans for a second room? The "Crazy Cat Lady" is a franchise room available elsewhere
12. **Electric karts** -- has Aidan considered transitioning? Removes ventilation complaints, reduces maintenance, aligns with market trend

---

*This research document supports Tony Winyard's discovery meeting with Aidan at Rogue Leisure on 6 February 2026. All pricing is indicative and based on publicly available information as of February 2026.*
