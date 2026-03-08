# AGENTS.md

## Project overview

This repository provides a reusable GitHub Actions composite action that runs [rpmlint](https://github.com/rpm-software-management/rpmlint) on RPM spec files. It is designed to be consumed by other repositories via `uses: reishoku/actions.rpmlint@v1`.

## Repository structure

```
action.yml              # Composite action definition (the main deliverable)
tests/hello.spec        # Test spec file used by CI
tests/.rpmlint.toml     # Test rpmlint configuration
.github/workflows/test.yml  # CI workflow that tests the action itself
.github/dependabot.yml  # Dependabot configuration for github-actions
```

## Key design decisions

- **rpmlint is installed from the Ubuntu apt repository** (`apt-get install rpmlint`), not from PyPI. The RPM Python bindings (`python3-rpm`) are pulled in as a dependency automatically.
- **The action runs on Ubuntu-based GitHub-hosted runners only.** The rpmlint version is tied to the Ubuntu release (currently 2.5.0 on Ubuntu 24.04).
- **No external GitHub Actions dependencies** in the action itself. Installation is done purely via apt.
- **Spec file search is non-recursive** (`-maxdepth 1` in find). The `path` input controls which directory to search.

## Action inputs

| Input | Default | Description |
|-------|---------|-------------|
| `config` | `.rpmlint.toml` | Path to rpmlint configuration file |
| `path` | `.` | Directory to search for spec files |
| `strict` | `false` | Treat warnings as errors (`--strict`) |

## Development guidelines

### Modifying the action

- `action.yml` is the composite action definition. All steps must have `shell: bash`.
- User inputs are passed to shell scripts via `env:` blocks (not inline `${{ }}` in `run:`) to prevent command injection.
- Validate changes with `yamllint`, `actionlint`, and `editorconfig-checker` before committing.
- Shell scripts embedded in `action.yml` should pass `shellcheck`.

### Testing

- The CI workflow (`.github/workflows/test.yml`) tests the action by running it against `tests/hello.spec`.
- Four test jobs cover: default mode, strict mode, no spec files, and custom config.
- The test workflow triggers on changes to `action.yml`, `.github/workflows/test.yml`, or `tests/**`.
- `tests/hello.spec` must pass both default and strict rpmlint modes. Include all required spec sections (`%prep`, `%build`, `%install`, `%check`) and a `BuildRoot:` tag.

### Linting and validation

- `yamllint` with `.yamllint` config for YAML files
- `actionlint` for GitHub Actions workflow files
- `editorconfig-checker` with `.editorconfig` for formatting
- `shellcheck` with `.shellcheckrc` for shell scripts

### Branching

- Create topic branches for all changes.
- The default branch is `reishoku`.
