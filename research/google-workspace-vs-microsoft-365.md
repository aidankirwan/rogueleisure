# Google Workspace vs Microsoft 365: Comparison for Rogue Leisure

**Date:** 7 February 2026
**Context:** Rogue currently uses Exchange for email (10 accounts). Need to decide whether to migrate to Google Workspace or upgrade to full Microsoft 365.

---

## UK Pricing (per user/month, excl. VAT, annual commitment)

### Google Workspace

| Plan | Price | Storage | Key Additions |
|------|-------|---------|---------------|
| **Business Starter** | **£5.90** | 30 GB/user | Gmail, Drive, Docs, Sheets, Forms, Meet (100 ppl), Chat, Calendar, Gemini AI |
| **Business Standard** | **£11.80** | 2 TB/user (pooled) | + Shared Drives, recorded meetings, NotebookLM, expanded Gemini |
| **Business Plus** | **£18.40** | 5 TB/user (pooled) | + eDiscovery, advanced endpoint management, AI Drive classification |

### Microsoft 365

| Plan | Price | Storage | Key Additions |
|------|-------|---------|---------------|
| **Exchange Online Plan 1** | **£3.60** | 50 GB mailbox | Email only. No Office apps, no Teams, no OneDrive. |
| **Business Basic** | **£4.60** | 1 TB/user | Web Office apps, Teams, OneDrive, Forms, Planner, Bookings |
| **Business Standard** | **£9.60** | 1 TB/user | + **Desktop** Word, Excel, PowerPoint, Outlook apps |
| **Business Premium** | **£16.90** | 1 TB/user | + Defender, Purview data protection, advanced security |

**Note:** Microsoft is raising prices in July 2026 (~17% on Business Basic, ~12% on Business Standard).

---

## Cost Modelling for Rogue Leisure

Assumptions: 10 users need email. 19 other staff access forms/checklists on tablets (no licence needed on either platform).

### Scenario A: Google Workspace Business Starter (Recommended)

| Item | Users | Per User | Monthly Total |
|------|-------|----------|---------------|
| Google Workspace Starter | 10 | £5.90 | **£59.00** |
| **Annual total** | | | **£708.00** |

### Scenario B: Microsoft 365 Business Basic

| Item | Users | Per User | Monthly Total |
|------|-------|----------|---------------|
| M365 Business Basic | 10 | £4.60 | **£46.00** |
| **Annual total** | | | **£552.00** |

### Scenario C: Microsoft 365 with Desktop Apps (what Aidan needs)

Staff need Word but don't have it. To get desktop Word, Excel, PowerPoint:

| Item | Users | Per User | Monthly Total |
|------|-------|----------|---------------|
| M365 Business Standard | 5 (managers) | £9.60 | £48.00 |
| M365 Business Basic | 5 (others) | £4.60 | £23.00 |
| **Total** | 10 | | **£71.00** |
| **Annual total** | | | **£852.00** |

### Scenario D: Current Exchange Standalone

| Item | Users | Per User | Monthly Total |
|------|-------|----------|---------------|
| Exchange Online Plan 1 | 10 | £3.60 | **£36.00** |
| Office apps | 0 | N/A | £0.00 (not purchased) |
| **Annual total** | | | **£432.00** |

**Key insight:** Google Workspace at £59/month includes Docs, Sheets, and Slides (free productivity apps). Microsoft at £46/month gives only web versions of Office; desktop apps cost £9.60/user. For a team that needs document editing, Google is cheaper overall.

---

## Key Differences for a Leisure Venue

### File Storage and Sharing
- **Google Drive** is simpler for non-technical staff. Intuitive sharing, clean interface.
- **SharePoint** is more powerful but significantly more complex. Multiple admin portals.
- **Winner: Google** (for a team without IT staff)

### Forms and Checklists
- **Google Forms** is simpler, faster to create, easier for managers to build and edit. Responses auto-populate Google Sheets.
- **Microsoft Forms** is competent but slightly less intuitive.
- Rogue's entire compliance system is already specced for Google Forms.
- **Winner: Google** (and the work is already done)

### Email
- Both provide business-class email with custom domains.
- Gmail is browser-first; clean, simple, works identically everywhere.
- Outlook has a stronger desktop app (but only in Business Standard at £9.60).
- **Winner: Tie** (both excellent)

### Admin Simplicity
- Google has **one admin console**. Clean, straightforward.
- Microsoft has **multiple admin portals** (M365 Admin, Exchange Admin, Azure AD, SharePoint Admin).
- **Winner: Google** (significantly easier for a non-technical owner)

### Mobile / Tablet Access
- Both work well on mobile. Google apps are lighter and more browser-friendly.
- The checklist system runs in a browser on Samsung tablets.
- Staff more likely to already have a Google account on their phone.
- **Winner: Google** (slight edge)

### Existing Google Usage
- H&S person already uses Google Drive for compliance docs.
- Google Forms specs already built for four compliance forms.
- **Winner: Google** (no migration needed for existing data)

---

## Migration Considerations

### Exchange to Google Workspace
- Google provides **GWMME** (free migration tool) for email, calendar, contacts.
- Admin runs it centrally; staff don't need to do anything.
- 10 mailboxes: a few hours to a day.
- Can run in parallel (keep Exchange running during migration, switch DNS when ready).
- Outlook rules need recreating as Gmail filters. Distribution lists become Google Groups.

### Running Both in Parallel (Not Recommended)
- Only one system can receive incoming email (one MX record holder).
- Calendar sync between Exchange and Google Calendar needs third-party tools.
- Doubles admin overhead. Doubles cost.
- Pick one ecosystem and commit.

---

## Recommendation

**Google Workspace Business Starter at £5.90/user/month for 10 users (£59/month + VAT).**

Rationale:
1. Cheaper than Microsoft when you factor in the Office apps Aidan needs but hasn't bought
2. Simpler to administer without IT staff
3. H&S person already on Google Drive
4. Entire compliance system designed around Google Forms and Sheets
5. Aidan said he's "quite happy to rip everything up and use a system that's potential"
6. Tony (consultant) is more familiar with Google ecosystem for ongoing support

The only scenario where Microsoft wins is if Rogue had heavy spreadsheet users who genuinely needed desktop Excel (complex macros, pivot tables). Their manual Excel bookkeeping doesn't qualify.

---

*Researched 7 February 2026. Prices may change; Microsoft increase announced for July 2026.*
