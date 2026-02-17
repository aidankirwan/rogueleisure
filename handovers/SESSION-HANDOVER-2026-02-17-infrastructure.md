# Session Handover — 2026-02-17 — Infrastructure & Integrations

## What We Did

Long infrastructure session focused on setting up Claude Code properly across two laptops and integrating Granola and Wispr Flow.

### 1. Cross-device sync strategy
- Confirmed: rogueleisure repo already on OneDrive, which syncs both laptops. Setup is correct.
- **Upcoming action:** Install Google Drive for Desktop and migrate repo from OneDrive before cancelling Microsoft 365/Exchange. Path will change from `C:\Users\aidan\OneDrive\Documents\Github\rogueleisure\` to `C:\Users\aidan\My Drive\Github\rogueleisure\` (exact path TBC after installation).
- Key gate: verify `@rogueleisure.co.uk` email DNS points to Google Workspace before cancelling Exchange.

### 2. Granola MCP (meeting notes)
- Created `.mcp.json` in repo root with official Granola MCP: `https://mcp.granola.ai/mcp`
- Granola stores notes in cloud (Supabase), not locally — official remote MCP is the only clean approach.
- First session start: Claude will prompt to authenticate via OAuth.
- Added "After Meetings" workflow to CLAUDE.md.

### 3. Wispr Flow MCP (voice ideas)
- Built `aidan-claude-setup/wispr-mcp/server.py` — Python MCP server reading `flow.sqlite` directly.
- DB at: `C:\Users\aidan\AppData\Roaming\Wispr Flow\flow.sqlite` (169 entries, going back 10 Feb 2026).
- Tools: `list_recent_dictations`, `get_dictation`, `search_dictations`, `get_idea_candidates`, `list_flow_notes`.
- Phone sync limitation confirmed: phone dictations do NOT sync content to desktop DB. Only Flow Notes sync. Aidan needs to use Wispr Flow Notes on iPhone for ideas he wants captured.
- Added Wispr entry to `.mcp.json` and added workflow section to CLAUDE.md.
- `mcp` package installed: `pip install mcp` (v1.26.0).

## What Still Needs Doing (Aidan's Actions)
1. Install Google Drive for Desktop on both laptops
2. Move rogueleisure repo to new Google Drive path
3. Update `.mcp.json` server path for wispr after migration
4. Cancel Microsoft 365 (after confirming above)
5. Authenticate Granola MCP (OAuth) on next Claude Code session start
6. Approve Wispr MCP on next Claude Code session start
7. Start using Wispr Flow Notes on iPhone for capturing ideas

## Files Changed This Session
- `rogueleisure/.mcp.json` (created)
- `rogueleisure/.claude/CLAUDE.md` (added Granola + Wispr sections)
- `rogueleisure/aidan-claude-setup/wispr-mcp/server.py` (created)
- `rogueleisure/aidan-claude-setup/wispr-mcp/requirements.txt` (created)
- `rogueleisure/aidan-claude-setup/second-brain/patterns/mcp-server-setup.md` (created)
- `rogueleisure/docs/CHANGELOG.md` (updated)
- `rogueleisure/docs/ROADMAP.md` (updated)

## Next Session
Pick up with Google Drive migration, then test both MCP connections.
