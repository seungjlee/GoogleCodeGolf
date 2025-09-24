# Agent Guidelines

## Code Golf Optimization Best Practices

### Verification and Testing
- Always verify code changes with `VerifyCode.py` before finalizing optimizations.
- For verifying a specific task script `./VerifyCode.py ./Reduced <task_number>`
- Use single-threaded verification to avoid hanging issues.
- Test incrementally rather than making bulk changes.

### Command Execution
- **Avoid `python -c` commands** - these can hang during verification and cause timeouts.
- Use script files instead of inline code execution.
- Prefer direct file execution over subprocess calls when possible.

### Safe Optimization Strategies
- Apply conservative optimizations first (trailing whitespace, safe spacing).
- Use function aliasing only when benefits clearly outweigh overhead.
- Test syntax with `compile()` before applying changes.
- Implement rollback mechanisms for failed optimizations. Use 'git restore' if needed.
- Remove unused code and unused variables.
- Replace all tabs with spaces but make sure indentations are still correct. Single space indentation.
- Remove all trailing spaces.
- Remove all extra end of line characters at the end of file.
- Shorten function names.
- Remove all constants that are just a digit or two. Replace the constant with the actual value in the code.
- Try to keep local variables in lower case and globals and function names in upper case for organization and to reduce conflicts.
- Correctly create globals that start with upper case to replace repeatedly used words like range, tuple, len, list, sorted, if it saves bytes. Change local variables to lower case if possible so that we can use more single letter upper case variables for globals. It is easier to start changing local variables to lower case and then use remaining upper case letters for globals. Note that 'p' is reserved.
- If possible, replace True with 1 and False with 0.
- Usually x.append(y) can be replaced by x+=[y]. x.extend(y) can be replaced by x+=y.

### Performance Considerations
- Some tasks may have complex logic that causes verification timeouts.
- Use shorter timeout periods (10-15 seconds) for initial testing.
- Consider skipping files that consistently timeout during verification.

### Code Organization
- **Keep only VerifyCode.py in the root directory** - all other scripts should be organized in subfolders.
- Move all AI-generated optimization scripts to the `AI/` subfolder for better organization.
- Maintain clean workspace structure with `Code/`, `Reduced/`, and `AI/` directories.
- **Run AI scripts from the root directory** - use `python3 AI/script_name.py` to maintain correct relative paths to `Code/` and `Reduced/` folders.