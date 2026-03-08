# rpmlint GitHub Action

A GitHub Actions composite action that runs [rpmlint](https://github.com/rpm-software-management/rpmlint) on RPM spec files.

## Usage

```yaml
steps:
  - uses: actions/checkout@v6

  - uses: reishoku/actions.rpmlint@v1
```

### With custom configuration

```yaml
steps:
  - uses: actions/checkout@v6

  - uses: reishoku/actions.rpmlint@v1
    with:
      config: .rpmlint.toml
      path: .
      strict: 'true'
```

## Inputs

| Name | Description | Required | Default |
|------|-------------|----------|---------|
| `config` | Path to rpmlint configuration file | No | `.rpmlint.toml` |
| `path` | Directory to search for spec files | No | `.` |
| `strict` | Treat warnings as errors (`--strict`) | No | `false` |

## Behavior

- Installs `python3-rpm` (RPM Python bindings) and `rpmlint` via pip.
- Searches for `*.spec` files in the specified directory (non-recursive).
- If a configuration file is found at the specified path, it is passed to rpmlint with `-c`.
- If no spec files are found, a warning is emitted and the step succeeds.
- Runs on Ubuntu-based GitHub-hosted runners.

## Configuration

Create a `.rpmlint.toml` file in your repository to customize rpmlint behavior:

```toml
Filters = [
    ".*spelling-error.*",
]
```

See `rpmlint --explain <check-id>` for details on individual checks.

## License

This project is provided as-is without a formal license.
