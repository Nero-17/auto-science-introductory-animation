---
name: auto-science-introductory-animation
description: Turn a scientific paper or technical result into an introductory Manim animation, with adaptive audience preferences, source-grounded storyboards, narration planning, and rendered visual review. Use for scientific explainer production, not proof writing or generic slide design.
---

# Auto Science Introductory Animation

Create understandable scientific introductions through one tool-enabled assistant. This is an early instruction-based skill; use the available rendering and audio tools. Do not claim a universal production runtime or a voice service is bundled.

## Read and decide

- Read the supplied paper. Keep a claim ledger linking each proposed scientific statement to a section, equation or figure. Separate reported results, exact teaching models, approximations and speculative visual analogies.
- Inherit explicit user preferences. Consult [the 14-question bank](references/questionnaire.json) only for consequential missing choices; offer reasonable defaults and delegated choices. Do not administer all questions automatically.
- Ask only questions that the paper and session cannot resolve. For an unspecified audience, propose an undergraduate-level intuitive explanation and record the assumption. Respect the requested language, length and proof depth.
- BGM is composed and supplied by the user. Accept it later; do not ask the removed BGM preference question or source substitute music.

## Build the explanation

Read [pattern records](references/patterns.jsonl) selectively by trigger. They study 3Blue1Brown style: explanatory logic, object continuity, visual references and scene composition. They are provisional cases, not universal teaching laws. Each record links public source and narration; frame observations are in the referenced verification files in this directory's `references/` folder.

Choose a small number of methods that serve the scientific question. For each scene record: what the viewer currently understands, the question being answered, the visible operation, the expected new understanding, and the source claim it supports. Do not force all patterns into one video.

Useful decisions from the study:

- Introduce what one point means before animating trajectories in an unfamiliar space.
- Preserve a reference while comparing ordinary and exceptional behavior.
- Keep fixed quantities and changing quantities visible in multi-panel scenes.
- Drive linked geometry and labels from shared state, not independent decorative animations.
- Preserve object identity when regrouping inputs into outputs. Show a complete operation before accelerating repetition.
- Distinguish an allowed region from a probability distribution; distinguish a schematic from numerical evidence. Avoid rescaling that hides a size change central to the result.
- Upstream scenes may rely on interactive input, assets or a different Manim engine. Translate the explanatory operation into the target engine; script any interaction required for unattended rendering.

## Narrate and render

Make a short representative preview before an expensive full render when it will resolve visual or voice uncertainty. Reuse accepted choices without another approval gate.

Write narration in natural phrases, handle scientific pronunciation, and measure generated speech. Prefer timing animation around that speech. Do not routinely force narration into rigid slots by changing its speed. If no voice provider is configured, make the visual preview and clearly label any scratch voice; do not silently use a paid service.

For user-supplied BGM, mix below narration with appropriate fades and ducking. Keep narration, music and animation sources separable so one can be replaced without redoing everything.

Use a task-local environment and preserve existing installations. Report missing renderer dependencies concretely. The [boundary demo](examples/boundary-demo/README.md) is a silent Manim CE example of continuous disk geometry and a fixed zoom view, not a general paper parser.

## Review and deliver

Render and inspect actual frames. Check key states and both sides of important transitions for clipping, occlusion, readable labels, consistent identities and faithful geometry. For video seeking, allow the frame to settle and record timing discrepancies. A successful render or a text-only review does not count as visual inspection.

Use mathematical checks where meaningful: containment, shared parameter values, units, normalization or correspondence to supplied data. Decode the finished video and audio. State separately whether audio was actually listened to and whether motion was reviewed continuously or only through samples.

Fix observed problems and rerender affected scenes. Deliver the video, editable source, narration/subtitles, source attributions and a concise validation record. Distinguish technical checks from evidence that a new viewer understood the explanation. Ask focused comprehension questions when the user wants to test teaching effectiveness.
