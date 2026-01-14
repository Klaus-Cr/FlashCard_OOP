# 📌 Application Description

This project is an object-oriented refactoring of an existing flashcard-based language learning application.

While the functional behavior remains unchanged from the non-OOP version, the primary focus of this implementation is **clean architecture** and **clear separation of concerns**.

---

## 🧱 Architectural Overview

The application follows a **Controller–View–Domain** architecture, ensuring that each layer has a single, well-defined responsibility.

---

## 🧠 Domain Layer

- Contains the core business logic
- Manages vocabulary data, training rules, and application state
- Independent of UI and infrastructure concerns

---

## 🎮 Controller Layer

- Acts as the central coordinator of the application
- Handles user interactions and application flow
- Delegates responsibilities between domain and view layers

---

## 🖥️ View Layer

- Responsible for rendering the user interface
- Captures user input and forwards events to the controller
- Contains no business logic

---

## 🎯 Design Goals

This architectural approach emphasizes:

- 🧩 Separation of responsibilities
- 🛠️ Maintainability and extensibility
- 🧪 Testable, UI-independent logic
- 🚀 Scalability for future enhancements

---

## 📦 Summary

This project demonstrates the transition from a **procedural implementation** to a **clean, object-oriented design** with well-defined architectural boundaries.

The focus lies on **structure, readability, and code quality**, rather than on introducing new features.

---

## ❗ Acknowledgments

The overall project structure, architectural decisions (MVC-style separation), and documentation approach were developed with the assistance of **ChatGPT**.

This includes guidance on:

- folder layout
- class responsibilities
- callback design
- type annotations
- docstring conventions

All implementation decisions and final code were written and reviewed by the author.
