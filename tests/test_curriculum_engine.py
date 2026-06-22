import pytest
from curriculum_engine import CurriculumEngine, Module
import os

def test_load_modules(tmp_path):
    # Create a temporary directory with a Markdown file
    content_dir = tmp_path / "content" / "modules"
    content_dir.mkdir(parents=True)
    with open(content_dir / "module1.md", "w") as f:
        f.write("AI-Tool-ID: tool1\nAssessment-ID: assess1\n# Module 1")
    engine = CurriculumEngine(str(content_dir))
    engine.load_modules()
    assert len(engine.modules) > 0

def test_parse_metadata():
    markdown = "AI-Tool-ID: tool1\nAssessment-ID: assess1\n# Module 1"
    ai_tool_id, assessment_id = CurriculumEngine.parse_metadata(markdown)
    assert ai_tool_id == "tool1"
    assert assessment_id == "assess1"

def test_get_module(tmp_path):
    # Create a temporary directory with a Markdown file
    content_dir = tmp_path / "content" / "modules"
    content_dir.mkdir(parents=True)
    with open(content_dir / "module1.md", "w") as f:
        f.write("AI-Tool-ID: tool1\nAssessment-ID: assess1\n# Module 1")
    engine = CurriculumEngine(str(content_dir))
    engine.load_modules()
    module = engine.get_module("module1")
    assert module is not None
    assert module.id == "module1"

def test_publish_module(tmp_path):
    # Create a temporary directory with a Markdown file
    content_dir = tmp_path / "content" / "modules"
    content_dir.mkdir(parents=True)
    with open(content_dir / "module1.md", "w") as f:
        f.write("AI-Tool-ID: tool1\nAssessment-ID: assess1\n# Module 1")
    engine = CurriculumEngine(str(content_dir))
    engine.load_modules()
    module_id = "module1"
    result = engine.publish_module(module_id)
    assert result is True

def test_publish_non_existent_module(tmp_path):
    # Create a temporary directory with a Markdown file
    content_dir = tmp_path / "content" / "modules"
    content_dir.mkdir(parents=True)
    with open(content_dir / "module1.md", "w") as f:
        f.write("AI-Tool-ID: tool1\nAssessment-ID: assess1\n# Module 1")
    engine = CurriculumEngine(str(content_dir))
    engine.load_modules()
    module_id = "non_existent_module"
    result = engine.publish_module(module_id)
    assert result is False
