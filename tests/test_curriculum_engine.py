from curriculum_engine import CurriculumEngine, Lab, AIHint

def test_add_lab():
    engine = CurriculumEngine()
    lab = Lab(1, "print('Hello World')", ["assert True"])
    engine.add_lab(lab)
    assert len(engine.labs) == 1

def test_add_ai_hint():
    engine = CurriculumEngine()
    lab = Lab(1, "print('Hello World')", ["assert True"])
    engine.add_lab(lab)
    hint = AIHint("Use print function")
    engine.add_ai_hint(lab.id, hint)
    assert len(engine.get_ai_hints(lab.id)) == 1

def test_get_ai_hints():
    engine = CurriculumEngine()
    lab = Lab(1, "print('Hello World')", ["assert True"])
    engine.add_lab(lab)
    hint1 = AIHint("Use print function")
    hint2 = AIHint("Use string formatting")
    engine.add_ai_hint(lab.id, hint1)
    engine.add_ai_hint(lab.id, hint2)
    assert len(engine.get_ai_hints(lab.id)) == 2

def test_run_lab():
    engine = CurriculumEngine()
    lab = Lab(1, "print('Hello World')", ["assert True"])
    engine.add_lab(lab)
    assert engine.run_lab(lab.id, lab.code) == True

def test_record_completion():
    engine = CurriculumEngine()
    lab = Lab(1, "print('Hello World')", ["assert True"])
    engine.add_lab(lab)
    assert engine.record_completion(lab.id) == True

def test_record_completion_failure():
    engine = CurriculumEngine()
    lab = Lab(1, "print('Hello World')", ["assert False"])
    engine.add_lab(lab)
    assert engine.record_completion(lab.id) == False
