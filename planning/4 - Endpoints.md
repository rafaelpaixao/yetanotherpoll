# API Endpoints

> **POST** /login/

- Without token:
  - Provides user token
- With guest token:
  - Provides user token and associate all guest polls and votes with the non guest user.

---

> **POST** /register/

- Without token:
  - Creates a new user.
- With guest token:
  - Creates a new user and associate all guest polls and votes with the non guest user.

---

> **GET** /poll/

- With token:
  - List polls authored by user.

---

> **POST** /poll/

- Without token:
  - Creates a poll and a new guest user.
- With token:
  - Creates a poll.

---

> **GET** /poll/:id/

- Fetch poll with id.

---

> **PUT** /poll/:id/

- With token:
  - Edit poll, if user is author.

---

> **GET** /poll/:id/results/

- Fetch poll's results.

---

> **POST** /poll/:id/vote/

- Without token:
  - Vote on poll, if poll allows vote without login, and creates a new guest user.
- With token:
  - Vote on poll. If user already has a vote, change it.

---
