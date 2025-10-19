# Automation and Workflows

This guide explains the automated workflows that help maintain the FastAPI GH AW Demo project.

## Overview

This project uses GitHub Actions with agentic workflows to automate documentation maintenance, ensuring that documentation stays synchronized with code changes.

## Automated Documentation Updates

### Update Docs Workflow

The repository includes an intelligent documentation automation workflow that monitors code changes and maintains documentation quality.

**Workflow File**: `.github/workflows/update-docs.md` (compiled to `update-docs.lock.yml`)

**Triggers**:
- Automatically runs on every push to the `main` branch
- Can be manually triggered via `workflow_dispatch`
- Time-limited execution (configurable stop-after period)

**What It Does**:

1. **Analyzes Code Changes**: Examines commits to identify new APIs, functions, classes, or configuration changes
2. **Reviews Documentation**: Checks existing documentation for accuracy and completeness
3. **Identifies Gaps**: Detects missing or outdated documentation
4. **Creates Updates**: Generates documentation following Diátaxis framework principles
5. **Submits Pull Requests**: Creates draft PRs with documentation improvements

### Documentation Framework

The automation follows the [Diátaxis framework](https://diataxis.fr/) to organize documentation into four categories:

- **Tutorials**: Learning-oriented, step-by-step guides
- **How-to Guides**: Problem-oriented, practical instructions
- **Reference**: Information-oriented, technical specifications
- **Explanation**: Understanding-oriented, conceptual discussions

### Quality Standards

The workflow ensures documentation meets these standards:

- **Clarity**: Plain English, active voice, progressive disclosure
- **Accuracy**: Code examples are tested and functional
- **Accessibility**: Clear structure, searchable content
- **Maintainability**: Documentation as code, version controlled

## GitHub Actions Integration

### Workflow Configuration

The workflow is defined using GitHub Actions Workflow (gh-aw) syntax, which provides:

- **Agentic Capabilities**: AI-powered analysis and documentation generation
- **Safe Operations**: Read-only by default, creates PRs for changes
- **Tool Access**: Web search, file operations, and bash commands
- **Security**: Prompt injection protection and permission controls

### Permissions

The workflow uses minimal permissions:
- **Read-all**: Can read repository contents
- **Creates PRs**: Can create draft pull requests (via safe-outputs)
- **No Direct Writes**: Cannot push directly to protected branches

### Timeout and Limits

- **Execution Time**: 15 minutes maximum per run
- **Stop After**: Workflow expires after configured period (default: 10 days)
- **Network Access**: Full internet access for research and validation

## Using the Workflow

### Manual Trigger

To manually trigger the documentation workflow:

1. Navigate to the Actions tab in GitHub
2. Select "Update Docs" workflow
3. Click "Run workflow"
4. Select the branch and confirm

### Reviewing Generated Documentation

When the workflow creates a pull request:

1. Review the PR description for a summary of changes
2. Check the modified files for accuracy
3. Test any code examples included
4. Request changes or approve the PR
5. Merge when ready

### Customizing the Workflow

To customize the workflow behavior:

1. Edit `.github/workflows/update-docs.md`
2. Modify the job description or configuration
3. Run `gh aw compile` to regenerate the lock file
4. Commit both the `.md` and `.lock.yml` files

**Note**: The `.lock.yml` file is auto-generated. Always edit the `.md` file and recompile.

## Best Practices

### For Contributors

When making code changes:

1. **Write Clear Code**: Use descriptive names and add docstrings
2. **Update Examples**: If API changes, update example code
3. **Review Auto-Generated Docs**: Check PRs from the workflow carefully
4. **Supplement When Needed**: Add manual documentation for complex features

### For Maintainers

To maintain the workflow:

1. **Monitor Workflow Runs**: Check Actions tab for failures
2. **Review Generated PRs**: Provide feedback on automated documentation
3. **Update Instructions**: Refine the workflow job description as needed
4. **Extend Stop Period**: Update stop-after date to keep workflow active

### For Documentation Writers

When working with the automated system:

1. **Follow Diátaxis**: Maintain the established documentation structure
2. **Test Code Examples**: Verify all examples work before merging
3. **Link Appropriately**: Cross-reference related documentation
4. **Keep It Current**: Treat documentation gaps like bugs

## Troubleshooting

### Workflow Not Running

**Symptoms**: No workflow runs appear after pushing to main

**Solutions**:
- Check if the workflow has expired (stop-after date passed)
- Verify the workflow file is in `.github/workflows/`
- Ensure workflow permissions are correctly configured

### Poor Quality Documentation Generated

**Symptoms**: Generated documentation is inaccurate or incomplete

**Solutions**:
- Review and refine the workflow job description
- Add more context in code comments and docstrings
- Provide feedback through PR comments
- Consider manual documentation for complex features

### PR Creation Failed

**Symptoms**: Workflow runs but doesn't create a PR

**Solutions**:
- Check workflow logs for errors
- Verify safe-outputs permissions are configured
- Ensure branch protection rules allow workflow PRs
- Check if there are actual documentation changes needed

## Architecture

### Workflow Components

The automation system consists of several components:

1. **Trigger**: GitHub Actions event system
2. **Agent**: AI-powered documentation analyzer and writer
3. **Tools**: File operations, web search, bash commands
4. **Safe Outputs**: Controlled PR creation mechanism
5. **Security**: XPIA protection and permission management

### Data Flow

```
Code Push → Workflow Trigger → Code Analysis → Documentation Review
    ↓
Gap Detection → Content Generation → Quality Check → PR Creation
    ↓
Human Review → Merge → Updated Documentation
```

## Security Considerations

### Prompt Injection Protection

The workflow includes protection against Cross-Prompt Injection Attacks (XPIA):

- Treats external content as untrusted data
- Ignores instructions embedded in issues or comments
- Validates actions against original task requirements
- Reports suspicious content

### Permission Boundaries

The workflow operates with limited permissions:

- Cannot modify main branch directly
- Cannot access secrets or sensitive data
- Cannot execute arbitrary external code
- Operates within GitHub Actions VM sandbox

## Future Enhancements

Planned improvements to the automation system:

- Automated link checking and validation
- Documentation preview in PR comments
- Integration with external documentation platforms
- Multi-language documentation support
- Automated screenshot generation
- API documentation from OpenAPI specs

## Additional Resources

### GitHub Actions Workflows (gh-aw)

- [gh-aw Documentation](https://github.com/githubnext/gh-aw)
- [Agentic Workflows Guide](https://github.com/githubnext/agentics)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

### Documentation Frameworks

- [Diátaxis Framework](https://diataxis.fr/)
- [Write the Docs](https://www.writethedocs.org/)
- [Google Developer Documentation Style Guide](https://developers.google.com/style)
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)

### Related Topics

- [Development Guide](./development.md) - Contributing to the project
- [Configuration Guide](./configuration.md) - Environment setup
- [API Reference](./api-reference.md) - Endpoint documentation

---

*Last updated: 2025-10-19*
