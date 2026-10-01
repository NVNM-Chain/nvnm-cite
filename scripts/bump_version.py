"""Bump the package version in every file that hardcodes it.

Does not commit, tag, or push. After the PR merges, CI tags vX.Y.Z.
Does not touch NORMALIZER_VERSION.
"""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"
SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def current_version() -> str:
    data = tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))
    ver = data["project"]["version"]
    if not SEMVER.match(ver):
        raise SystemExit(f"pyproject version is not MAJOR.MINOR.PATCH: {ver}")
    return ver


def next_version(current: str, how: str) -> str:
    if SEMVER.match(how):
        return how
    maj, minor, pat = (int(p) for p in current.split("."))
    if how == "patch":
        return f"{maj}.{minor}.{pat + 1}"
    if how == "minor":
        return f"{maj}.{minor + 1}.0"
    if how == "major":
        return f"{maj + 1}.0.0"
    raise SystemExit(f"usage: bump_version.py patch|minor|major|X.Y.Z (got {how!r})")


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise SystemExit(f"{path}: expected exactly one {old!r}, found {text.count(old)}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def apply(old: str, new: str) -> None:
    replace_once(PYPROJECT, f'version = "{old}"', f'version = "{new}"')
    replace_once(ROOT / "src/nvnm_cite/__init__.py", f'__version__ = "{old}"', f'__version__ = "{new}"')
    replace_once(
        ROOT / "src/nvnm_cite/webapp/service.py",
        f'WEBAPP_VERSION = "{old}"',
        f'WEBAPP_VERSION = "{new}"',
    )
    replace_once(
        ROOT / "src/nvnm_cite/webapp/server.py",
        f'server_version = "nvnm-cite-web/{old}"',
        f'server_version = "nvnm-cite-web/{new}"',
    )
    replace_once(
        ROOT / "src/nvnm_cite/webapp/static/openapi.json",
        f'"version": "{old}"',
        f'"version": "{new}"',
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", nargs="?", help="patch, minor, major, or X.Y.Z")
    parser.add_argument("--print", action="store_true", dest="print_only")
    args = parser.parse_args()
    old = current_version()
    if args.print_only or args.spec is None:
        print(old)
        return
    new = next_version(old, args.spec)
    if new == old:
        print(f"{old} unchanged")
        return
    apply(old, new)
    print(f"{old} → {new}")
    print("Commit this in the PR. After merge, CI tags v" + new + ".")


if __name__ == "__main__":
    sys.exit(main())
