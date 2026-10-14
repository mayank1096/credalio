# Credalio · full project history

The full build log (every generator, blob id, past decision; the old 49 KB CLAUDE.md) is kept in git, not loaded every session.

Read it with:

    git show 4293dcc:CLAUDE.md > /tmp/history.md    # then grep /tmp/history.md for what you need

(If the clone is too shallow: `git fetch --depth=200 origin` first.)
Grep it for a detail (generator name, blob id, past decision); never read it whole. Rules in /CLAUDE.md win over anything in it.
