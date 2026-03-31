# Project Report — FacultyBot
## VIT Bhopal Faculty Finder | CSA2001 – Fundamentals in AI and ML

| Field | Details |
|-------|---------|
| Course | CSA2001 – Fundamentals in AI and ML |
| Institution | VIT Bhopal University |
| Project Type | BYOP – Bring Your Own Project |
| Language | Python 3 |
| Libraries | `random`, `re` (standard library only) |

---

## 1. Problem Identified

At VIT Bhopal, I noticed that students frequently struggle to find basic faculty information at the start of every semester. Questions like "Who teaches AI?", "Where is Dr. Jyoti's cabin?", and "When can I meet Dr. Muneeswaran?" get repeated constantly in class WhatsApp groups. The information exists, but it is scattered across notice boards, course pages, and word of mouth. There is no single quick-access tool for this.

This is a small but genuine daily friction that every student faces. I chose to solve it as my BYOP project because it is a real problem I personally experienced, and because it maps directly to the Intelligent Agent concept from CSA2001 CO1.

---

## 2. Solution

FacultyBot is a command-line chatbot that acts as an Intelligent Agent. A student types a natural language query — such as "Who teaches Python?" or "Cabin of Dr. Anita" — and the agent immediately returns the relevant information. No GUI, no internet, no login required.

---

## 3. AI Concept — Intelligent Agent (CSA2001 CO1)

This project directly implements the Intelligent Agent architecture from Russell & Norvig (Chapter 2), which is the core topic of CSA2001 CO1.

An Intelligent Agent perceives its environment, reasons about the percept, and acts to achieve a goal.

| Agent Component | In FacultyBot |
|----------------|--------------|
| Environment | Student's typed text |
| Sensor | `input()` — keyboard |
| Percept | Raw query string |
| Agent Program | `respond()` function |
| Reasoning | `find_faculty()` + `intent()` |
| Actuator | `print()` — terminal output |
| Goal | Return correct faculty information |
| Memory | `history` list |

FacultyBot is a **Goal-Based Agent**: it does not just react to keywords — it first determines *what* the user wants (cabin, email, availability, or all details) using `intent()`, then searches the knowledge base, and responds with only the relevant information.

---

## 4. Syllabus Coverage

### CSA2001 – Fundamentals in AI and ML

| CO | Topic | Where Applied |
|----|-------|--------------|
| CO1 | Intelligent Agents | Entire agent architecture — perceive, reason, act |
| CO1 | Goal-Based Agent | `intent()` classifies goal before responding |
| CO1 | Agent Memory | `history` list stores all exchanges |
| CO2 | Knowledge Representation | `FACULTY_DB` encodes facts as structured dictionaries |
| CO2 | Rule-Based Reasoning | `RESPONSES` dict maps patterns to answers |

### CSE1021 – Introduction to Problem Solving and Programming

| Unit | Topic | Where Applied |
|------|-------|--------------|
| Unit 2 | Functions, Parameters | `clean()`, `find_faculty()`, `intent()`, `format_result()` |
| Unit 3 | Conditionals, Loops | Intent detection `if-elif` chain, subject matching loop |
| Unit 5 | Lists, Dictionaries | `FACULTY_DB`, `RESPONSES`, `history` |

---

## 5. System Design

### Knowledge Base

`FACULTY_DB` is a list of 10 dictionaries. Each dictionary is one faculty member:

```python
{
    "name":      "Dr. Jyoti Chauhan",
    "subjects":  ["ai", "machine learning", "csa2001"],
    "cabin":     "Block B, Room 312",
    "email":     "jyoti.chauhan@vitbhopal.ac.in",
    "available": "Mon-Thu 2PM-4PM",
    "dept":      "CSE"
}
```

### Agent Decision Flow

```
User types: "where is dr jyoti cabin"
        |
        v
clean() → "where is dr jyoti cabin"
        |
        v
intent() → scans for cabin/email/available keywords → "cabin"
        |
        v
find_faculty() → name match on "jyoti" → Dr. Jyoti Chauhan
        |
        v
format_result(faculty, mode="cabin") → shows cabin only
        |
        v
Output: "Name: Dr. Jyoti Chauhan  Cabin: Block B, Room 312"
```

### Intent Classification

| Intent | Trigger Words | Shows |
|--------|--------------|-------|
| `cabin` | cabin, room, office, where, location | Cabin only |
| `email` | email, mail, contact | Email only |
| `available` | available, timing, when, schedule | Hours only |
| `all` | (none matched) | All details |

---

## 6. Test Results

| Input | Expected | Matched |
|-------|----------|---------|
| `who teaches python` | Dr. Muneeswaran V | Yes |
| `cabin of dr jyoti` | Block B, Room 312 | Yes |
| `email of dr rakesh` | rakesh.verma@vitbhopal.ac.in | Yes |
| `when is dr sharma available` | Mon-Wed 9AM-11AM | Yes |
| `who teaches dbms` | Dr. Anita Sharma | Yes |
| `show all` | All 10 faculty | Yes |
| `who teaches quantum` | Not found message | Yes |
| `hello` | Greeting response | Yes |

**Accuracy: 100% on tested queries**

---

## 7. Challenges

**1. Partial name matching:** Students type "Dr. Jyoti" not the full name. Solved by splitting names into parts and matching any part longer than 3 characters.

**2. Focused responses:** Without intent detection, every query returned all details which was noisy. Adding `intent()` made responses clean and precise.

**3. Subject overlap:** "ai" could match unrelated queries. Solved by checking full subject phrases first before falling back to word-level matching.

---

## 8. What I Learned

Writing this project made the Intelligent Agent concept from the textbook feel real. The perceive-reason-act loop is not abstract theory — it is literally the structure of the `respond()` function. I also learned that good knowledge representation (the `FACULTY_DB` dictionary design) is more important than complex algorithms. A well-structured knowledge base made the reasoning logic simple and reliable.

---

## 9. Conclusion

FacultyBot solves a real problem observed in my daily campus life using a properly structured Intelligent Agent. It demonstrates CSA2001 CO1 (Intelligent Agents), CO2 (Knowledge Representation), and core Python programming from CSE1021 — all in a working, useful CLI application that any VIT Bhopal student can run immediately.

---

## 10. References

1. Russell, S. & Norvig, P. — *Artificial Intelligence: A Modern Approach*, 3rd Ed., Prentice Hall, 2009.
2. Alpaydin, E. — *Machine Learning: The New AI*, MIT Press, 2016.
3. Dierbach, C. — *Introduction to Computer Science Using Python*, Wiley, 2015.
4. Dromey, R.G. — *How to Solve it by Computer*, PHI.
5. Python 3 Docs — https://docs.python.org/3/
