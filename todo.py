#!/usr/bin/env python3
"""
Simple CLI Todo Manager
"""

import os
import json
from pathlib import Path


class TodoManager:
    """Manages todos with file persistence"""
    
    def __init__(self, filepath="todos.json"):
        self.filepath = filepath
        self.todos = self._load_todos()
    
    def _load_todos(self):
        """Load todos from file"""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def _save_todos(self):
        """Save todos to file"""
        with open(self.filepath, 'w') as f:
            json.dump(self.todos, f, indent=2)


def main():
    """Main entry point"""
    manager = TodoManager()
    
    print("Welcome to CLI Todo Manager!")
    print("Commands: add, list, complete, delete, exit")
    
    while True:
        command = input("\n> ").strip().lower()
        
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "help":
            print("Commands: add, list, complete, delete, exit")
        else:
            print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
