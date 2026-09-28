---
name: ux-researcher-designer
description: UX research and design toolkit for Senior UX Designer/Researcher including data-driven persona generation, journey mapping, usability testing frameworks, and research synthesis. Use for user research, persona creation, journey mapping, and design validation.
---

# UX Researcher & Designer

Comprehensive toolkit for user-centered research and experience design.

## Core Capabilities
- Data-driven persona generation
- Customer journey mapping
- Usability testing frameworks
- Research synthesis and insights
- Design validation methods

## Key Scripts

### persona_generator.py
Creates research-backed personas from user data and interviews.

**Usage**: `python scripts/persona_generator.py [json]`

Run it from this skill's directory (`.claude/skills/ux-researcher-designer/`).
Without an argument it runs on built-in sample data. Add `--format json` for
machine-readable output.

**Features**:
- Analyzes user behavior patterns
- Identifies persona archetypes
- Extracts psychographics
- Generates scenarios
- Provides design implications
- Confidence scoring based on sample size

**Input format** (all fields optional except `users`):

```json
{
  "users": [
    {
      "id": "u1",
      "age": 34,
      "role": "Farmacéutica",
      "tech_savviness": 4,
      "usage_frequency": "daily",
      "device": "mobile",
      "goals": ["reponer stock rápido"],
      "pain_points": ["demasiados pasos para pedir"],
      "motivations": ["ahorrar tiempo"],
      "quotes": ["Quiero pedir en dos clicks."]
    }
  ]
}
```

`tech_savviness` goes from 1 to 5. `usage_frequency` is one of `daily`,
`weekly`, `monthly` or `rarely`.
