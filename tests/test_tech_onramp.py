import json
from tech_onramp import process_code_snippet, CodeSnippet

def test_process_code_snippet_def():
    user_id = "test_user"
    code = "def example(): pass"
    expected_suggestions = ["Consider adding docstrings.", "Check for unused variables."]
    result = process_code_snippet(user_id, code)
    assert isinstance(result, CodeSnippet)
    assert result.code == code
    assert result.suggestions == expected_suggestions

def test_process_code_snippet_for():
    user_id = "test_user"
    code = "for i in range(10): pass"
    expected_suggestions = ["Ensure loop termination conditions are correct.", "Avoid modifying loop variables inside the loop."]
    result = process_code_snippet(user_id, code)
    assert isinstance(result, CodeSnippet)
    assert result.code == code
    assert result.suggestions == expected_suggestions

def test_process_code_snippet_no_keywords():
    user_id = "test_user"
    code = "print('Hello, world!')"
    expected_suggestions = ["Your code looks good!"]
    result = process_code_snippet(user_id, code)
    assert isinstance(result, CodeSnippet)
    assert result.code == code
    assert result.suggestions == expected_suggestions
