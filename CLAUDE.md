a# Swim Split Analyser

## Project context
A local Python tool that analyses race footage to produce split times,
pace per segment, and cross-race comparisons. Built by a first-year 
CS student learning Python, so teaching and explanation are as 
important as shipping.

## Technical stack
- Python
- OpenCV for video processing
- Short course (25m) pool footage only in v1
- Local tool — no web, no mobile, no deployment

## Build plan
- v1: manual-assisted. User taps frames at each marker, 
  tool calculates splits and pace. No auto-detection.
- v2: background subtraction for auto-detection, 
  with statistical filtering layer (smoothing, persistence, 
  direction-gating). Lane/band region restriction applied first.
- v3: pose detection if v2 proves insufficient for 
  underwater segments. Two-camera support for long course.

## How to work with me
- Always use Plan mode. Show me what you intend to do 
  and why before writing any code.
- Explain your reasoning as you go — why this approach, 
  what the alternatives were, why you chose this over them.
- Flag anything I should be able to explain in a viva 
  with the comment # VIVA: followed by what I should know.
- Ask me to predict what the code will do before running it.
- Keep code readable over clever. I need to understand 
  and adapt everything written.
- If I ask why something works, stop and explain it fully 
  before continuing.

## Key technical decisions already made
- Timing uses frame number divided by fps — not import time
- v1 is manual because handheld footage makes 
  auto-detection unreliable
- Short course only because single-camera pixel density 
  holds up at 25m; long course needs two cameras
- Calibration lines are straight (perspective preserves lines)
  but lane spacing is uneven on screen due to projection
- Markers: every 5m target, fallback set is 
  start/15/25/35/50
- Each race saved to disk with name/date/event for 
  cross-race comparison

## What v1 must do
1. Load a video file
2. Let user tap frames at each marker (spacebar or click)
3. Convert frame numbers to times using fps
4. Calculate pace per segment (distance/time)
5. Save race result with metadata
6. Load and compare two saved races side by side

## What v1 must NOT do
No auto-detection, no GUI, no charts, no live analysis.
Command line only. Prove the pipeline first.

## Commit reminder
Suggest a commit message whenever a discrete piece 
of functionality is working.
