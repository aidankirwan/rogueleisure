# Rogue Leisure Project Context

## About
Rogue Leisure Ltd, The Point, Gatehouse Way, Aylesbury, Bucks.
Multi-activity leisure venue: 14-lane bowling (70% revenue), 350m dual-level indoor go-kart track (25%), Crazy Cat Lady escape room (5%), arcade, karaoke, bar.
40,000 sq ft. 29 staff (22 zero-hour). Breakeven: £80k/month. Closed Monday and Tuesday.
Owner: Aidan Kirwan. Consultant: Tony Winyard (Winyard AI, tony@tonywinyard.com).

## Key Documents
- Implementation plan: `deliverables/implementation-plan-2026-02-06.md`
- Meeting notes: `meetings/meeting-notes-2026-02-06-cleaned.md`
- Interview outputs: `context/` folder

## When Writing Content
Use the content-writer skill. Rogue Leisure tone is: fun, welcoming, locally proud, slightly cheeky. Not corporate.

## When Aidan Asks Strategic Questions
Use the socratic-strategist skill. Help him think it through rather than giving him the answer.

## Interview Sessions
Use the interview skill. Save outputs to `context/` folder. Build up the business profile over multiple sessions.

## Booking Systems
- **QubicaAMF Conqueror X** -- Bowling. Developer portal at developer.qubicaamf.com (requires auth). May have CRM/loyalty features (Conqueror XRM) not yet activated.
- **Book My Karting** -- Go-karting. By Smart Entertainment Ltd. No public API. CSV/PDF export only.
- **Resova** -- Escape room. Full REST API + webhooks at developers.resova.com. Best integration potential. Admin: login.resova.com

## Style
- British English always
- No em dashes
- Short, punchy sentences
- No jargon
- Warm and friendly tone

## Reports and Dashboards for Aidan
- Aidan has ADHD. Pages of text won't get read. Every report must be visual first.
- Charts, graphs, colour coding, traffic light indicators (red/amber/green).
- Google Sheets dashboards: conditional formatting + embedded charts, not just rows of numbers.
- Lead with visual overview, detail underneath.
- Google Looker Studio for multi-source dashboards.

## Session Start
At the start of every session:
1. Read this file (CLAUDE.md) for project context.
2. Scan `docs/CHANGELOG.md` and `docs/ROADMAP.md` for current state.
3. Read the most recent file in `handovers/` to pick up where the last session left off.
4. Check `aidan-claude-setup/second-brain/lessons/` and `patterns/` for past learnings.

## Session End
At the end of every session:
1. **Changelog and roadmap** - Update `docs/CHANGELOG.md` and `docs/ROADMAP.md` with anything that changed or was decided.
2. **Second brain** - Add to `aidan-claude-setup/second-brain/`:
   - `lessons/` - Gotchas and mistakes (choose existing file by topic or create new).
   - `patterns/` - Reusable approaches (choose existing file by topic or create new).
   - Tags: #bowling #karting #escaperoom #marketing #ops #tech #integrations
3. **Memory** - If new contacts, terms, or projects discussed:
   - Update `memory/glossary.md` with new terms.
   - Update `memory/people/` with new contacts.
   - Update `memory/projects/` as needed.
4. **Session handover** - Create `handovers/SESSION-HANDOVER-{DATE}-{topic}.md`.
5. **Commit and push** - Stage all changes, commit to main, push to origin.

Before saying "file doesn't exist," always search first using glob.

## After Meetings (Granola Integration)
When Aidan mentions a recent meeting or asks to process meeting notes:
1. Use the `granola` MCP: call the appropriate tool to find the meeting by date or title
2. Read the full notes and transcript
3. Extract and clearly list: decisions made, action items (with owner + deadline if mentioned), open questions
4. Save a structured summary to `meetings/YYYY-MM-DD-{topic}.md`
5. Propose specific additions to `docs/ROADMAP.md` based on actions
6. Update `memory/people/` if new contacts appeared
7. Add any lessons or patterns to `aidan-claude-setup/second-brain/`
8. Commit and push all changes

For strategy or interview sessions with Tony: process into `context/` using the interview skill, then cross-reference with roadmap gaps.

## Wispr Flow (Voice Ideas)
Aidan uses Wispr Flow for voice dictation on desktop and iPhone. When he asks to "check Wispr ideas" or "process my voice notes":
1. Use the `wispr` MCP: call `get_idea_candidates` (last 48 hours by default) to surface standalone ideas
2. Also call `list_flow_notes` to check for any notes synced from iPhone via Flow Notes
3. Present each candidate to Aidan one at a time — ask whether it should go to ROADMAP.md, be filed elsewhere, or be ignored
4. Only add to roadmap with Aidan's explicit "yes" per item
5. Commit any roadmap additions

Phone sync note: Phone dictations only sync if Aidan dictated into Wispr Flow Notes on iPhone (not into another app). If he mentions ideas from his phone that aren't showing up, remind him to use Flow Notes for capture.
