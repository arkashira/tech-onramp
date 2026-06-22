import os
import json
from dataclasses import dataclass
from typing import List

@dataclass
class Module:
    id: str
    markdown: str
    ai_tool_id: str
    assessment_id: str

class CurriculumEngine:
    def __init__(self, content_dir):
        self.content_dir = content_dir
        self.modules = []

    def load_modules(self):
        if not os.path.exists(self.content_dir):
            return  # Return if the directory does not exist
        for filename in os.listdir(self.content_dir):
            if filename.endswith(".md"):
                with open(os.path.join(self.content_dir, filename), "r") as f:
                    markdown = f.read()
                module_id = os.path.splitext(filename)[0]
                ai_tool_id, assessment_id = self.parse_metadata(markdown)
                self.modules.append(Module(module_id, markdown, ai_tool_id, assessment_id))

    @staticmethod
    def parse_metadata(markdown):
        lines = markdown.splitlines()
        ai_tool_id = None
        assessment_id = None
        for line in lines:
            if line.startswith("AI-Tool-ID:"):
                ai_tool_id = line.split(":")[1].strip()
            elif line.startswith("Assessment-ID:"):
                assessment_id = line.split(":")[1].strip()
        return ai_tool_id, assessment_id

    def get_module(self, module_id):
        for module in self.modules:
            if module.id == module_id:
                return module
        return None

    def publish_module(self, module_id):
        module = self.get_module(module_id)
        if module:
            # Simulate publishing by printing the module's markdown
            print(module.markdown)
            return True
        return False
