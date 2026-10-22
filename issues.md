| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| eval() on caller-supplied string | Security (High) | 42 | Arbitrary code execution via promo_expr (Bandit B307, Pylint W0123) | Replace with arithmetic on a validated discount percentage |
| os.system with concatenated string | Security (High) | 58 | Shell injection through filename (Bandit B605/B607) | Remove shell call, print confirmation |
| MD5 for ticket hash | Security (High) | 47 | Weak hash (Bandit B324) | Use hashlib.sha256 |
| Hardcoded secret, printed to stdout | Security (Medium) | 71, 80 | Credential in source and leaked in output | Read from environment variable, print only whether it is set |
| random used for POS PIN | Security (Low/Med) | 51 | Predictable PRNG for a credential (Bandit B311) | Use secrets.randbelow |
| Bare except: pass | Bug (Medium) | 26-27 | Swallows every error (Bandit B110, Flake8 E722, Pylint W0702) | Use dict.pop(key, None) |
| Mutable default argument | Bug (Medium) | 15 | order_log=[] shared across calls (Pylint W0102) | Default None, fall back to module-level log |
| Export writes settled orders | Logic (Medium) | 54-57 | README says "active orders" but all are exported | Filter on is_settled |
| == None comparison | Style | 32 | Flake8 E711, Pylint C0121 | Use is None |
| Unused import and variable | Style | 6, 31 | math, service_tax unused (F401, F841) | Delete |
| File opened without with | Bug (Low) | 55-57 | Leaks handle on error, no encoding (R1732, W1514) | with open(..., encoding="utf-8") |
| Non-snake_case names | Style | 15, 23, 30, 40 | Pylint C0103 | Rename; checkTableStatus becomes is_table_pending |
| Missing docstrings | Style | functions | Pylint C0116 | Add docstrings |
| Parameter shadows global | Style | 61 | orders shadows module-level orders (W0621) | Rename parameter |
| Needless else after return | Style | 34-37 | Pylint R1705 | Return expression directly |
| Lines over 79 chars | Style | 18, 19 | Flake8 E501 | Wrap lines |
| main() runs on import | Style | 83 | Side effects at import | if __name__ == "__main__" guard |
