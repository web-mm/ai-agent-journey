"""
Python Crash Course for C#/JavaScript Developers
Run this file, read the comments, understand the differences
"""

# ============================================
# 1. VARIABLES (No types needed!)
# ============================================
# C#:  string name = "Manish";
# JS:  const name = "Manish";
# Python:
name = "Manish"
age = 30
is_learning = True  # not 'true' like JS

print(f"Hello, {name}!")  # f-strings = template literals

name = "Alice"  # variables are mutable by default
print(f"Hello, {name}!")


# ============================================
# 2. LISTS (like arrays)
# ============================================
# C#:  List<string> tools = new List<string>{"Python", "LLM"};
# JS:  const tools = ["Python", "LLM"];
# Python:
tools = ["Python", "LLM", "LangChain"]
tools.append("RAG")           # like .Add() in C# or .push() in JS
first = tools[0]              # same as C#/JS
last = tools[-1]              # Python trick: negative index!
subset = tools[1:3]           # slicing: ["LLM", "LangChain"]

print(f"Tools: {tools}")
print(f"First: {first}, Last: {last}")
print(f"Subset: {subset}")


# ============================================
# 3. DICTIONARIES (like objects/Dictionary)
# ============================================
# C#:  var person = new Dictionary<string, object>();
# JS:  const person = { name: "Manish", role: "engineer" };
# Python:
person = {
    "name": "Manish",
    "role": "engineer",
    "learning": ["AI", "Python"]
}
print(person["name"])              # access by key
person["goal"] = "AI Engineer"     # add new key
print(f"Person: {person}")


# ============================================
# 4. FUNCTIONS
# ============================================
# C#:  public string Greet(string name) { return $"Hello {name}"; }
# JS:  const greet = (name) => `Hello ${name}`;
# Python:
def greet(name):
    return f"Hello {name}"

# Default parameters
def greet_with_title(name, title="Mr"):
    return f"Hello {title}. {name}"

print(greet("Manish"))
print(greet_with_title("Manish", "Dr"))


# ============================================
# 5. LOOPS
# ============================================
# Indentation matters! No braces {}
for tool in tools:
    print(f"Learning: {tool}")

# With index
for i, tool in enumerate(tools):
    print(f"{i}: {tool}")

# List comprehension (Python superpower!)
# C#:  tools.Select(t => t.ToUpper()).ToList()
# JS:  tools.map(t => t.toUpperCase())
upper_tools = [t.upper() for t in tools]
print(f"Upper: {upper_tools}")


# ============================================
# 6. CLASSES
# ============================================
class Agent:
    def __init__(self, name, model):    # constructor
        self.name = name                # self = this
        self.model = model

    def respond(self, question):
        return f"{self.name} thinks about: {question}"

agent = Agent("MyBot", "gpt-4o-mini")
print(agent.respond("What is AI?"))


# ============================================
# 7. ERROR HANDLING
# ============================================
# C#:  try { } catch (Exception e) { }
# JS:  try { } catch (e) { }
# Python:
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("This always runs")


# ============================================
# 8. KEY DIFFERENCES TO REMEMBER
# ============================================
print("\n=== KEY DIFFERENCES ===")
print("No semicolons ;")
print("No braces {} → use indentation (4 spaces)")
print("No var/let/const → just variable_name = value")
print("snake_case not camelCase")
print("self not this")
print("__init__ not constructor")
print("None not null")
print("True/False not true/false (capital)")
print("print() not Console.WriteLine() or console.log()")
print("len(list) not list.Length or list.length")

print("\n✅ You now know enough Python to start!")