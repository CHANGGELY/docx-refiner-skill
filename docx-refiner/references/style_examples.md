# Style Preservation Examples

## Core Principle

Maintain the author's authentic voice while improving clarity and organization. Never "sanitize" or over-formalize the content.

## Voice Preservation Techniques

### 1. Keep Colloquial Expressions

**Original**: "这个破玩意儿根本不好用，我折腾了半天才搞定"

**Preserved**: "这个工具确实难用，我花了很长时间才搞定"

**What NOT to do**: "该工具使用困难，需要较长时间进行配置"

### 2. Maintain Technical Jargon

**Original**: "我在纳指期货上实测MACD是管用的"

**Preserved**: "我在纳斯达克指数期货的实际交易中测试过，MACD指标确实有效"

**What NOT to do**: "经过在金融衍生品市场的实证研究，移动平均收敛发散指标展现了预测价值"

### 3. Preserve Author's Opinions

**Original**: "别听邢不行在那瞎比比说MACD没用，他只会无脑选币"

**Preserved**: "不建议采纳邢不行关于MACD无效的观点，他的方法主要局限于无脑选币，缺乏对择时和网格策略的理解"

**What NOT to do**: "有市场观点认为MACD指标的有效性存在争议"

### 4. Keep Personal Asides

**Original**: "（说句题外话，这个功能我当初差点就删了，后来发现真香）"

**Preserved**: "*插一句：这个功能我最初考虑删除，但实际使用后发现非常实用*"

**What NOT to do**: [删除]

## Organization Examples

### Topic-based Clustering

**Chronological Original**:
```
今天用了A工具，不错。
昨天买了B产品，也很好用。
上个月试了C工具，一般。
```

**Topic-based Refined**:
```
## 工具评测

### A工具
今天用了A工具，不错。

### C工具
上个月试了C工具，一般。

## 产品推荐

### B产品
昨天买了B产品，也很好用。
```

### Maintaining Flow

**Original Fragmented**:
```
终端配置很重要。
ZSH很好用。
另外，量化交易也要注意风险。
MACD指标其实有用。
```

**Refined with Flow**:
```
## 一、 终端开发环境配置

终端配置对效率至关重要。ZSH作为Mac系统默认Shell，其智能补全和插件支持是高效工作的基石。

## 二、 量化交易策略

在量化交易中，风险管理是首要考虑。关于技术指标，MACD在纳指期货实盘中的表现证明其有效性，与某些观点相悖。
```

## Specific Style Elements

### 1. Parenthetical Remarks

Keep parenthetical comments and asides:

```markdown
跑下一个策略的时候，记得先把U转到带单项目里（这样还能额外白嫖10%的分成）。
```

### 2. Emphatic Statements

Preserve emphatic language:

```markdown
**切记**：不要把"系统终端"和"Python终端"搞混！
```

### 3. Direct Address

Keep direct address to reader:

```markdown
如果你受够了"一关Trae IDE，实盘进程就跟着挂掉"的窘境，请务必执行以下解耦方案。
```

### 4. Humor and Personality

Maintain humor and personality:

```markdown
想要效率高，终端必须好。不要守着那个破烂的原始Shell，增强版的工具才是程序员的生产力工具。
```

## Technical Content Handling

### Code and Commands

Preserve exact technical content while improving presentation:

```markdown
### 1.2 PowerShell 增强模块

如果你在Windows或跨平台环境下使用PowerShell，以下模块必装：
- **Terminal-Icons**：为目录添加漂亮的图标，视觉效果拉满。
- **PSFzf**：为fzf绑定PowerShell键位，让搜索如丝般顺滑。
```

### Warnings and Notes

Keep warnings prominent:

```markdown
> **注意**：当你输入`python3`进入交互式解释器后，那是Python的地盘，只能执行Python代码，别在那瞎输系统命令。
```

## Quality Checklist

For each section, verify:

- [ ] Author's voice is recognizable
- [ ] Technical terms are preserved
- [ ] Opinions are maintained but clarified
- [ ] Colloquialisms are toned down but not eliminated
- [ ] Personal asides are marked appropriately
- [ ] Flow is improved without losing authenticity
- [ ] Humor and personality elements remain

## Before and After Examples

### Example 1: Tool Recommendation

**Before**:
```
rg挺好用的，比grep快多了，谁用谁知道。
```

**After**:
```
### ripgrep (rg)
ripgrep是极速全局搜索工具，相比传统grep在性能上有数个量级的提升。实际使用体验极佳，推荐作为日常搜索的首选工具。
```

### Example 2: Technical Process

**Before**:
```
先cd到目录，然后source激活环境，最后python跑脚本。别搞错了。
```

**After**:
```
### 环境激活与执行步骤

1. **切换到项目目录**
   ```bash
   cd /path/to/project
   ```

2. **激活Python虚拟环境**
   ```bash
   source .venv/bin/activate
   ```

3. **执行主程序**
   ```bash
   python main.py
   ```

> **重要提示**：请按顺序执行以上步骤，确保环境正确激活后再运行程序。
```

### Example 3: Opinionated Content

**Before**:
```
那个XXX就是个垃圾，别用。
```

**After**:
```
### 关于XXX工具的评估

基于实际使用经验，不建议使用XXX工具，主要问题包括：
- 性能表现不佳
- 稳定性存在问题
- 缺乏必要功能支持

建议考虑以下替代方案：[具体替代方案]
```