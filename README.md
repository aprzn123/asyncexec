# Async Exec

This is a project to facilitate the use of multithreading by adding listeners and a simple asynchronous execute method.

## Installation

Run this to install:

```python
pip install helloworld
```

## Usage

```python
import asyncexec as ae

def async_function(arg1, arg2, arg3):
    . . .

# Execute function asynchronously
startThread(async_function, args=(1, 2, 3), daemon=False)

condition = false

# Create a listener which asynchronously runs a function
# when a condition is true
startListenerThread(lambda: condition, async_function, args=(1, 2, 3), daemon=false)
```
