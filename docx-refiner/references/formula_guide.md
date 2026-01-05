# Formula Handling Guide

## Dual Format Principle

All mathematical formulas should be presented in dual format for maximum compatibility and accessibility.

### Format Structure

1. **LaTeX Format** - For technical accuracy
   ```markdown
   $E = mc^2$
   ```

2. **Unicode Equivalent** - For universal readability
   ```markdown
   E = mc²
   ```

### Implementation Pattern

```markdown
**LaTeX**: $∫_0^∞ e^{-x^2} dx = \frac{\sqrt{π}}{2}$

**Unicode**: ∫₀^∞ e⁻ˣ² dx = √π/2
```

## Common Formula Conversions

### Superscripts and Subscripts

| LaTeX | Unicode |
|-------|---------|
| `x^2` | x² |
| `x^n` | xⁿ |
| `x_1` | x₁ |
| `x_i` | xᵢ |

### Greek Letters

| LaTeX | Unicode |
|-------|---------|
| `\alpha` | α |
| `\beta` | β |
| `\gamma` | γ |
| `\delta` | δ |
| `\epsilon` | ε |
| `\pi` | π |
| `\sigma` | σ |
| `\theta` | θ |

### Operators

| LaTeX | Unicode |
|-------|---------|
| `\times` | × |
| `\div` | ÷ |
| `\neq` | ≠ |
| `\leq` | ≤ |
| `\geq` | ≥ |
| `\approx` | ≈ |
| `\infty` | ∞ |

### Fractions

Simple fractions:
```markdown
**LaTeX**: $\frac{1}{2}$

**Unicode**: ½
```

Complex fractions:
```markdown
**LaTeX**: $\frac{a+b}{c+d}$

**Unicode**: (a+b)/(c+d)
```

### Integrals and Summations

```markdown
**LaTeX**: $\sum_{i=1}^n x_i$

**Unicode**: Σᵢ₌₁ⁿ xᵢ
```

```markdown
**LaTeX**: $\int_a^b f(x) dx$

**Unicode**: ∫ₐᵇ f(x) dx
```

## Special Cases

### Matrix Notation

Keep matrices in LaTeX format only, as Unicode representation is often unclear:

```markdown
$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$
```

### Complex Equations

For multi-line equations, use LaTeX with proper alignment:

```markdown
\[
\begin{align}
f(x) &= x^2 + 2x + 1 \\
     &= (x + 1)^2
\end{align}
\]
```

## Processing Rules

1. **Always preserve original LaTeX** - Never remove the LaTeX version
2. **Add Unicode when possible** - Include readable Unicode equivalent
3. **Maintain clarity** - If Unicode is ambiguous, LaTeX takes precedence
4. **Consistent formatting** - Use the same pattern throughout the document
5. **Test readability** - Ensure both formats render correctly

## Examples in Context

### Physics Example

```markdown
The kinetic energy is given by:

**LaTeX**: $E_k = \frac{1}{2}mv^2$

**Unicode**: Eₖ = ½mv²
```

### Statistics Example

```markdown
The normal distribution:

**LaTeX**: $f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$

**Unicode**: f(x) = (1/σ√2π)e^(-1/2((x-μ)/σ)²)
```

### Calculus Example

```markdown
The derivative:

**LaTeX**: $\frac{d}{dx}(x^n) = nx^{n-1}$

**Unicode**: d/dx(xⁿ) = nxⁿ⁻¹
```