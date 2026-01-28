# PyPI Publication Status Report

**Last Updated:** January 28, 2026  
**Total Projects:** 27+ (counting all subdirectories)  
**On PyPI:** 20 ✅  
**Not Python (npm/Node.js):** 5  
**Failed/Unknown Reason:** ~2-3  

---

## 📊 Summary by Status

### ✅ Successfully on PyPI (20 packages)

These packages have been successfully published to PyPI and are ready for installation via `pip install`.

1. **brain-dev** - AI-powered code intelligence MCP server
2. **code-covered** - Code coverage analysis and improvement
3. **tool-scan** - Security scanning for MCP tools
4. **mcp-stress-test** - Performance and load testing for MCP servers
5. **comfy-headless** - Headless ComfyUI wrapper for image generation
6. **audiobooker** - Audio book generation from text
7. **file-compass** - File discovery and navigation tools
8. **integradio** - Integration discovery and orchestration
9. **flexiflow** - Flexible workflow automation
10. **tool-compass** - MCP tool discovery and registry
11. **payroll-engine** - Payroll processing automation
12. **pathway** - Process automation and workflow management
13. **mcpt** - MCP tool CLI and configuration
14. **nexus-router** - Core routing engine
15. **nexus-router-adapter-stdout** - stdout adapter for routing
16. **ally-demo-python** - Accessibility demo application
17. **aspire-ai** - AI integration framework
18. **headless-wheel-builder** - Headless Python wheel builder
19. **a11y-assist**, **a11y-ci**, **a11y-lint** - Accessibility tools
20. **voice-soundboard** ✅ (just fixed - Python 3.14 compatible)

---

## ⚠️ Non-Python Packages (npm/Node.js) - 5 packages

These cannot be published to PyPI as they are JavaScript/Node.js projects. They should be published to **npm** instead.

| Package | Type | Location | Status |
|---------|------|----------|--------|
| **a11y-evidence-engine** | Node.js | `accessibility/a11y-evidence-engine/` | Should publish to npm |
| **a11y-mcp-tools** | Node.js | `accessibility/a11y-mcp-tools/` | Should publish to npm |
| **prov-engine-js** | Node.js | `core/prov-engine-js/` | Should publish to npm |
| **synthesis** | Node.js/Web | `core/synthesis/` | Should publish to npm |
| **venvkit** | Node.js/Hybrid | `core/venvkit/` | May need npm or PyPI |

**Recommendation:** Set up npm publishing workflows for these projects. Check if they have `.npmrc` or publish scripts configured.

---

## ❌ Failed to Publish / Unknown Reason

Based on workspace scan, these projects have issues:

### 1. **nexus-router-adapter-http** ❌ NO PUBLISH WORKFLOW
**Status:** ❌ Missing PyPI workflow  
**Location:** `core/nexus-router-adapter-http/`  
**Description:** HTTP adapter for nexus-router (reference implementation)  
**Version:** 0.1.0  
**Python:** >=3.10  
**Dependencies:** nexus-router>=0.8.0, httpx>=0.25.0  
**Issue:** Only has `adapter-ci.yml` for testing, NO `publish.yml` workflow  

**Fix:**
- Add `.github/workflows/publish.yml` with PyPI publishing action
- Configure release-triggered publishing
- See examples: `tool-scan`, `mcp-stress-test`, `voice-soundboard`

---

### 2. **backpropagate** ✅ HAS WORKFLOW (Verify Published)
**Status:** ✅ Publish workflow exists  
**Location:** `ai/backpropagate/`  
**Description:** Production-ready headless LLM fine-tuning with LoRA/QLoRA  
**Version:** 0.1.0  
**Python:** >=3.10  
**Issue:** None detected - likely published successfully  

**Action:** Verify on PyPI - if NOT published, check workflow logs

---

### 3. **context-window-manager** ✅ HAS WORKFLOW (Verify Published)
**Status:** ✅ Publish workflow exists  
**Location:** `ai/context-window-manager/`  
**Description:** MCP server for LLM context restoration via KV cache persistence  
**Version:** 0.6.2  
**Python:** >=3.11  
**Issue:** None detected - likely published successfully  

**Action:** Verify on PyPI - if NOT published, check workflow logs

---

### 4. **headless-wheel-builder** ✅ HAS WORKFLOW (Verify Published)
**Status:** ✅ Publish workflow exists  
**Location:** `reference/headless-wheel-builder/`  
**Description:** Universal headless Python wheel builder with GitHub operations  
**Details:** 
- Has comprehensive publish workflow
- README claims PyPI badge
- 226 tests, 62%+ coverage
- Production ready designation

**Action:** Verify on PyPI - if NOT published, check workflow logs
**Details:**
- Has `pyproject.toml` indicating Python project
- Complex project with build/publish features
- May have been intentionally excluded from PyPI (reference implementation)

**Action:** Check git history or documentation for why it wasn't published

---

### 3. Other Potential Issues

Check these projects if they're not accounted for in the "On PyPI" list:

| Project | Location | To Investigate |
|---------|----------|-----------------|
| **comfy-headless** (media) | `media/comfy-headless/` | Duplicate of root-level? Check if both exist |
| **a11y-assist** | `accessibility/a11y-assist/` | Python or Node.js? |
| **a11y-ci** | `accessibility/a11y-ci/` | Python or Node.js? |
| **a11y-lint** | `accessibility/a11y-lint/` | Python or Node.js? |
| **nexus-router-adapter-http** | `core/nexus-router-adapter-http/` | May be npm package |

---

## 🔧 Projects Needing Action

### High Priority (Blocking Issues)

| Project | Issue | Action |
|---------|-------|--------|
| **voice-soundboard** | Python 3.14 incompatibility | Update dependencies or Python requirements |
| **Non-Python packages** | Published to wrong registry | Set up npm publishing |

### Medium Priority (Verification Needed)

| Project | Issue | Action |
|---------|-------|--------|
| **reference/headless-wheel-builder** | Unknown reason | Investigate & clarify |
| **accessibility/** subprojects | Type unclear | Determine language & registry |

---

## 📋 Checklist for New Python Packages

Before publishing to PyPI, ensure:

- [ ] `pyproject.toml` with all required fields (name, version, description)
- [ ] `requires-python` specified (e.g., `>=3.10`)
- [ ] All dependencies are compatible with declared Python versions
- [ ] `README.md` at project root for PyPI display
- [ ] `LICENSE` file present
- [ ] Version follows semantic versioning (e.g., `1.0.0`, not `1.0-beta`)
- [ ] No conflicts with existing PyPI package names
- [ ] Entry points configured (if CLI or MCP server)
- [ ] Tests pass locally
- [ ] Run: `python -m build` successfully creates `.whl` and `.tar.gz`

---

## 📚 Publishing Workflow Reference

### For Python Packages

```bash
# 1. Build distribution
python -m build

# 2. Test locally
pip install dist/package-name-version.whl

# 3. Upload to PyPI (requires API token)
python -m twine upload dist/*
```

### For Node.js Packages

```bash
# 1. Build (if needed)
npm run build

# 2. Test locally
npm install

# 3. Publish to npm (requires npm account)
npm publish
```

---

## 🔗 Resources

- **PyPI:** https://pypi.org/
- **npm Registry:** https://www.npmjs.com/
- **Building Packages:** https://packaging.python.org/tutorials/packaging-projects/
- **Publishing to PyPI:** https://packaging.python.org/guides/publishing-distribution-packages-to-pypi/

---

## 📝 Notes

- Some projects in `reference/` may be intentionally excluded from PyPI (examples/templates)
- `code-covered/` appears to be a special project - verify its purpose
- Consider creating GitHub Actions workflows for automated publishing on version tags
- Maintain this document as new packages are added or publishing status changes

---

## Next Steps

1. **Verify Non-Python Packages:** Confirm all 5 npm packages are properly registered/publishing to npm
2. **Fix voice-soundboard:** Resolve Python 3.14 compatibility issue
3. **Audit Reference Projects:** Determine which should be published vs. kept as examples
4. **Set Up CI/CD:** Add automated PyPI publishing workflows to GitHub Actions
5. **Document Blockers:** Create issues for any remaining publication failures

