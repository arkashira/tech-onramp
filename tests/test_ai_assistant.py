from ai_assistant import AIAssistant, CodeSnippet

def test_get_code_suggestions():
    assistant = AIAssistant()
    code_snippet = CodeSnippet("example_function", "python")
    suggestions = assistant.get_code_suggestions(code_snippet)
    assert len(suggestions) == 2
    assert suggestions[0].startswith("def example_function():")
    assert suggestions[1] == "    pass  # Replace with your code"

def test_log_ai_interaction():
    assistant = AIAssistant()
    code_snippet = CodeSnippet("example_function", "python")
    suggestions = ["def example_function():", "    pass  # Replace with your code"]
    assistant.log_ai_interaction(code_snippet, suggestions)
    interactions = assistant.get_ai_interactions()
    assert len(interactions) == 1
    assert interactions[0]["code_snippet"] == "example_function"
    assert interactions[0]["language"] == "python"
    assert interactions[0]["suggestions"] == suggestions

def test_get_ai_interactions():
    assistant = AIAssistant()
    code_snippet1 = CodeSnippet("example_function1", "python")
    suggestions1 = ["def example_function1():", "    pass  # Replace with your code"]
    assistant.log_ai_interaction(code_snippet1, suggestions1)
    code_snippet2 = CodeSnippet("example_function2", "python")
    suggestions2 = ["def example_function2():", "    pass  # Replace with your code"]
    assistant.log_ai_interaction(code_snippet2, suggestions2)
    interactions = assistant.get_ai_interactions()
    assert len(interactions) == 2
    assert interactions[0]["code_snippet"] == "example_function1"
    assert interactions[1]["code_snippet"] == "example_function2"
