# Agent Guidelines

## Code Golf Optimization Best Practices

### Verification and Testing
- Always verify code changes with `VerifyCode.py` before finalizing optimizations
- Use single-threaded verification to avoid hanging issues
- Test incrementally rather than making bulk changes

### Command Execution
- **Avoid `python -c` commands** - these can hang during verification and cause timeouts
- Use script files instead of inline code execution
- Prefer direct file execution over subprocess calls when possible

### Safe Optimization Strategies
- Apply conservative optimizations first (trailing whitespace, safe spacing)
- Use function aliasing only when benefits clearly outweigh overhead
- Test syntax with `compile()` before applying changes
- Implement rollback mechanisms for failed optimizations

### Performance Considerations
- Some tasks may have complex logic that causes verification timeouts
- Use shorter timeout periods (10-15 seconds) for initial testing
- Consider skipping files that consistently timeout during verification

### Code Organization
- **Keep only VerifyCode.py in the root directory** - all other scripts should be organized in subfolders
- Move all AI-generated optimization scripts to the `AI/` subfolder for better organization
- Maintain clean workspace structure with `Code/`, `Reduced/`, and `AI/` directories
- **Run AI scripts from the root directory** - use `python3 AI/script_name.py` to maintain correct relative paths to `Code/` and `Reduced/` folders