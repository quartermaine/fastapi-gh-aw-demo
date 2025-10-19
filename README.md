# 🧠 FastAPI + GitHub Agentic Workflows (GH-AW) Demo

This project demonstrates how to use **GitHub Agentic Workflows (GH-AW)** with **GitHub Copilot** to automatically generate and maintain project documentation from code — on every push.

---

## ⚙️ Overview

This repository uses **[GitHub Agentic Workflows (GH-AW)](https://githubnext.github.io/gh-aw/)** — an experimental GitHub CLI extension that enables AI-powered automation through workflows defined in Markdown.

When you push changes to this repo or manually run the workflow, the **`update-docs`** workflow automatically:
- Analyzes your code and structure,
- Generates or updates Markdown documentation under the `docs/` folder,
- Updates the project’s `README.md`,
- And (optionally) opens a pull request with the changes.

---

## 🧩 Prerequisites

Before running the workflow, make sure you have the following:

- ✅ **A GitHub Copilot subscription**
- ✅ **GitHub CLI (`gh`) installed and authenticated**
- ✅ **A fine-grained personal access token (PAT)** with the following properties:

### 🔐 Token Setup — `COPILOT_CLI_TOKEN`

Create a fine-grained token at  
👉 [https://github.com/settings/tokens?type=beta](https://github.com/settings/tokens?type=beta)

| Section | Setting | Access |
|----------|----------|--------|
| **Repository access** | All repositories | ✅ |
| **Repository permissions** | Actions | Read & Write |
| | Issues | Read-only |
| | Pull requests | Read & Write |
| | Workflows | Read & Write |
| **Account permissions** | Copilot Requests | Read-only |

Save this token as a **repository secret** named:

```

COPILOT_CLI_TOKEN

````

### ⚙️ Repository Settings

In your repository:

- Go to **Settings → Actions → General**  
  → Under **Workflow permissions**, check:  
  ✅ “Allow GitHub Actions to create and approve pull requests”

---

## 🚀 Setup Instructions

### 1️⃣ Log in to GitHub CLI

```bash
gh auth login --web -h github.com
````

### 2️⃣ Install the GitHub Agentic Workflows extension

```bash
gh extension install githubnext/gh-aw
```

### 3️⃣ Add a sample workflow

```bash
gh aw add githubnext/agentics/update-docs
```

### 4️⃣ Compile the workflow

```bash
gh aw compile
```

### 5️⃣ Run the workflow (and auto-merge PRs)

```bash
gh aw run update-docs --automerge-prs
```

---

## 🧾 What Happens When You Run It

* The **GitHub Agentic Workflow** runs a local or CI process via the Copilot CLI.
* It uses the context from your repository to create or update documentation.
* It pushes changes to a branch or opens a pull request (if permissions allow).
* The documentation follows the **[Diátaxis framework](https://diataxis.fr/)** for clarity and structure:

  * `docs/tutorial.md`
  * `docs/how-to.md`
  * `docs/reference.md`
  * `docs/explanation.md`

---

## 📚 Result

Once completed, your repository will include:

| File                  | Description                                       |
| --------------------- | ------------------------------------------------- |
| `README.md`           | Overview of the project and workflow instructions |
| `docs/tutorial.md`    | Hands-on learning guide                           |
| `docs/how-to.md`      | Task-oriented guides                              |
| `docs/reference.md`   | Technical and API reference                       |
| `docs/explanation.md` | Architecture and rationale documentation          |

---

## 🧠 Notes

* You can manually re-run the workflow anytime with:

  ```bash
  gh aw run update-docs
  ```
* For private repositories, ensure your `COPILOT_CLI_TOKEN` has `repo` and `workflow` scopes.
* For public repositories, the default GitHub token permissions usually suffice.

---

## 🧩 Credits & related links

References, upstream projects, and quick-start resources for agentic workflows:

- [GitHub Next — Agentic Workflows](https://githubnext.github.io/gh-aw/)
- [Agentic workflows quick-start tutorial](https://githubnext.github.io/gh-aw/start-here/quick-start/)
- [Agentics repository](https://github.com/githubnext/agentics)
- [GH-AW repository](https://github.com/githubnext/gh-aw)
- [GitHub Copilot CLI](https://github.com/githubnext/cli)
- [FastAPI](https://fastapi.tiangolo.com/)



