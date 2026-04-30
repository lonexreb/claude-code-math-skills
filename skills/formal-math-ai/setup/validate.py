#!/usr/bin/env python3
"""
validate.py -- Quality validation for PDF-to-Markdown conversions.

Checks LaTeX integrity, document structure, encoding quality, and content density.
Produces a score (0.0-1.0) and detailed issue list.

Usage:
  python validate.py references/              # Validate all .md files
  python validate.py references/topic.md      # Validate a single file
"""

import os
import re
import sys
from dataclasses import dataclass, field


@dataclass(frozen=True)
class ValidationIssue:
    line: int
    severity: str       # "error", "warning", "info"
    category: str       # "latex", "structure", "encoding", "content"
    message: str


@dataclass
class ValidationReport:
    file_path: str
    total_lines: int
    issues: list[ValidationIssue] = field(default_factory=list)
    score: float = 1.0


# Severity weights for scoring
SEVERITY_WEIGHTS: dict[str, float] = {
    "error": 0.05,      # Each error deducts 5%
    "warning": 0.02,    # Each warning deducts 2%
    "info": 0.005,      # Each info deducts 0.5%
}


def validate_latex_integrity(text: str) -> list[ValidationIssue]:
    """Check for broken LaTeX math delimiters and commands."""
    issues: list[ValidationIssue] = []
    lines = text.split('\n')

    in_code_block = False
    inline_dollar_count = 0

    for line_num, line in enumerate(lines, start=1):
        # Skip code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Count unescaped $ signs (excluding $$)
        stripped = re.sub(r'\$\$', '', line)
        dollar_count = stripped.count('$')
        inline_dollar_count += dollar_count

        # Check for broken LaTeX commands (backslash at end of line before non-brace)
        if re.search(r'\\[a-zA-Z]+\s*$', line) and line_num < len(lines):
            next_line = lines[line_num] if line_num < len(lines) else ''
            if next_line.strip() and not next_line.strip().startswith('{'):
                issues.append(ValidationIssue(
                    line=line_num,
                    severity="warning",
                    category="latex",
                    message="LaTeX command at end of line may be broken across lines",
                ))

    # Check for unmatched display math $$
    display_count = text.count('$$')
    if display_count % 2 != 0:
        issues.append(ValidationIssue(
            line=0,
            severity="error",
            category="latex",
            message=f"Unmatched $$ delimiters: found {display_count} (odd count)",
        ))

    # Check for unmatched inline math $ (after removing $$)
    text_no_display = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
    # Also remove code blocks
    text_no_code = re.sub(r'```.*?```', '', text_no_display, flags=re.DOTALL)
    inline_count = text_no_code.count('$')
    if inline_count % 2 != 0:
        issues.append(ValidationIssue(
            line=0,
            severity="error",
            category="latex",
            message=f"Unmatched $ delimiters: found {inline_count} (odd count)",
        ))

    return issues


def validate_structure(text: str) -> list[ValidationIssue]:
    """Check document structure against reference file conventions."""
    issues: list[ValidationIssue] = []
    lines = text.split('\n')

    # Check for title heading (# at start)
    has_title = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('# ') and not stripped.startswith('## '):
            has_title = True
        break

    if not has_title:
        issues.append(ValidationIssue(
            line=1,
            severity="warning",
            category="structure",
            message="Missing top-level heading (# Title)",
        ))

    # Check for Table of Contents
    has_toc = bool(re.search(r'^##\s+Table of Contents', text, re.MULTILINE))
    if not has_toc:
        issues.append(ValidationIssue(
            line=0,
            severity="info",
            category="structure",
            message="No '## Table of Contents' section found",
        ))

    # Check heading hierarchy (no ### before first ##)
    found_h2 = False
    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith('## ') and not stripped.startswith('### '):
            found_h2 = True
        elif stripped.startswith('### ') and not found_h2:
            issues.append(ValidationIssue(
                line=line_num,
                severity="warning",
                category="structure",
                message="### heading appears before any ## heading",
            ))
            break

    # Check for empty sections (heading followed by another heading)
    prev_was_heading = False
    prev_heading_line = 0
    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()
        is_heading = stripped.startswith('#')
        if is_heading and prev_was_heading:
            issues.append(ValidationIssue(
                line=prev_heading_line,
                severity="info",
                category="structure",
                message="Empty section (heading followed immediately by another heading)",
            ))
        if stripped:  # non-empty line
            prev_was_heading = is_heading
            prev_heading_line = line_num

    # Check for section separators (--- between major sections)
    h2_count = len(re.findall(r'^## ', text, re.MULTILINE))
    separator_count = len(re.findall(r'^---\s*$', text, re.MULTILINE))
    if h2_count > 2 and separator_count == 0:
        issues.append(ValidationIssue(
            line=0,
            severity="info",
            category="structure",
            message=f"No --- separators found between {h2_count} sections",
        ))

    return issues


def validate_encoding(text: str) -> list[ValidationIssue]:
    """Check for encoding problems and artifacts."""
    issues: list[ValidationIssue] = []
    lines = text.split('\n')

    # Common mojibake patterns (UTF-8 decoded as Latin-1 or similar)
    mojibake_patterns = [
        (r'Ã\u00a9', 'e-acute mojibake'),
        (r'Ã\u00bc', 'u-umlaut mojibake'),
        (r'Ã\u00b6', 'o-umlaut mojibake'),
        (r'Ã\u00a4', 'a-umlaut mojibake'),
        (r'Â\u00b2', 'superscript mojibake'),
        (r'\ufffd', 'Unicode replacement character'),
    ]

    for line_num, line in enumerate(lines, start=1):
        for pattern, desc in mojibake_patterns:
            if re.search(pattern, line):
                issues.append(ValidationIssue(
                    line=line_num,
                    severity="error",
                    category="encoding",
                    message=f"Possible {desc} detected",
                ))

        # Check for remaining ligatures
        remaining_ligatures = {'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬀ': 'ff', 'ﬃ': 'ffi', 'ﬄ': 'ffl'}
        for lig, replacement in remaining_ligatures.items():
            if lig in line:
                issues.append(ValidationIssue(
                    line=line_num,
                    severity="warning",
                    category="encoding",
                    message=f"Remaining ligature '{lig}' (should be '{replacement}')",
                ))

        # Check for control characters (except \t \n)
        for i, ch in enumerate(line):
            if ord(ch) < 32 and ch not in ('\t',):
                issues.append(ValidationIssue(
                    line=line_num,
                    severity="warning",
                    category="encoding",
                    message=f"Control character U+{ord(ch):04X} at position {i}",
                ))
                break  # One per line is enough

    return issues


def validate_content_density(text: str) -> list[ValidationIssue]:
    """Check content density for signs of poor conversion quality."""
    issues: list[ValidationIssue] = []

    # Split into paragraphs (blocks separated by blank lines)
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]

    if not paragraphs:
        issues.append(ValidationIssue(
            line=0,
            severity="error",
            category="content",
            message="No content paragraphs found",
        ))
        return issues

    # Filter out headings, separators, and code blocks for density analysis
    content_paragraphs = [
        p for p in paragraphs
        if not p.startswith('#')
        and not p.startswith('---')
        and not p.startswith('```')
        and not p.startswith('|')  # table rows
    ]

    if not content_paragraphs:
        return issues

    avg_len = sum(len(p) for p in content_paragraphs) / len(content_paragraphs)

    if avg_len < 20:
        issues.append(ValidationIssue(
            line=0,
            severity="warning",
            category="content",
            message=f"Very short average paragraph length ({avg_len:.0f} chars) -- possible OCR fragmentation",
        ))

    if avg_len > 2000:
        issues.append(ValidationIssue(
            line=0,
            severity="warning",
            category="content",
            message=f"Very long average paragraph length ({avg_len:.0f} chars) -- possible missing line breaks",
        ))

    # Check for lines that are mostly non-alphabetic (possible OCR garbage)
    lines = text.split('\n')
    garbage_lines = 0
    for line in lines:
        stripped = line.strip()
        if len(stripped) > 10:
            alpha_ratio = sum(1 for c in stripped if c.isalpha()) / len(stripped)
            if alpha_ratio < 0.2:
                garbage_lines += 1

    if garbage_lines > len(lines) * 0.1:
        issues.append(ValidationIssue(
            line=0,
            severity="warning",
            category="content",
            message=f"{garbage_lines} lines appear to be OCR noise (>10% of file)",
        ))

    return issues


def compute_score(issues: list[ValidationIssue]) -> float:
    """Compute aggregate quality score from issues."""
    deduction = sum(SEVERITY_WEIGHTS.get(issue.severity, 0) for issue in issues)
    return max(0.0, min(1.0, 1.0 - deduction))


def validate_file(filepath: str) -> ValidationReport:
    """Run all validators on a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')
    all_issues: list[ValidationIssue] = []

    all_issues.extend(validate_latex_integrity(text))
    all_issues.extend(validate_structure(text))
    all_issues.extend(validate_encoding(text))
    all_issues.extend(validate_content_density(text))

    score = compute_score(all_issues)

    return ValidationReport(
        file_path=filepath,
        total_lines=len(lines),
        issues=all_issues,
        score=score,
    )


def validate_directory(dirpath: str) -> list[ValidationReport]:
    """Validate all .md files in a directory."""
    reports: list[ValidationReport] = []
    for fname in sorted(os.listdir(dirpath)):
        if fname.lower().endswith('.md'):
            fpath = os.path.join(dirpath, fname)
            if os.path.isfile(fpath):
                reports.append(validate_file(fpath))
    return reports


def print_report(report: ValidationReport) -> None:
    """Print a single validation report."""
    score_str = f"{report.score:.2f}"
    status = "PASS" if report.score >= 0.9 else ("REVIEW" if report.score >= 0.7 else "FAIL")
    print(f"  {os.path.basename(report.file_path):45s} {report.total_lines:5d} lines  {score_str}  {status}")

    for issue in report.issues:
        prefix = {"error": "ERR", "warning": "WRN", "info": "INF"}.get(issue.severity, "???")
        line_str = f"L{issue.line}" if issue.line > 0 else "   "
        print(f"    [{prefix}] {line_str:6s} [{issue.category}] {issue.message}")


def print_summary(reports: list[ValidationReport]) -> None:
    """Print summary table of all reports."""
    print("\n" + "=" * 75)
    print(f"  {'File':45s} {'Lines':>5s}  {'Score':>5s}  Status")
    print("-" * 75)
    for report in reports:
        score_str = f"{report.score:.2f}"
        status = "PASS" if report.score >= 0.9 else ("REVIEW" if report.score >= 0.7 else "FAIL")
        fname = os.path.basename(report.file_path)
        print(f"  {fname:45s} {report.total_lines:5d}  {score_str:>5s}  {status}")
    print("-" * 75)
    avg_score = sum(r.score for r in reports) / len(reports) if reports else 0
    total_issues = sum(len(r.issues) for r in reports)
    print(f"  {'AVERAGE':45s}        {avg_score:.2f}  ({total_issues} total issues)")
    print("=" * 75)


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate.py <file_or_directory>")
        print("  python validate.py references/           # Validate all .md files")
        print("  python validate.py references/topic.md   # Validate single file")
        sys.exit(1)

    target = sys.argv[1]

    if os.path.isdir(target):
        reports = validate_directory(target)
        if not reports:
            print(f"No .md files found in {target}")
            sys.exit(1)
        for report in reports:
            if report.issues:
                print(f"\n{os.path.basename(report.file_path)}:")
                print_report(report)
        print_summary(reports)
    elif os.path.isfile(target):
        report = validate_file(target)
        print(f"\n{report.file_path}:")
        print_report(report)
    else:
        print(f"ERROR: {target} not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
