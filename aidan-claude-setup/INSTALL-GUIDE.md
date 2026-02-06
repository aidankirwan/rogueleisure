# Installing Claude Code for Aidan (Tuesday Checklist)

## Before You Arrive

Make sure:
- [ ] The `rogue-leisure` GitHub repo is set up and pushed (done)
- [ ] Aidan has created a GitHub account (or you'll do it together)
- [ ] You've added Aidan as a collaborator on the repo
- [ ] This `aidan-claude-setup` folder is on a USB stick or accessible from your laptop

## On Aidan's Computer

### Step 1: Install Prerequisites (5 min)

1. Check if Node.js is installed: open Terminal, type `node --version`
2. If not installed, download from https://nodejs.org (LTS version)
3. Install Claude Code: `npm install -g @anthropic-ai/claude-code`

### Step 2: Copy Claude Config (5 min)

1. Copy the `.claude/` folder from this bundle to Aidan's home directory:
   ```
   cp -r .claude/ ~/
   ```
   This gives him: CLAUDE.md (global instructions) and 5 skills (interview, socratic-strategist, content-writer, testimonial-manager, call-prep)

2. Copy the `second-brain/` folder:
   ```
   cp -r second-brain/ ~/
   ```

### Step 3: Install GitHub Desktop (5 min)

1. Download from https://desktop.github.com
2. Sign in with Aidan's GitHub account
3. Clone the `rogue-leisure` repo to `~/projects/rogue-leisure/`

### Step 4: Set Up Claude Pro (10 min)

1. Go to claude.ai
2. Sign up for Claude Pro (£18/month)
3. Create a Project called "Rogue Leisure"
4. Add custom instructions (copy from the project instructions below)
5. Upload key documents as Project Knowledge:
   - `deliverables/implementation-plan-2026-02-06.md`
   - `meetings/meeting-notes-2026-02-06-cleaned.md`
   - `audio-briefings/audio-briefing-competitors.md`

### Step 5: Test Claude Code (5 min)

1. Open Terminal
2. Navigate to the project: `cd ~/projects/rogue-leisure`
3. Run: `claude`
4. Try: "What do you know about this project?"
5. Verify it reads the .claude/CLAUDE.md and knows about Rogue Leisure

### Step 6: Run First Interview Session (20-30 min)

1. In Claude Code, type: `/interview`
2. Start with "You and the Business" category
3. Let Aidan answer naturally. Follow tangents.
4. After 20-30 minutes, tell Claude to save the output to `context/business-profile.md`
5. Show Aidan how to continue on his own later

### Step 7: Quick Content Win (5 min)

1. Ask Claude to write a social media post about something that happened today
2. Show Aidan how the content-writer skill shapes the tone
3. Post it to Facebook/Instagram right there and then

---

## Claude Pro Project Instructions (Copy-Paste)

```
You are helping Aidan, owner of Rogue Leisure (bowling, go-karting, escape rooms in Aylesbury, Bucks). He has ADHD and prefers short, direct answers. Use British English. No jargon.

Key facts:
- 40,000 sq ft venue at The Point, Gatehouse Way, Aylesbury
- 14-lane bowling (70% revenue), 350m dual-level go-kart track (25%), Crazy Cat Lady escape room (5%)
- 29 staff (22 zero-hour), breakeven £80k/month, closed Mon-Tue
- Key people: Dawn (manager), Doris (bar), Pete (karting), Jane (web developer)
- Systems: Google Workspace, Webflow website, 3 booking systems
- Tony Winyard (AI consultant, tony@tonywinyard.com) is helping with technology and automation

For emails and customer responses: warm, friendly, local. Not corporate.
For social media: fun, authentic, real people and real stories. Not polished Canva graphics.
Keep answers short and actionable. One thing at a time.
```

---

## After the Visit

- [ ] Aidan can open Claude Code and ask a question
- [ ] Aidan can open Claude Pro (claude.ai) and ask a question
- [ ] GitHub Desktop is syncing the rogue-leisure repo
- [ ] At least one interview session output is saved to `context/`
- [ ] Aidan has posted one social media piece written with Claude
