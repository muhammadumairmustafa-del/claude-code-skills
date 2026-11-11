# Extra AI-writing patterns (supplement)

Paraphrased and condensed from blader/humanizer v3.1.0 (https://github.com/blader/humanizer, MIT; license copy in `humanizer-LICENSE.txt`). Use after the main no-ai-slop pass. Each item: what to look for, then the fix.

1. **Forced triads.** Ideas grouped in threes because three sounds complete ("innovation, inspiration, and insights"), at sentence or paragraph scale. Keep the number of items the meaning actually has.
2. **Arguing with no one.** "I'm not saying...", "To be clear...", "Don't get me wrong", "A tempting approach would be..." rebutting a claim nobody made. Delete the defense; keep only a real claim or a real objection that appears elsewhere.
3. **Sayings that sound deep.** "At its core", "the real question is", "X is the Y of Z", "not a tool but a mirror". Replace with the specific claim.
4. **Promotional travel-brochure tone.** "Nestled in", "vibrant", "rich heritage", "breathtaking", "must-visit". Say what the thing is.
5. **Prestige lists as evidence.** A list of outlets, follower counts, or "featured in" logos standing in for what was actually said. Keep the one source the reader can check.
6. **Bold-label lists.** Every bullet starts with a bold label and colon that repeats the sentence. Merge into prose when the labels add nothing.
7. **Decorative headings.** Title Case On Every Word, emoji or arrows in headings, a rule between every section. Use sentence case and plain headings.
8. **Curly quotes in plain-text targets.** Weak on its own; match the target format (straight quotes in code, Markdown source, JSON).
9. **Chatbot residue.** "Great question!", "I hope this helps", "Let me know if...", "Here is a...". Remove the wrapper, keep the content.
10. **Knowledge-limit disclaimers and guesses.** "As of my last update", "while details are limited... it likely...". State what the source does not show, or cut it. Never fill the gap with a plausible guess.
11. **Heading echo.** A heading followed by a one-line sentence restating it. Delete the echo.
12. **Writing about the document.** "This section was added to replace...", "compiled from...". Describe the subject, except in changelogs, release notes, and migration guides.
13. **Re-explaining what the reader knows.** In a reply, rebuilding the whole background before the decision. Lead with the decision and the one fact the reader lacks.

## When not to act
Leave a pattern alone inside a quotation, a title, a proper name, or text that discusses the pattern. Keep specific odd details, mixed feelings, era-bound references, and genuine asides: they carry the writer's voice.
