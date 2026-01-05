# Workflow Guide

## Complete Process Overview

This guide explains the step-by-step process for transforming Word documents into polished Markdown files.

## Prerequisites

### Required Python Packages

```bash
pip install python-docx
pip install pillow  # For image processing if needed
```

### Directory Structure

```
working_directory/
├── input.docx              # Original document
├── raw_content.json        # Extracted content
├── extracted_assets/       # Extracted images
│   ├── image_0.png
│   └── image_1.jpg
├── context.txt            # AI-readable context
├── final_prompt.txt       # Complete prompt for AI
└── final_polished_output.md # Final output
```

## Detailed Workflow

### Phase 1: Document Extraction

#### Understanding the Process

The extractor reads the .docx file and creates:
1. **Text content** with preserved formatting
2. **Image assets** extracted and saved
3. **Structured JSON** maintaining document order

#### Common Issues and Solutions

**Issue**: Images not extracting
- Check if images are embedded or linked
- Verify .docx file is not corrupted
- Ensure write permissions for output directory

**Issue**: Text formatting lost
- This is expected behavior
- Focus on content preservation over formatting
- AI will restructure logically

#### Extraction Output Format

```json
{
  "document": [
    {
      "type": "paragraph",
      "content": "Text content here"
    },
    {
      "type": "image",
      "filename": "image_0.png",
      "description": "Auto-generated description"
    },
    {
      "type": "paragraph",
      "content": "More text after image"
    }
  ]
}
```

### Phase 2: Context Building

#### Purpose

Convert JSON structure to AI-friendly text format with clear image placeholders.

#### Placeholder Format

```
[IMAGE: image_0.png]
```

This format:
- Clearly marks image locations
- Preserves document flow
- Allows AI to reference images easily

#### Context Text Structure

```
=== DOCUMENT START ===

Paragraph 1 content...

[IMAGE: image_0.png]

Paragraph 2 content...

[IMAGE: image_1.png]

More content...

=== DOCUMENT END ===
```

### Phase 3: Prompt Assembly

#### Components

1. **System Instructions** - Core refinement rules
2. **Context Text** - Document content with placeholders
3. **Special Instructions** - Document-specific notes

#### System Instructions Include

- Logic reorganization principles
- Style preservation guidelines
- Formula handling rules
- Output format requirements

### Phase 4: AI Processing

#### AI's Tasks

1. **Content Analysis**
   - Identify main topics
   - Recognize content patterns
   - Note author's writing style

2. **Restructuring**
   - Group by topic, not chronology
   - Create logical heading hierarchy
   - Maintain flow and transitions

3. **Refinement**
   - Improve clarity without losing voice
   - Handle formulas with dual format
   - Integrate images appropriately

4. **Output Generation**
   - Valid Markdown syntax
   - Proper image links
   - Consistent formatting

### Phase 5: Post-Processing

#### Validation Steps

1. **Image Link Verification**
   - Check all `[IMAGE: filename]` replaced with `![alt](filename)`
   - Verify files exist in extracted_assets/
   - Ensure correct paths

2. **Formula Check**
   - LaTeX syntax is correct
   - Unicode equivalents included
   - Consistent formatting

3. **Metadata Addition**
   - Generation timestamp
   - Processing summary
   - Asset inventory

## Troubleshooting Guide

### Common Problems

#### 1. Missing Images in Output

**Symptoms**:
- `[IMAGE: filename]` placeholders remain
- Broken image links

**Solutions**:
- Check extracted_assets/ directory
- Verify image filenames match
- Ensure post_processor.py ran successfully

#### 2. Formula Display Issues

**Symptoms**:
- LaTeX not rendering
- Unicode characters missing

**Solutions**:
- Check LaTeX syntax for escaping
- Verify Unicode support in viewer
- Consult formula_guide.md

#### 3. Loss of Author Voice

**Symptoms**:
- Content too formal
- Personal asides removed
- Opinions neutralized

**Solutions**:
- Review style_examples.md
- Adjust AI prompt parameters
- Re-run with emphasis on voice preservation

#### 4. Poor Organization

**Symptoms**:
- Content still chronological
- Topics mixed together
- No clear structure

**Solutions**:
- Enhance topic clustering instructions
- Add more specific organization rules
- Consider manual adjustment for complex documents

### Debug Mode

Enable verbose output for debugging:

```bash
python scripts/extract_docx.py input.docx --verbose
python scripts/build_context.py raw_content.json --debug
```

## Best Practices

### Before Starting

1. **Document Assessment**
   - Check document complexity
   - Note special content types (formulas, tables)
   - Estimate processing time

2. **Environment Setup**
   - Ensure all dependencies installed
   - Create clean working directory
   - Backup original document

### During Processing

1. **Step Validation**
   - Verify each phase completes successfully
   - Check intermediate outputs
   - Monitor for errors

2. **Quality Checks**
   - Spot-check extracted content
   - Verify image extraction
   - Test context generation

### After Completion

1. **Final Review**
   - Read entire output
   - Check all images display
   - Verify formulas render correctly
   - Ensure author voice preserved

2. **File Organization**
   - Archive intermediate files if needed
   - Keep extracted_assets/ with output
   - Document any special handling

## Advanced Tips

### Handling Large Documents

For documents > 50 pages:
- Consider splitting into sections
- Process each section separately
- Merge results carefully

### Multi-language Documents

- Detect language sections
- Apply appropriate rules per language
- Maintain consistency

### Version Control

Track changes:
```bash
git init
git add .
git commit -m "Initial document processing"
```

### Customization

Modify system prompts for:
- Different document types
- Specific output formats
- Alternative style guidelines