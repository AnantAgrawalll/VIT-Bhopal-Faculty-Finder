import random
import re

FACULTY_DB = [
    {"name": "Dr. Muneeswaran V",     "subjects": ["python", "cse1021", "problem solving", "programming"],        "cabin": "Block A, Room 204", "email": "muneeswaran.v@vitbhopal.ac.in",   "available": "Mon-Fri 10AM-12PM", "dept": "CSE"},
    {"name": "Dr. Jyoti Chauhan",     "subjects": ["ai", "machine learning", "csa2001", "artificial intelligence","ai ml"], "cabin": "Block B, Room 312", "email": "jyoti.chauhan@vitbhopal.ac.in",   "available": "Mon-Thu 2PM-4PM",  "dept": "CSE"},
    {"name": "Dr. Pradeep K Mishra",  "subjects": ["data structures", "algorithms", "dsa", "csa1002"],            "cabin": "Block B, Room 308", "email": "pradeep.mishra@vitbhopal.ac.in",  "available": "Tue-Fri 11AM-1PM",  "dept": "CSE"},
    {"name": "Dr. Anita Sharma",      "subjects": ["dbms", "database", "sql", "rdbms", "csa2003"],                "cabin": "Block C, Room 101", "email": "anita.sharma@vitbhopal.ac.in",    "available": "Mon-Wed 9AM-11AM",  "dept": "CSE"},
    {"name": "Dr. Rakesh Verma",      "subjects": ["computer networks", "networking", "cn", "tcp", "csa3001"],    "cabin": "Block A, Room 110", "email": "rakesh.verma@vitbhopal.ac.in",    "available": "Wed-Fri 3PM-5PM",   "dept": "CSE"},
    {"name": "Dr. Sunita Yadav",      "subjects": ["operating systems", "os", "unix", "linux", "csa2004"],       "cabin": "Block B, Room 215", "email": "sunita.yadav@vitbhopal.ac.in",    "available": "Mon-Fri 12PM-2PM",  "dept": "CSE"},
    {"name": "Dr. Vikas Tripathi",    "subjects": ["software engineering", "sdlc", "agile", "se", "csa3002"],    "cabin": "Block C, Room 205", "email": "vikas.tripathi@vitbhopal.ac.in",  "available": "Tue-Thu 10AM-12PM", "dept": "CSE"},
    {"name": "Dr. Neha Agrawal",      "subjects": ["web technologies", "web development", "html", "csa3003"],    "cabin": "Block A, Room 320", "email": "neha.agrawal@vitbhopal.ac.in",    "available": "Mon-Fri 9AM-10AM",  "dept": "CSE"},
    {"name": "Dr. Amit Saxena",       "subjects": ["cloud computing", "aws", "cloud", "csa4001"],                "cabin": "Block D, Room 102", "email": "amit.saxena@vitbhopal.ac.in",     "available": "Mon-Wed 2PM-4PM",   "dept": "CSE"},
    {"name": "Dr. Pooja Jain",        "subjects": ["deep learning", "neural networks", "cnn", "csa4002"],        "cabin": "Block D, Room 210", "email": "pooja.jain@vitbhopal.ac.in",      "available": "Thu-Fri 10AM-1PM",  "dept": "CSE"},
]

RESPONSES = {
    "greet":  ["Hello! Ask me: 'Who teaches AI?' or 'Cabin of Dr. Jyoti?'",
               "Hi! Type a subject or professor name to get started.",
               "Hey! I can find faculty cabin, email, and availability for you."],
    "thanks": ["You're welcome!", "Happy to help!", "Anytime!"],
    "help":   ["Try asking:\n  - 'Who teaches Python?'\n  - 'Cabin of Dr. Anita'\n  - 'Email of Dr. Rakesh'\n  - 'When is Dr. Jyoti available?'\n  - 'show all'  to list everyone"],
}

history = []

def clean(text):
    return re.sub(r"[?!.,;:']", "", text.lower().strip())

def find_faculty(query):
    results = []
    for f in FACULTY_DB:
        for s in f["subjects"]:
            if s in query:
                if f not in results:
                    results.append(f)
                break
        else:
            for part in f["name"].lower().replace("dr.", "").split():
                if len(part) > 3 and part in query:
                    if f not in results:
                        results.append(f)
                    break
    return results

def intent(query):
    if any(w in query for w in ["cabin", "room", "office", "where", "location", "block"]):
        return "cabin"
    if any(w in query for w in ["email", "mail", "contact", "@"]):
        return "email"
    if any(w in query for w in ["available", "availability", "timing", "when", "schedule", "hours"]):
        return "available"
    return "all"

def format_result(faculty_list, mode):
    lines = []
    for f in faculty_list:
        lines.append(f"\n  Name  : {f['name']}  ({f['dept']})")
        if mode == "cabin":
            lines.append(f"  Cabin : {f['cabin']}")
        elif mode == "email":
            lines.append(f"  Email : {f['email']}")
        elif mode == "available":
            lines.append(f"  Hours : {f['available']}")
        else:
            lines.append(f"  Cabin : {f['cabin']}")
            lines.append(f"  Email : {f['email']}")
            lines.append(f"  Hours : {f['available']}")
            lines.append(f"  Teach : {', '.join(f['subjects'][:3])}")
        lines.append("  " + "-" * 40)
    return "\n".join(lines)

def show_all():
    lines = [f"\n  {'#':<4}{'Name':<26}{'Subject':<22}{'Cabin'}", "  " + "-"*68]
    for i, f in enumerate(FACULTY_DB, 1):
        lines.append(f"  {i:<4}{f['name']:<26}{f['subjects'][0]:<22}{f['cabin']}")
    return "\n".join(lines)

def respond(user_input):
    q = clean(user_input)

    if any(w in q for w in ["hello", "hi", "hey", "good morning"]):
        return random.choice(RESPONSES["greet"])
    if any(w in q for w in ["thank", "thanks", "helpful"]):
        return random.choice(RESPONSES["thanks"])
    if "help" in q:
        return RESPONSES["help"][0]
    if "show all" in q or "list all" in q or "all faculty" in q:
        return show_all()
    if "history" in q:
        if not history:
            return "No history yet."
        return "\n".join(f"  [{i+1}] You: {h[0]}\n       Bot: {h[1][:60]}..." for i, h in enumerate(history))

    matches = find_faculty(q)
    if matches:
        return format_result(matches, intent(q))

    return "  Faculty not found. Try 'show all' to browse, or 'help' for usage tips."

def main():
    print("\n" + "="*52)
    print("   FACULTYBOT — VIT Bhopal Faculty Finder")
    print("   Intelligent Agent  |  CSA2001  |  Python")
    print("="*52)
    print("   Type 'help' to get started.\n")

    while True:
        try:
            user_input = input("  You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Bot: Goodbye!\n"); break

        if not user_input:
            continue
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("  Bot: Goodbye! Best of luck with your studies!\n"); break

        reply = respond(user_input)
        print(f"\n  Bot: {reply}\n")
        history.append((user_input, reply))

if __name__ == "__main__":
    main()
