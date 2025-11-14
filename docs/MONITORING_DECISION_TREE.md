# Health Check Monitoring - Decision Tree

Rozhodovací strom pro diagnostiku a řešení problémů detekovaných health check systémem.

## Alert Decision Flow

```
┌─────────────────────────────────────┐
│  Přijat Uptimerobot Alert          │
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│  Otevřít /health-status/            │
└───────────────┬─────────────────────┘
                │
                ▼
        ┌───────┴───────┐
        │  Status?      │
        └───┬───────┬───┘
            │       │
     CRITICAL    WARNING/OK
            │       │
            ▼       ▼
    ┌───────────┐  ┌──────────────┐
    │  URGENTNÍ │  │  False       │
    │  Akce     │  │  Positive?   │
    └───────────┘  └──────────────┘
```

## Critical Alert Flow

```
Status: CRITICAL
    ↓
┌───────────────────────────────────────────────┐
│  Zkontrolovat Alert Messages                 │
└───────┬───────────────────────────────────────┘
        │
        ▼
   ┌────┴────┐
   │  Typ?   │
   └─┬─────┬─┘
     │     │
     ▼     ▼
  Language  Articles
   Alert    Alert
     │        │
     ▼        ▼
┌─────────────────────────┐  ┌──────────────────────────┐
│ "Pouze X% článků        │  │ "Pouze X článků          │
│  v češtině"             │  │  za 24h"                 │
└────────┬────────────────┘  └────────┬─────────────────┘
         │                             │
         ▼                             ▼
┌─────────────────────────┐  ┌──────────────────────────┐
│ LLM Translation Failed  │  │ NewsAPI / Generation     │
│                         │  │ Failed                   │
│ Actions:                │  │                          │
│ 1. Check OPENROUTER_KEY │  │ Actions:                 │
│ 2. Check LLM API status │  │ 1. Check NEWS_API_KEY    │
│ 3. Review GitHub logs   │  │ 2. Check GitHub Actions  │
│ 4. Manual re-run if OK  │  │ 3. Manual trigger        │
└─────────────────────────┘  └──────────────────────────┘
```

## Warning Alert Flow

```
Status: WARNING
    ↓
┌──────────────────────────────────┐
│  Zkontrolovat Severity           │
└────────┬─────────────────────────┘
         │
    ┌────┴────┐
    │  Trend? │
    └─┬─────┬─┘
      │     │
   Zhoršuje  Stable/Zlepšuje
      │     │
      ▼     ▼
┌──────────────┐  ┌─────────────────┐
│ Eskalovat    │  │ Monitor only    │
│ na CRITICAL  │  │ Review týdně    │
└──────────────┘  └─────────────────┘
```

## Language Quality Decision Tree

```
Czech Ratio < 85%?
    │
    ▼
┌────────────────────────────────────────┐
│  Zkontrolovat English Articles Sample  │
└───────┬────────────────────────────────┘
        │
   ┌────┴────┐
   │ Pattern?│
   └─┬─────┬─┘
     │     │
     ▼     ▼
  All New  Random Mix
  Articles
     │        │
     ▼        ▼
┌─────────────────────┐  ┌──────────────────────┐
│ Recent LLM Failure  │  │ Ongoing Partial      │
│                     │  │ Failure              │
│ Cause:              │  │                      │
│ - API outage        │  │ Causes:              │
│ - API key expired   │  │ - Rate limiting      │
│ - Quota exceeded    │  │ - Cost limits        │
│                     │  │ - Model degradation  │
│ Fix:                │  │                      │
│ 1. Check API status │  │ Fix:                 │
│ 2. Verify API key   │  │ 1. Check quotas      │
│ 3. Re-run workflow  │  │ 2. Check rate limits │
│                     │  │ 3. Review LLM config │
└─────────────────────┘  └──────────────────────┘
```

## Freshness Problem Decision Tree

```
Newest Article > 6h old?
    │
    ▼
┌──────────────────────────────────┐
│  Zkontrolovat GitHub Actions     │
└───────┬──────────────────────────┘
        │
   ┌────┴────┐
   │ Status? │
   └─┬─────┬─┘
     │     │
  Success  Failed
     │        │
     ▼        ▼
┌────────────────────┐  ┌──────────────────────┐
│ Schedule Problem   │  │ Workflow Failure     │
│                    │  │                      │
│ Možné příčiny:     │  │ Možné příčiny:       │
│ - Cron disabled    │  │ - API keys invalid   │
│ - Repo archived    │  │ - Dependencies error │
│ - Workflow paused  │  │ - Syntax error       │
│                    │  │ - Network timeout    │
│ Fix:               │  │                      │
│ 1. Check .yml      │  │ Fix:                 │
│ 2. Manual trigger  │  │ 1. Review logs       │
│ 3. Re-enable cron  │  │ 2. Fix error         │
│                    │  │ 3. Re-run            │
└────────────────────┘  └──────────────────────┘
```

## Content Quality Decision Tree

```
Avg Content Length < 300?
    │
    ▼
┌──────────────────────────────────┐
│  Zkontrolovat Sample Articles    │
└───────┬──────────────────────────┘
        │
   ┌────┴────┐
   │ Pattern?│
   └─┬─────┬─┘
     │     │
     ▼     ▼
  All Short  Random
  Content
     │        │
     ▼        ▼
┌──────────────────────┐  ┌─────────────────────┐
│ LLM Prompt Issue     │  │ Source Quality      │
│                      │  │ Problem             │
│ Možné příčiny:       │  │                     │
│ - Prompt truncated   │  │ Možné příčiny:      │
│ - Max tokens low     │  │ - NewsAPI sources   │
│ - Model changed      │  │ - Snippet-only      │
│                      │  │ - Paywall content   │
│ Fix:                 │  │                     │
│ 1. Review prompt     │  │ Fix:                │
│ 2. Check token limit │  │ 1. Review sources   │
│ 3. Test LLM params   │  │ 2. Adjust filters   │
└──────────────────────┘  └─────────────────────┘
```

## Response Time Matrix

| Alert Level | Response Time | Escalation | Notes |
|-------------|--------------|------------|-------|
| **CRITICAL** | Immediate | 1 hour | Requires manual intervention |
| **WARNING - Trend down** | 4 hours | 24 hours | Monitor closely |
| **WARNING - Stable** | 24 hours | 1 week | Review at weekly check |
| **INFO** | Next weekly review | N/A | Informational only |

## Diagnostic Command Cheat Sheet

```bash
# Quick Status Check
curl -s https://marigold.cz/health-check/ | jq '.status, .summary'

# Full Health Data
curl -s https://marigold.cz/health-check/ | jq '.'

# Check Specific Metric
curl -s https://marigold.cz/health-check/ | jq '.metrics.czech_ratio'

# List All Alerts
curl -s https://marigold.cz/health-check/ | jq '.alerts[]'

# GitHub Actions Status
gh run list --workflow=tech-news.yml --limit 5

# View Latest Run
gh run view --workflow=tech-news.yml

# View Logs of Latest Run
gh run view --log --workflow=tech-news.yml

# Manual Trigger Workflow
gh workflow run tech-news.yml

# Local Health Check
python3 scripts/tech_news_health_check.py

# Test Specific Article Language
python3 << 'EOF'
import sys
sys.path.insert(0, 'scripts')
from tech_news_health_check import TechNewsHealthCheck
checker = TechNewsHealthCheck()
text = open('_tech_news/2025-11-14-example.md').read()
score = checker._detect_language(text)
print(f"Language score: {score} ({'Czech' if score > 0.5 else 'English'})")
EOF
```

## False Positive Handling

```
False Positive Alert
    ↓
┌──────────────────────────────────┐
│  Verify Against /health-status/  │
└───────┬──────────────────────────┘
        │
   ┌────┴────┐
   │ Real    │
   │ Problem?│
   └─┬─────┬─┘
     │     │
    YES   NO
     │     │
     ▼     ▼
┌───────────────┐  ┌──────────────────────┐
│ Not False     │  │ True False Positive  │
│ Positive      │  │                      │
│               │  │ Možné příčiny:       │
│ Follow        │  │ - Uptimerobot cache  │
│ normal        │  │ - Stale data         │
│ decision      │  │ - Threshold too      │
│ tree          │  │   strict             │
│               │  │                      │
│               │  │ Actions:             │
│               │  │ 1. Note in log       │
│               │  │ 2. Consider adjust   │
│               │  │    threshold         │
│               │  │ 3. Wait for next     │
│               │  │    check (5 min)     │
└───────────────┘  └──────────────────────┘
```

## Escalation Path

```
┌─────────────────────┐
│  CRITICAL Alert     │
│  (Immediate)        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Initial Response   │
│  (< 15 min)         │
│  - Acknowledge      │
│  - Quick diagnosis  │
└──────────┬──────────┘
           │
           ▼
   ┌───────┴────────┐
   │  Can Fix       │
   │  Quickly?      │
   └───┬────────┬───┘
       │        │
      YES      NO
       │        │
       ▼        ▼
┌──────────┐  ┌─────────────────┐
│ Fix &    │  │ Escalate to     │
│ Verify   │  │ Team Lead       │
│          │  │                 │
│ < 1 hour │  │ If unresolved   │
│          │  │ after 2 hours → │
│          │  │ Emergency       │
│          │  │ manual run      │
└──────────┘  └─────────────────┘
```

## Priority Matrix

| Metric | Current | Threshold | Severity | Priority |
|--------|---------|-----------|----------|----------|
| Czech Ratio | < 50% | 85% | CRITICAL | P0 (Immediate) |
| Czech Ratio | 50-70% | 85% | CRITICAL | P1 (< 4h) |
| Czech Ratio | 70-85% | 85% | WARNING | P2 (< 24h) |
| Articles 24h | 0 | 10 | CRITICAL | P0 (Immediate) |
| Articles 24h | 1-5 | 10 | WARNING | P1 (< 4h) |
| Articles 24h | 5-10 | 10 | WARNING | P2 (< 24h) |
| Newest Age | > 24h | 6h | CRITICAL | P1 (< 4h) |
| Newest Age | 12-24h | 6h | WARNING | P2 (< 24h) |
| Newest Age | 6-12h | 6h | WARNING | P3 (Monitor) |

## Preventive Actions

### Daily (Automated)
- ✅ Uptimerobot monitoring running
- ✅ GitHub Actions scheduled runs
- ✅ Auto-generation of health data

### Weekly (15 min manual)
- Review health trends in `/health-status/`
- Check false positive/negative rate
- Verify alert email delivery
- Quick test of manual workflow trigger

### Monthly (1 hour manual)
- Deep analysis of all metrics
- Review and adjust thresholds
- Update documentation
- Post-mortem any incidents
- Test disaster recovery procedure

### Quarterly (2 hours manual)
- Full system audit
- Test all failure scenarios
- Review and update alerting strategy
- Team training on procedures
- Backup and disaster recovery drill

---

**Tips:**
- 🔍 Always verify against `/health-status/` before acting
- 📊 Check trends, not just single data points
- ⏱️ Consider time of day (weekends, holidays have lower traffic)
- 📝 Document all incidents for future threshold tuning
- 🧪 Test fixes in local environment before deploying

**Quick Access:**
- 📊 Dashboard: https://marigold.cz/health-status/
- 🔧 Uptimerobot: https://uptimerobot.com/dashboard
- 🤖 GitHub Actions: https://github.com/username/marigold-page/actions
