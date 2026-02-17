# Pattern: Setting Up MCP Servers for Claude Code

#tech #integrations

## What it is
Connecting external tools and data sources to Claude Code via MCP (Model Context Protocol) servers, so Claude can read from them during sessions.

## When to use
When Aidan wants Claude to automatically access data from an external tool (meeting notes, voice ideas, booking system data, etc.) without manual copy-paste.

## How to do it

### For remote/cloud APIs with official MCP support (e.g. Granola)
Add to `rogueleisure/.mcp.json`:
```json
{
  "mcpServers": {
    "server-name": {
      "type": "http",
      "url": "https://mcp.example.com/mcp"
    }
  }
}
```
Then authenticate via OAuth on first Claude Code session start.

### For local data sources without an API (e.g. Wispr Flow SQLite)
1. Write a Python MCP server using `mcp` package (`pip install mcp`)
2. Use `FastMCP` from `mcp.server.fastmcp` for simplicity
3. Copy the DB to a temp file before reading (avoids locking errors)
4. Add to `.mcp.json` with `command`/`args` instead of `url`
5. Server starts on-demand via stdio — no persistent daemon needed

### Key files
- `.mcp.json` — project-level, commits to Git, syncs to both laptops
- `aidan-claude-setup/wispr-mcp/server.py` — example local MCP server
- `aidan-claude-setup/wispr-mcp/requirements.txt` — `mcp>=1.26.0`

## Why it works
Claude Code automatically detects `.mcp.json` at session start and offers to connect the servers. Once approved, MCP tools are available in every session without any extra setup. The `.mcp.json` lives in the Git repo so both laptops get the same config automatically.

## Gotchas
- `mcpServers` does NOT go in `settings.local.json` — that schema doesn't support it. Use `.mcp.json` instead.
- Local servers using SQLite: always copy DB + WAL + SHM files together to temp before connecting, or you'll get locking errors while the app is running.
- After Google Drive migration, update hardcoded paths in `args` from `OneDrive` to `My Drive`.
- Remote MCP servers (like Granola) need OAuth auth on first use — Claude will prompt for it.
