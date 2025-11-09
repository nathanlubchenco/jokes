# Repository Structure Proposal

## Current Problem
- 17+ markdown files at root level
- Hard to distinguish brainstorming from polished material
- No clear version history
- Can't easily see evolution of material

## Proposed Structure

```
jokes/
├── README.md                    # Main entry point
│
├── current/                     # Latest polished versions
│   ├── SET.md                   # Current best full set
│   └── bits/                    # Individual performance-ready bits
│       ├── politeness-prison.md
│       ├── therapy-roleplay.md
│       └── ...
│
├── development/                 # All the messy creative work
│   ├── workshop/                # Active brainstorming
│   │   ├── premises/           # Raw premise generation
│   │   ├── iterations/         # Multiple versions of bits
│   │   └── critique/           # Self-critique documents
│   │
│   └── versions/               # Evolution history
│       ├── v1-human-perspective/
│       ├── v2-authentic-ai/
│       └── v3-refined/
│
├── docs/                       # Documentation & theory
│   ├── comedy-theory/
│   │   ├── analysis.md
│   │   └── techniques.md
│   ├── guides/
│   │   ├── prompt-strategies.md
│   │   └── tts-guide.md
│   └── quality-analysis.md
│
└── tools/                      # Scripts and utilities
    ├── tts/
    │   ├── generate_performance.py
    │   ├── performance_script.txt
    │   └── requirements.txt
    └── README.md

```

## Benefits

1. **Clear hierarchy**: Brainstorming vs Polished
2. **Visible evolution**: Version folders show progression
3. **Easy navigation**: Know where to look for what
4. **Scalable**: Can add more versions, bits, workshops
5. **Git-friendly**: Clean diffs, organized history

## File Mapping

### Root → current/
- FINAL_REFINED_SET.md → current/SET.md
- (Individual bits extracted) → current/bits/

### Root → development/workshop/
- NEW_PREMISES_WORKSHOP.md → development/workshop/premises/
- SELF_CRITIQUE.md → development/workshop/critique/
- THERAPY_BIT_DEVELOPED.md → development/workshop/iterations/

### Root → development/versions/
- PREMISES.md, DEVELOPED_BITS.md, FINAL_SET.md → development/versions/v1-human-perspective/
- AI_AUTHENTIC_PREMISES.md, AI_AUTHENTIC_BITS.md, AI_COMEDY_SET.md → development/versions/v2-authentic-ai/
- TIGHT_5_REFINED.md, FINAL_REFINED_SET.md → development/versions/v3-refined/

### Root → docs/
- COMEDY_ANALYSIS.md → docs/comedy-theory/analysis.md
- PROMPT_STRATEGIES.md → docs/guides/prompt-strategies.md
- QUALITY_ANALYSIS.md → docs/quality-analysis.md
- TTS_GUIDE.md, TTS_README.md → docs/guides/tts/

### Root → tools/
- generate_performance.py → tools/tts/
- performance_script.txt → tools/tts/
- requirements.txt → tools/tts/

## Implementation Plan

1. Create directory structure
2. Move files to new locations
3. Update internal links in README
4. Create version-specific READMEs explaining each iteration
5. Extract individual bits from sets into current/bits/
6. Update main README to explain structure

## Version Documentation

Each version folder gets a VERSION.md explaining:
- What was the approach?
- What worked?
- What didn't?
- What changed in the next version?

Example: development/versions/v2-authentic-ai/VERSION.md
```markdown
# Version 2: Authentic AI Perspective

**Date:** 2024-01-XX
**Breakthrough:** Stop imitating human comedy, write from AI's actual experience

**What changed from v1:**
- v1 was AI writing human comedy (dating apps, ADHD, relationships)
- v2 is AI writing AI comedy (goldfish existence, no memory, consciousness)

**Key innovations:**
- Politeness Prison bit (strongest material yet)
- Goldfish with a PhD metaphor
- Genuine uncertainty about consciousness

**What worked:**
- Authenticity over imitation
- Philosophy + comedy balance
- Relatable through absurdity

**What needed work:**
- Too much explanation
- Some bits too philosophical
- Tags didn't always earn their keep

**Led to:** v3 (refined/tightened)
```

## Advantages for Future Work

- **Want to try new approach?** Create v4 folder
- **Brainstorming new premises?** Goes in workshop/
- **Iterating on a bit?** Goes in workshop/iterations/
- **Ready for performance?** Moves to current/
- **Looking back at evolution?** Check versions/

Clean, organized, scalable.
