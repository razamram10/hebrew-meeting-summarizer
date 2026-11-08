# Hebrew meeting summarizer

I built a Hebrew meeting workflow for Polyben that turns a recording into a decision log and follow-up tasks. Vibe handles local transcription, an AI assistant organizes the transcript, and Python renders the reviewed notes for sharing.

## Try the portfolio demo

Compare [the fictional transcript](transcript.md) with [the expected summary](summary.md). To try a different conversation, give a Hebrew transcript and the instructions in [AGENTS.md](AGENTS.md) to your assistant. Review the resulting Markdown against the transcript. Run the following command with Python 3 to generate a standalone right-to-left HTML page.

    python render.py summary.md

Open summary.html in a browser. The renderer uses the Python standard library. This public example starts after transcription and includes a compact renderer prepared for the demo.

## What to check

The speaker agrees to a pilot and volunteers to prepare a draft by Tuesday. A launch date is discussed but never agreed. A good summary preserves that distinction and the named owner.
