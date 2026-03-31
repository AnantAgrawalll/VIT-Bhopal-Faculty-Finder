# VIT-Bhopal-Faculty-Finder
# FacultyBot — VIT Bhopal Faculty Finder

A command-line **Intelligent Agent** built in Python that helps VIT Bhopal students find which professor teaches which subject, along with cabin location, email, and availability — without searching notice boards or WhatsApp groups.

**Course:** CSA2001 – Fundamentals in AI and ML | VIT Bhopal

---

## Problem Statement

Every semester, students struggle to find basic faculty information — who teaches their subject, where the professor sits, and when to visit. This information is scattered and hard to access. FacultyBot solves this with a single CLI tool.

---

## Features

| Query | Example |
|-------|---------|
| Find by subject | `Who teaches Python?` |
| Find by name | `Tell me about Dr. Jyoti` |
| Cabin location | `Where is Dr. Sharma's cabin?` |
| Email address | `Email of Dr. Rakesh` |
| Availability | `When is Dr. Muneeswaran available?` |
| List all faculty | `show all` |

---

## AI Concept — Intelligent Agent (CSA2001 CO1)

FacultyBot implements the **Perceive → Reason → Act** agent loop:

```
User Input  →  clean/preprocess  (PERCEIVE)
            →  detect intent + search knowledge base  (REASON)
            →  format and return response  (ACT)
            →  store in history  (MEMORY)
```

---

## Requirements

- Python 3.7+
- No external libraries needed

---

## Setup

```bash
git clone https://github.com/{your-username}/faculty-bot
cd faculty-bot
python chatbot.py
```

> Use `python3` on Linux/Mac

---

## Example

```
====================================================
   FACULTYBOT — VIT Bhopal Faculty Finder
   Intelligent Agent  |  CSA2001  |  Python
====================================================

  You: who teaches machine learning

  Bot:
  Name  : Dr. Jyoti Chauhan  (CSE)
  Cabin : Block B, Room 312
  Email : jyoti.chauhan@vitbhopal.ac.in
  Hours : Mon-Thu 2PM-4PM
  Teach : ai, machine learning, csa2001

  You: show all

  Bot:
  #   Name                   Subject              Cabin
  -------------------------------------------------------
  1   Dr. Muneeswaran V      python               Block A, Room 204
  2   Dr. Jyoti Chauhan      ai                   Block B, Room 312
  ...
```

---

## Commands

| Command | Description |
|---------|-------------|
| `help` | Show usage guide |
| `show all` | List all faculty |
| `history` | Show conversation history |
| `bye` / `exit` | Quit |

---

## File Structure

```
faculty-bot/
├── chatbot.py        # Main program
├── README.md         # This file
└── PROJECT_REPORT.md # Project report
```

> Faculty data is representative and used for academic demonstration purposes.

**Author:** VIT Bhopal | CSA2001
