# auto-science-introductory-animation

An early skill for turning scientific papers and technical results into introductory animations through a tool-enabled LLM assistant, with minimal manual input.

## Learning 3Blue1Brown style

We study **3Blue1Brown style**, especially explanatory progression and scene composition, using public Manim source code, narration and sampled video frames. The aim is to understand reusable teaching decisions: how a question motivates a representation, how objects remain traceable, and how a visual result becomes understandable.

This independent project is not affiliated with or endorsed by 3Blue1Brown. “Learning” means collecting and applying evidence-backed cases; no model weights have been trained.

## Version 0.1: a starting point

Included:

- A usable [SKILL.md](SKILL.md) defining the assistant workflow.
- A [14-question adaptive preference bank](references/questionnaire.json). Existing answers are reused; users need not fill out fourteen questions each time.
- [17 provisional pattern records](references/patterns.jsonl), with public source and narration references. Eight patterns have sampled visual support across eight videos and 27 observations. These are selected excerpts, not eight complete video viewings.
- An original [Manim CE boundary demo](examples/boundary-demo/README.md), adapted from a locally rendered and visually reviewed test. This repository version is silent and has no local machine paths or voice-model dependency.

Not yet complete: automated corpus ingestion, broad cross-topic evaluation, integrated high-quality voice selection, universal dependency installation, and a fully unattended paper-to-video runtime. A local prototype ran for approximately 67 seconds, but that does not establish improved learning outcomes or zero-background portability.

## Use

Place this repository in the skills directory supported by your assistant, or ask a file-capable assistant to read `SKILL.md` explicitly. Installation details depend on the host. The assistant needs access to the input paper, code execution and the chosen renderer; text-only chat cannot render video.

Example request:

> Use auto-science-introductory-animation to explain this paper to ordinary undergraduates in English. Focus on the main result and geometric intuition, without proofs. Reuse sensible defaults and render a short preview first.

The skill is Markdown-based; its instruction file does not install dependencies by itself. The included demo has its own rendering instructions.

## Product direction

- Better narration through voice auditions, pronunciation handling and natural speech timing.
- BGM composed and supplied by the user. No BGM question and no replacement music generation.
- Standard artifacts, previews, visual checks, recoverable failures and incremental rendering.
- Almost no manual setup or prompting for the eventual zero-background workflow.

## Sources and provenance

The research references [3b1b/videos](https://github.com/3b1b/videos), snapshot `674b966fbb6cf0307590d27744d186165e8b6a76`, and [3b1b/captions](https://github.com/3b1b/captions), snapshot `9aef876b0ed62ce4f099c0a2f0e7a52e8d1058c9`. Verification records distinguish observations from inferred teaching rationale and untested effectiveness. One Bayes frame has inconsistent player timing, recorded explicitly.

The upstream video-source repository identifies CC BY-NC-SA 4.0, distinct from the Manim engine's license. This repository does not bundle upstream scene code, full transcripts, videos or character assets. Its example scene is original. No project-wide redistribution license has been selected yet; upstream references retain their respective terms.

Private manuscripts, credentials, voice models, BGM and rendered media are not included in this initial repository.
