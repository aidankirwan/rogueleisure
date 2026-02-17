"""
Wispr Flow MCP Server
Reads dictation history and Flow Notes from the local Wispr Flow SQLite database.
"""

import sqlite3
import shutil
import tempfile
import os
import json
from datetime import datetime, timezone, timedelta
from mcp.server.fastmcp import FastMCP

DB_PATH = os.path.expandvars(r"%APPDATA%\Wispr Flow\flow.sqlite")

# Apps where dictation is clearly purposeful work input (not standalone ideas)
WORK_APPS = {
    "claude", "gmail", "msedge", "chrome", "WINWORD",
    "outlook", "excel", "sheets", "docs", "SearchHost",
}

mcp = FastMCP("wispr")


def get_db_connection() -> sqlite3.Connection:
    """Copy the DB to a temp file to avoid locking, then connect."""
    wal = DB_PATH + "-wal"
    shm = DB_PATH + "-shm"
    tmp = os.path.join(tempfile.gettempdir(), "wispr_mcp_read.db")
    shutil.copy2(DB_PATH, tmp)
    if os.path.exists(wal):
        shutil.copy2(wal, tmp + "-wal")
    if os.path.exists(shm):
        shutil.copy2(shm, tmp + "-shm")
    conn = sqlite3.connect(tmp)
    conn.row_factory = sqlite3.Row
    return conn


def format_entry(row: sqlite3.Row) -> dict:
    return {
        "id": row["transcriptEntityId"],
        "timestamp": row["timestamp"],
        "app": row["app"],
        "platform": row["platform"],
        "num_words": row["numWords"],
        "text": row["formattedText"] or row["asrText"] or "",
    }


@mcp.tool()
def list_recent_dictations(hours: int = 24, app: str = None) -> str:
    """
    List recent Wispr Flow dictations from the desktop history.

    Args:
        hours: How many hours back to look (default 24)
        app: Optional filter by app name (e.g. 'claude', 'Wispr Flow', 'chrome')
    """
    since = datetime.now(timezone.utc) - timedelta(hours=hours)
    since_str = since.strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db_connection()
    try:
        if app:
            rows = conn.execute(
                """
                SELECT transcriptEntityId, timestamp, app, platform, numWords,
                       formattedText, asrText
                FROM History
                WHERE timestamp >= ? AND app = ? AND formattedText IS NOT NULL
                ORDER BY timestamp DESC
                """,
                (since_str, app),
            ).fetchall()
        else:
            rows = conn.execute(
                """
                SELECT transcriptEntityId, timestamp, app, platform, numWords,
                       formattedText, asrText
                FROM History
                WHERE timestamp >= ? AND formattedText IS NOT NULL
                ORDER BY timestamp DESC
                """,
                (since_str,),
            ).fetchall()
    finally:
        conn.close()

    if not rows:
        return f"No dictations found in the last {hours} hours" + (f" for app '{app}'" if app else "") + "."

    entries = [format_entry(r) for r in rows]
    return json.dumps(entries, indent=2, ensure_ascii=False)


@mcp.tool()
def get_dictation(dictation_id: str) -> str:
    """
    Get the full text of a specific Wispr Flow dictation by its ID.

    Args:
        dictation_id: The transcriptEntityId of the dictation
    """
    conn = get_db_connection()
    try:
        row = conn.execute(
            """
            SELECT transcriptEntityId, timestamp, app, platform, numWords,
                   formattedText, asrText, url, editedText
            FROM History
            WHERE transcriptEntityId = ?
            """,
            (dictation_id,),
        ).fetchone()
    finally:
        conn.close()

    if not row:
        return f"No dictation found with ID: {dictation_id}"

    result = {
        "id": row["transcriptEntityId"],
        "timestamp": row["timestamp"],
        "app": row["app"],
        "platform": row["platform"],
        "num_words": row["numWords"],
        "url": row["url"],
        "formatted_text": row["formattedText"] or "",
        "edited_text": row["editedText"] or "",
        "raw_asr": row["asrText"] or "",
    }
    return json.dumps(result, indent=2, ensure_ascii=False)


@mcp.tool()
def search_dictations(query: str, hours: int = 168) -> str:
    """
    Search Wispr Flow dictation history for a keyword or phrase.

    Args:
        query: Text to search for (case-insensitive)
        hours: How many hours back to search (default 168 = 1 week)
    """
    since = datetime.now(timezone.utc) - timedelta(hours=hours)
    since_str = since.strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db_connection()
    try:
        rows = conn.execute(
            """
            SELECT transcriptEntityId, timestamp, app, platform, numWords,
                   formattedText, asrText
            FROM History
            WHERE timestamp >= ?
              AND formattedText IS NOT NULL
              AND lower(formattedText) LIKE lower(?)
            ORDER BY timestamp DESC
            """,
            (since_str, f"%{query}%"),
        ).fetchall()
    finally:
        conn.close()

    if not rows:
        return f"No dictations found matching '{query}' in the last {hours} hours."

    entries = [format_entry(r) for r in rows]
    return json.dumps(entries, indent=2, ensure_ascii=False)


@mcp.tool()
def get_idea_candidates(hours: int = 48) -> str:
    """
    Return Wispr Flow dictations that are likely to be standalone ideas rather than
    work input typed into a specific tool. These are dictations made:
    - Inside the Wispr Flow app itself (Flow Notes or quick capture), OR
    - In apps not classified as standard work tools

    Args:
        hours: How many hours back to look (default 48)
    """
    since = datetime.now(timezone.utc) - timedelta(hours=hours)
    since_str = since.strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db_connection()
    try:
        rows = conn.execute(
            """
            SELECT transcriptEntityId, timestamp, app, platform, numWords,
                   formattedText, asrText
            FROM History
            WHERE timestamp >= ?
              AND formattedText IS NOT NULL
            ORDER BY timestamp DESC
            """,
            (since_str,),
        ).fetchall()
    finally:
        conn.close()

    candidates = []
    for row in rows:
        app = row["app"] or ""
        # Include if it's a Wispr Flow app entry or not in a standard work tool
        if app == "Wispr Flow" or app not in WORK_APPS:
            candidates.append(format_entry(row))

    if not candidates:
        return f"No idea candidates found in the last {hours} hours."

    return json.dumps(candidates, indent=2, ensure_ascii=False)


@mcp.tool()
def list_flow_notes() -> str:
    """
    List all Wispr Flow Notes (synced notes from the Wispr app, including from iPhone
    if dictated into Flow Notes on mobile).
    """
    conn = get_db_connection()
    try:
        rows = conn.execute(
            """
            SELECT id, title, contentPreview, content, createdAt, modifiedAt
            FROM Notes
            WHERE isDeleted = 0 OR isDeleted IS NULL
            ORDER BY modifiedAt DESC
            """,
        ).fetchall()
    finally:
        conn.close()

    if not rows:
        return (
            "No Flow Notes found. To capture phone ideas that sync here: open the "
            "Wispr Flow app on iPhone and dictate into Flow Notes (not into another app)."
        )

    notes = []
    for row in rows:
        notes.append({
            "id": row["id"],
            "title": row["title"],
            "preview": row["contentPreview"],
            "content": row["content"],
            "created": row["createdAt"],
            "modified": row["modifiedAt"],
        })
    return json.dumps(notes, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    mcp.run()
