# Curriculum Engine

A simple curriculum engine that provides interactive coding labs with AI hints.

## Features

* Embedded labs in an iframe sandbox that runs Python code
* AI hint button provides up to 3 suggestions per lab, each limited to 150 characters
* Lab completion is recorded only after the solution passes all hidden test cases

## Usage

1. Create a new lab by adding a `Lab` object to the `CurriculumEngine`
2. Add AI hints to the lab using the `add_ai_hint` method
3. Run the lab using the `run_lab` method
4. Record completion of the lab using the `record_completion` method
