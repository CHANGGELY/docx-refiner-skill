---
name: docx-refiner
description: Intelligent Word document restructuring and refinement expert that transforms messy .docx files containing images, formulas, and scattered notes into well-organized Markdown documents compatible with Feishu. Use when Codex needs to extract and preserve all content from Word documents including images and formulas, reorganize scattered content by topic rather than chronological order, maintain the author's personal voice and style while improving clarity, convert documents to Markdown format with proper image links and formula representations, or process Chinese technical documents with mixed media content.
---

# Docx Refiner

## Overview

Transforms messy Word documents into structured, polished Markdown documents while preserving all content, images, and the author's unique voice.

## Workflow Decision Tree

First, understand the document type:

**For messy documents with scattered notes** → Use full workflow
**For structured documents needing refinement** → Skip to Phase 2
**For documents requiring formula handling** → Enable LaTeX processing

## Phase 1: Content Extraction

### 1.1 Extract Document Contents

Run the extractor to parse the .docx file:

```bash
python scripts/extract_docx.py input.docx
```

This creates:
- `raw_content.json` - Structured content with image references
- `extracted_assets/` - Directory with all extracted images

### 1.2 Verify Extraction

Check that all content is preserved:
- Text passages are complete
- Images are extracted with proper names
- Document structure is maintained in JSON

## Phase 2: Context Building

### 2.1 Build AI Context

Convert extracted JSON to AI-readable format:

```bash
python scripts/build_context.py raw_content.json
```

This generates context text with `[IMAGE: filename]` placeholders.

### 2.2 Assemble Prompt

Create the final prompt with system instructions:

```bash
python scripts/assemble_prompt.py context.txt
```

The prompt includes:
- System instructions for logic reorganization
- Style preservation guidelines
- Formula handling rules (LaTeX + Unicode)
- Image integration instructions

## Phase 3: AI Processing

### 3.1 Execute Refinement

Have the AI process the prompt to:
- Reorganize content by topic clusters
- Preserve author's personality and asides
- Convert formulas to dual format (LaTeX + Unicode)
- Maintain all original information (zero-deletion principle)

### 3.2 Generate Initial Output

AI produces initial Markdown draft with:
- Proper heading structure
- Integrated image links
- Formatted formulas
- Preserved author voice

## Phase 4: Post-Processing

### 4.1 Validate Output

Ensure all components are properly formatted:

```bash
python scripts/post_process.py output.md
```

This validates:
- Image link validity
- Formula formatting
- Metadata addition

### 4.2 Final Polish

Add metadata footer:
- Generation timestamp
- Processing summary
- Asset references

## Advanced Features

### Formula Handling

For mathematical content:
- Preserve original LaTeX notation
- Add Unicode equivalents for accessibility
- Use dual format: `$formula$` (LaTeX) + Unicode symbol

### Image Integration

- Extract with original resolution
- Maintain logical placement
- Use descriptive filenames
- Add alt-text for accessibility

### Style Preservation

- Keep colloquial expressions and asides
- Maintain author's unique tone
- Preserve technical terminology
- Don't over-formalize informal content

## Resources

### scripts/

Core processing scripts for document refinement:

- `extract_docx.py` - Main document extractor using python-docx
- `build_context.py` - Converts JSON to AI-readable context
- `assemble_prompt.py` - Combines context with system instructions
- `post_process.py` - Validates and finalizes output

### references/

Essential reference materials:

- `system_prompt.md` - Core refinement instructions and style guidelines
- `formula_guide.md` - Mathematical notation handling rules
- `style_examples.md` - Examples of voice preservation techniques
- `workflow_guide.md` - Detailed workflow explanations and troubleshooting

## Quality Checklist

Before finalizing, ensure:

- [ ] All original content preserved
- [ ] Images properly linked and accessible
- [ ] Formulas in dual format
- [ ] Logical topic-based organization
- [ ] Author's voice maintained
- [ ] Markdown syntax valid
- [ ] Metadata added

## Troubleshooting

**Missing images**: Check `extracted_assets/` directory and verify image paths in output
**Formula issues**: Consult `formula_guide.md` for proper formatting
**Style inconsistencies**: Review `style_examples.md` for voice preservation techniques
**Structure problems**: Refer to `workflow_guide.md` for organization principles