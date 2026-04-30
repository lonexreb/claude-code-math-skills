"""
latex_postprocess.py -- LaTeX-aware post-processing for PDF-to-Markdown conversions.

Converts simple LaTeX to Unicode (matching existing reference file style) and
preserves complex expressions in $...$ notation. Handles common OCR artifacts
in mathematical content.
"""

import re
from typing import Optional


# --- Unicode mappings for simple LaTeX commands ---

GREEK_LOWER: dict[str, str] = {
    "alpha": "\u03b1", "beta": "\u03b2", "gamma": "\u03b3", "delta": "\u03b4",
    "epsilon": "\u03b5", "varepsilon": "\u03b5", "zeta": "\u03b6", "eta": "\u03b7",
    "theta": "\u03b8", "vartheta": "\u03d1", "iota": "\u03b9", "kappa": "\u03ba",
    "lambda": "\u03bb", "mu": "\u03bc", "nu": "\u03bd", "xi": "\u03be",
    "pi": "\u03c0", "rho": "\u03c1", "sigma": "\u03c3", "tau": "\u03c4",
    "upsilon": "\u03c5", "phi": "\u03c6", "varphi": "\u03c6", "chi": "\u03c7",
    "psi": "\u03c8", "omega": "\u03c9",
}

GREEK_UPPER: dict[str, str] = {
    "Gamma": "\u0393", "Delta": "\u0394", "Theta": "\u0398", "Lambda": "\u039b",
    "Xi": "\u039e", "Pi": "\u03a0", "Sigma": "\u03a3", "Upsilon": "\u03a5",
    "Phi": "\u03a6", "Psi": "\u03a8", "Omega": "\u03a9",
}

OPERATORS: dict[str, str] = {
    "in": "\u2208", "notin": "\u2209", "ni": "\u220b",
    "subset": "\u2282", "supset": "\u2283", "subseteq": "\u2286", "supseteq": "\u2287",
    "cup": "\u222a", "cap": "\u2229", "bigcup": "\u22c3", "bigcap": "\u22c2",
    "emptyset": "\u2205", "varnothing": "\u2205",
    "forall": "\u2200", "exists": "\u2203", "nexists": "\u2204",
    "infty": "\u221e", "partial": "\u2202", "nabla": "\u2207",
    "pm": "\u00b1", "mp": "\u2213", "times": "\u00d7", "cdot": "\u00b7",
    "leq": "\u2264", "geq": "\u2265", "neq": "\u2260", "approx": "\u2248",
    "equiv": "\u2261", "sim": "\u223c", "simeq": "\u2243", "cong": "\u2245",
    "propto": "\u221d", "ll": "\u226a", "gg": "\u226b",
    "to": "\u2192", "rightarrow": "\u2192", "leftarrow": "\u2190",
    "Rightarrow": "\u21d2", "Leftarrow": "\u21d0",
    "leftrightarrow": "\u2194", "Leftrightarrow": "\u21d4",
    "implies": "\u27f9", "iff": "\u27fa",
    "mapsto": "\u21a6", "hookrightarrow": "\u21aa",
    "neg": "\u00ac", "land": "\u2227", "lor": "\u2228",
    "wedge": "\u2227", "vee": "\u2228",
    "oplus": "\u2295", "otimes": "\u2297",
    "langle": "\u27e8", "rangle": "\u27e9",
    "lceil": "\u2308", "rceil": "\u2309", "lfloor": "\u230a", "rfloor": "\u230b",
    "circ": "\u2218", "star": "\u22c6",
    "ell": "\u2113", "hbar": "\u210f", "Re": "\u211c", "Im": "\u2111",
    "aleph": "\u2135",
    "ldots": "\u2026", "cdots": "\u22ef", "vdots": "\u22ee", "ddots": "\u22f1",
    "triangle": "\u25b3", "square": "\u25a1",
}

SUPERSCRIPT_DIGITS: dict[str, str] = {
    "0": "\u2070", "1": "\u00b9", "2": "\u00b2", "3": "\u00b3",
    "4": "\u2074", "5": "\u2075", "6": "\u2076", "7": "\u2077",
    "8": "\u2078", "9": "\u2079",
    "n": "\u207f", "i": "\u2071",
    "+": "\u207a", "-": "\u207b",
    "*": "\u002a",
}

SUBSCRIPT_DIGITS: dict[str, str] = {
    "0": "\u2080", "1": "\u2081", "2": "\u2082", "3": "\u2083",
    "4": "\u2084", "5": "\u2085", "6": "\u2086", "7": "\u2087",
    "8": "\u2088", "9": "\u2089",
    "n": "\u2099", "m": "\u2098", "k": "\u2096", "i": "\u1d62",
    "j": "\u2c7c", "p": "\u209a", "s": "\u209b", "t": "\u209c",
    "+": "\u208a", "-": "\u208b",
}

# Commands that indicate a complex expression -- keep as LaTeX
COMPLEX_COMMANDS = frozenset({
    r"\frac", r"\dfrac", r"\tfrac",
    r"\int", r"\iint", r"\iiint", r"\oint",
    r"\sum", r"\prod", r"\coprod",
    r"\lim", r"\limsup", r"\liminf",
    r"\sqrt", r"\root",
    r"\begin", r"\end",
    r"\matrix", r"\pmatrix", r"\bmatrix", r"\vmatrix",
    r"\underbrace", r"\overbrace",
    r"\stackrel", r"\overset", r"\underset",
    r"\binom", r"\choose",
})


def protect_code_blocks(text: str) -> tuple[str, list[str]]:
    """Extract fenced code blocks to protect them from LaTeX processing."""
    blocks: list[str] = []
    pattern = re.compile(r'(```[^\n]*\n.*?\n```)', re.DOTALL)

    def _replace(match: re.Match) -> str:
        blocks.append(match.group(0))
        return f"\x00CODEBLOCK{len(blocks) - 1}\x00"

    return pattern.sub(_replace, text), blocks


def restore_code_blocks(text: str, blocks: list[str]) -> str:
    """Restore protected code blocks."""
    for i, block in enumerate(blocks):
        text = text.replace(f"\x00CODEBLOCK{i}\x00", block)
    return text


def normalize_latex_delimiters(text: str) -> str:
    r"""Normalize LaTeX delimiters to standard markdown math notation.

    \( ... \)  ->  $...$
    \[ ... \]  ->  $$...$$
    \begin{equation} ... \end{equation}  ->  $$...$$
    \begin{equation*} ... \end{equation*}  ->  $$...$$
    """
    # Inline: \( ... \) -> $...$
    text = re.sub(r'\\\(\s*', '$', text)
    text = re.sub(r'\s*\\\)', '$', text)

    # Display: \[ ... \] -> $$...$$
    text = re.sub(r'\\\[\s*', '$$', text)
    text = re.sub(r'\s*\\\]', '$$', text)

    # equation/equation* environments -> $$...$$
    text = re.sub(
        r'\\begin\{equation\*?\}\s*(.*?)\s*\\end\{equation\*?\}',
        r'$$\1$$',
        text,
        flags=re.DOTALL,
    )

    return text


def fix_latex_artifacts(text: str) -> str:
    r"""Fix common OCR and extraction artifacts in LaTeX content.

    - Rejoin LaTeX commands broken across lines
    - Fix spurious spaces inside math delimiters
    - Remove OCR-introduced backslash doubling in math
    """
    # Rejoin commands broken across lines: \frac\n{a}{b} -> \frac{a}{b}
    text = re.sub(r'(\\[a-zA-Z]+)\s*\n\s*(\{)', r'\1\2', text)

    # Fix doubled backslashes that aren't intentional linebreaks (within $...$)
    def _fix_double_backslash(match: re.Match) -> str:
        content = match.group(1)
        # Don't touch \\ at end of line (intentional linebreak in align)
        content = re.sub(r'\\\\([a-zA-Z])', r'\\\1', content)
        return f'${content}$'

    text = re.sub(r'\$([^$]+)\$', _fix_double_backslash, text)

    # Remove trailing whitespace within inline math: $ x $ -> $x$
    text = re.sub(r'\$\s+', '$', text)
    text = re.sub(r'\s+\$', '$', text)

    return text


def _is_complex_expression(expr: str) -> bool:
    """Check if a LaTeX expression is too complex for Unicode conversion."""
    for cmd in COMPLEX_COMMANDS:
        if cmd in expr:
            return True
    # Check nesting depth of braces
    depth = 0
    max_depth = 0
    for ch in expr:
        if ch == '{':
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == '}':
            depth -= 1
    return max_depth > 2


def _convert_simple_command(cmd: str) -> Optional[str]:
    """Convert a single LaTeX command name to Unicode, or None if not convertible."""
    if cmd in GREEK_LOWER:
        return GREEK_LOWER[cmd]
    if cmd in GREEK_UPPER:
        return GREEK_UPPER[cmd]
    if cmd in OPERATORS:
        return OPERATORS[cmd]
    return None


def _convert_superscript(char: str) -> Optional[str]:
    """Convert a single character to its Unicode superscript form."""
    return SUPERSCRIPT_DIGITS.get(char)


def _convert_subscript(char: str) -> Optional[str]:
    """Convert a single character to its Unicode subscript form."""
    return SUBSCRIPT_DIGITS.get(char)


def simplify_latex_to_unicode(text: str) -> str:
    r"""Convert simple LaTeX expressions to Unicode, preserving complex ones.

    Simple conversions:
      \alpha -> alpha, \in -> in, \forall -> forall, \leq -> leq
      x^{2} -> x superscript 2 (single-char superscripts only)
      x_{n} -> x subscript n (single-char subscripts only)

    Preserved as $...$:
      \frac{a}{b}, \int_0^1 f dx, matrices, aligned environments
    """

    def _process_math_block(match: re.Match) -> str:
        """Process a single $...$ or $$...$$ math block."""
        full = match.group(0)
        is_display = full.startswith('$$')
        inner = match.group(1)  # Both display and inline patterns capture in group(1)

        if inner is None:
            return full

        if _is_complex_expression(inner):
            return full

        result = inner

        # Replace LaTeX commands with Unicode equivalents
        def _replace_cmd(m: re.Match) -> str:
            cmd_name = m.group(1)
            unicode_char = _convert_simple_command(cmd_name)
            if unicode_char is not None:
                return unicode_char
            return m.group(0)  # keep original if no mapping

        result = re.sub(r'\\([a-zA-Z]+)', _replace_cmd, result)

        # Convert single-char superscripts: ^{x} or ^x
        def _replace_sup(m: re.Match) -> str:
            char = m.group(1)
            sup = _convert_superscript(char)
            return sup if sup is not None else m.group(0)

        result = re.sub(r'\^\{([0-9a-z+\-*])\}', _replace_sup, result)
        result = re.sub(r'\^([0-9])', _replace_sup, result)

        # Convert single-char subscripts: _{x} or _x
        def _replace_sub(m: re.Match) -> str:
            char = m.group(1)
            sub = _convert_subscript(char)
            return sub if sub is not None else m.group(0)

        result = re.sub(r'_\{([0-9a-z+\-])\}', _replace_sub, result)
        result = re.sub(r'_([0-9])', _replace_sub, result)

        # If after conversion there are no remaining backslashes or braces,
        # the expression is fully converted -- return plain text
        if '\\' not in result and '{' not in result and '}' not in result:
            return result.strip()

        # Otherwise keep it wrapped in math delimiters
        if is_display:
            return f'$${result}$$'
        return f'${result}$'

    # Process display math first ($$...$$), then inline ($...$)
    text = re.sub(r'\$\$(.+?)\$\$', _process_math_block, text, flags=re.DOTALL)
    text = re.sub(r'\$([^$]+?)\$', lambda m: _process_math_block(m), text)

    # Also convert standalone LaTeX commands outside math delimiters
    # (common in markdown text: "for all \alpha \in A")
    def _replace_standalone(m: re.Match) -> str:
        cmd_name = m.group(1)
        unicode_char = _convert_simple_command(cmd_name)
        return unicode_char if unicode_char is not None else m.group(0)

    text = re.sub(r'\\([a-zA-Z]+)(?![{a-zA-Z])', _replace_standalone, text)

    return text


def latex_postprocess(text: str) -> str:
    """Master post-processing pipeline for LaTeX content.

    Pipeline: protect code blocks -> normalize delimiters -> fix artifacts ->
    simplify to Unicode -> restore code blocks.
    """
    text, blocks = protect_code_blocks(text)
    text = normalize_latex_delimiters(text)
    text = fix_latex_artifacts(text)
    text = simplify_latex_to_unicode(text)
    text = restore_code_blocks(text, blocks)
    return text
