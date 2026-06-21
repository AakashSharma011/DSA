# Contributing to DSA in Python

First off, thank you for considering contributing to this project! It's people like you who make this repository an excellent reference for the community.

## 🚀 How Can I Contribute?

### 1. Adding New Data Structures/Algorithms
If you want to implement a new data structure (e.g., Trees, Graphs) or algorithm (e.g., Dijkstra's, QuickSort):
- Create a new folder if the category doesn't exist (e.g., `Trees/`).
- Write clean, commented Python code.
- Add dynamic tests/demonstration in the `if __name__ == "__main__":` block.
- Update the root `README.md` progress tracker.

### 2. Bug Reports & Refactoring
If you find a bug in the existing code or want to optimize an operation:
- Open an Issue describing the bug or performance bottleneck.
- Implement the fix in a separate branch (see below).

---

## 🌿 Branching Strategy

We follow a modular feature branch strategy:
- `main` - The production-ready stable branch.
- `feature/feature-name` - For new implementations.
- `fix/bug-name` - For bug fixes.
- `docs/doc-name` - For documentation changes.
- `refactor/refactor-name` - For code quality improvements.

---

## 📝 Commit Message Format

We enforce semantic commit messages to keep the history clean and readable:
- `feat:` for new features or implementations.
- `fix:` for bug fixes.
- `docs:` for documentation updates.
- `refactor:` for code cleanups/performance changes.
- `test:` for adding or improving test code.
- `chore:` for repository setup/maintenance tasks.

*Example:* `feat: add binary search tree implementation`

---

## 📬 Pull Request Process

1. Create a new branch from `main`.
2. Commit your changes with descriptive messages.
3. Open a Pull Request pointing to `main`.
4. Ensure your code compiles and executes successfully without warnings.
5. Link any related issues by writing `Closes #IssueNumber` in the PR description.
