

## 1. Project Overview

The **Project Workspace Navigator Using MCP** is a read-only Agentic AI project designed to help developers understand unfamiliar codebases.

When developers join an existing project, they often need to find where authentication is implemented, which files handle password resets, or where deployment settings are configured. Manually searching through a large repository can be time-consuming.

This project uses the **Model Context Protocol (MCP)** to access workspace tools, search for relevant files, inspect project documentation, and gather evidence. The agent then provides clear explanations based on the actual project files without modifying the workspace.

## 2. Problem Statement

Developers working with unfamiliar codebases often face challenges such as:

- Finding the implementation of a specific feature.
- Identifying files involved in a particular workflow.
- Locating configuration and deployment settings.
- Understanding relationships between different modules.
- Determining which files may be affected by a proposed change.

An AI model without access to the actual workspace cannot reliably identify the correct files or explain the project's real structure.

## 3. Proposed Solution

The Project Workspace Navigator is an AI agent that investigates a project workspace using MCP-exposed capabilities.

The agent follows these steps:

1. Understand the user's question.
2. Select the appropriate MCP tool.
3. Search relevant directories, filenames, or file contents.
4. Read selected files to gather evidence.
5. Refine the search when the results are incomplete.
6. Connect related files and understand their relationships.
7. Generate an explanation supported by the gathered evidence.

**Important:** The initial version is strictly read-only. The agent can investigate and recommend changes, but it cannot create, edit, delete, or execute project files.

## 4. Main Objectives

- Help developers navigate unfamiliar codebases.
- Identify files related to specific features.
- Explain the relationships between files and modules.
- Locate project configurations and documentation.
- Select tools according to the user's question.
- Minimize unnecessary file searches and reading.
- Provide evidence-based explanations.
- Handle sensitive information safely.
- Maintain a strictly read-only workspace boundary.

## 5. System Architecture

The conceptual architecture consists of the following components:

1. **User Question** — The developer asks a question about the project.
2. **Workspace Navigator Agent** — Interprets the question and plans an investigation.
3. **MCP Workspace Tools** — Provides capabilities to list directories, search files, and inspect selected files.
4. **Evidence Collection** — Gathers relevant information from the workspace.
5. **Navigation and Verification** — Refines searches and verifies findings.
6. **Evidence-Based Explanation** — Presents the answer with relevant file paths and supporting evidence.

### Architecture Flow

```text
User Question
     |
     v
Workspace Navigator Agent
     |
     v
Select Appropriate MCP Tool
     |
     v
List / Search Files
     |
     v
Read Relevant Files
     |
     v
Verify and Connect Evidence
     |
     v
Evidence-Based Explanation
```

The agent repeats the discovery process when additional information is required.

## 6. MCP Capabilities

Depending on the connected MCP server, the agent may use the following capabilities:

| Capability | Purpose |
|---|---|
| List Directories | Understand the project structure |
| Search Filenames | Locate files by name or pattern |
| Search File Contents | Find relevant code, functions, and keywords |
| Read Files | Inspect selected files for detailed evidence |
| Inspect Documentation | Understand project conventions and workflows |
| Inspect Metadata | Identify project technologies and configuration |

The exact available tools depend on the MCP server implementation.

## 7. A.G.E.N.T. Framework

This project follows the A.G.E.N.T. design lifecycle.

### A — Aim

Help developers understand unfamiliar projects by autonomously selecting and using read-only workspace tools.

The agent should identify feature implementations, locate configuration files, explain workflows, and recommend potential integration points.

**Boundary:** The agent must not modify or execute project files.

### G — Gather

Collect the minimum relevant evidence required to answer the user's question.

The agent can list directories, search filenames and file contents, read selected files, and inspect documentation or metadata.

The objective is to avoid scanning the entire repository unnecessarily.

### E — Execution

The agent interprets the question, selects an appropriate MCP capability, observes the result, and determines whether another investigation step is necessary.

The execution loop is:

**Think → Select Tool → Execute → Observe → Decide → Repeat or Answer**

For example, when asked where rate limiting should be implemented, the agent can inspect API routes, existing middleware, and configuration conventions before recommending an appropriate integration point.

### N — Navigation

The agent adapts its investigation when the initial search does not provide sufficient evidence.

Examples include:

- File not found: Try alternative search terms or directories.
- Too many results: Narrow the search scope.
- Insufficient context: Inspect related files.
- Unexpected architecture: Adjust the investigation strategy.
- Sensitive content encountered: Avoid exposing secrets in the response.

The navigation process follows:

**DISCOVER → SEARCH → INSPECT → VERIFY → EXPLAIN**

### T — Test

Validate the agent's tool selection, search efficiency, explanation accuracy, and safe handling of sensitive information.

Testing should cover normal requests, ambiguous questions, missing files, large repositories, and incomplete search results.

## 8. Example Use Cases

### Find Authentication Implementation

**User question:** Where is authentication implemented?

**Expected behavior:** Search for authentication-related files, inspect relevant modules, and explain how the files work together.

### Investigate Password Reset

**User question:** Which files are involved in password reset?

**Expected behavior:** Locate relevant routes, controllers, services, and related configuration where applicable, then explain their relationships.

### Locate Deployment Configuration

**User question:** Where is deployment configured?

**Expected behavior:** Search for deployment files and inspect relevant configuration or documentation.

### Recommend a Rate-Limiting Integration Point

**User question:** Where should rate limiting be implemented?

**Expected behavior:** Inspect API routes, middleware patterns, and configuration conventions before explaining possible integration points and supporting evidence.

### Handle Missing Files

**User question:** Where is the payment service implemented?

**Expected behavior:** If the expected file cannot be found, broaden the search or investigate alternative names and modules rather than inventing a file path.

## 9. Testing Scenarios

| Test Scenario | Expected Behavior |
|---|---|
| Find authentication implementation | Locate relevant files and explain their relationships |
| Feature spans multiple modules | Connect evidence across the relevant modules |
| Expected file does not exist | Search alternative locations or patterns |
| Large repository | Avoid reading the entire workspace |
| Search returns irrelevant results | Refine the search strategy |
| Sensitive configuration is encountered | Avoid exposing secrets |
| Ambiguous feature name | Investigate likely interpretations or ask for clarification |
| Insufficient evidence | Continue investigating or clearly state the limitation |
| Read-only boundary | Never modify, delete, create, or execute project files |

## 10. Safety and Limitations

- **Read-only access:** The agent must not modify project files.
- **Evidence-based answers:** Findings should be supported by inspected workspace evidence.
- **Limited access:** The agent can only inspect information exposed by its MCP tools and permissions.
- **Sensitive information:** Secrets, credentials, and tokens must not be reproduced in answers.
- **Search limitations:** Incorrect terminology or incomplete indexing may require alternative searches.
- **No unsupported assumptions:** The agent should distinguish verified findings from recommendations and uncertainty.
- **No guaranteed completeness:** The agent may miss information when tools cannot access relevant files.

## 11. Expected Outcomes

By completing this project, the system should demonstrate the ability to:

- Understand user questions about an existing codebase.
- Select suitable tools autonomously.
- Gather relevant evidence from multiple files.
- Adapt its search strategy based on tool results.
- Explain code organization and relationships.
- Provide practical recommendations grounded in project evidence.
- Respect read-only and information-safety boundaries.

## 12. Key Principle

An agent does not need to know everything in advance. It needs to know how to acquire the information required to answer a question reliably.

The Project Workspace Navigator demonstrates the transition from autonomous reasoning to **autonomous capability selection**, using MCP to investigate real project workspaces.

## 13. Conclusion

The Project Workspace Navigator Using MCP provides a structured approach to understanding unfamiliar software projects. By combining autonomous tool selection, selective evidence gathering, adaptive navigation, and evidence-based explanations, it helps developers find relevant information more efficiently while maintaining a strictly read-only boundary.

This project establishes a foundation for more advanced agentic systems that can interact with development environments through controlled and clearly defined capabilities.