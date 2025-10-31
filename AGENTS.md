# Project Stack & Guidelines: Python 3.11+

**version**: 1.0

---

## Description

This document outlines the preferred technology stack and guidelines for **any AI agent or developer** working on this project. The focus is on leveraging asynchronous capabilities, type safety, and best-in-class libraries for common development tasks. This stack is optimized for Python 3.11 and newer.

---

## Preferred Stack

This is the default, recommended stack for new Python projects. Each library is chosen for its modern design, performance, and strong community support.

### Core Framework & API
* **`FastAPI`**: The primary web framework for building high-performance, async-native APIs with automatic data validation and documentation.
* **`Pydantic`**: The foundational library for data validation, settings management, and data serialization using Python type hints.

### Database & ORM
* **`SQLAlchemy` (2.0+)**: The preferred Object-Relational Mapper (ORM) for all database interactions, featuring a fully type-hinted and async-capable API.

### Networking & Web Interaction
* **`HTTPX`**: The standard HTTP client for both synchronous and asynchronous requests. It's the modern replacement for `requests`.
* **`Beautiful Soup (BS4)`**: The go-to library for parsing and extracting data from HTML and XML, used for web scraping tasks in conjunction with `HTTPX`.

### Data Science & Manipulation
* **`Pandas`**: The essential library for any data manipulation and analysis involving tabular data (e.g., from CSVs, Excel files, or databases).

### Development Tools & Utilities
* **`Pytest`**: The standard framework for writing clean, scalable, and maintainable tests for both synchronous and async code.
* **`mypy`**: An essential static type checker to enforce type safety and catch bugs before runtime. It is a critical part of the development workflow.
* **`Rich`**: The preferred library for creating beautiful, informative terminal output, logging, and debugging.
* **`Pathlib`**: The built-in, object-oriented module for all filesystem path manipulations, replacing older `os.path` methods.

---

## Rules & Guidelines

1.  **Async First**: For any I/O-bound operation (networking, database calls), asynchronous patterns using `async/await` should be the default choice.
2.  **Type Everything**: All function signatures, variables, and data models should have explicit type hints. Code must pass `mypy --strict` checks.
3.  **Test Rigorously**: All new features and business logic must be accompanied by corresponding unit and integration tests written using `pytest`.
4.  **Dependency Management**: Use a modern dependency manager (like Poetry or PDM) to lock and manage project dependencies via `pyproject.toml`.
