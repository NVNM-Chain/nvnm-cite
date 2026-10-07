# Package version lives in pyproject.toml and a few hardcoded copies.
# Bump here in the PR (also refreshes uv.lock); CI tags vX.Y.Z after merge.
# Does not commit or tag.

.PHONY: version bump-patch bump-minor bump-major bump

PYTHON ?= python3

version:
	@$(PYTHON) scripts/bump_version.py --print

bump-patch:
	@$(PYTHON) scripts/bump_version.py patch

bump-minor:
	@$(PYTHON) scripts/bump_version.py minor

bump-major:
	@$(PYTHON) scripts/bump_version.py major

# make bump VERSION=1.0.0
bump:
	@test -n "$(VERSION)" || (echo "usage: make bump VERSION=X.Y.Z" >&2; exit 1)
	@$(PYTHON) scripts/bump_version.py $(VERSION)
