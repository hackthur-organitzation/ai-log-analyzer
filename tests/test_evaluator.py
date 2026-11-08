from evaluate import evaluate_root_cause


def test_detects_uncertainty():
    diagnosis = "No se puede determinar la causa raiz con estos logs."
    expected = {"root_cause_confirmed": False}

    result = evaluate_root_cause(diagnosis, expected)

    assert result["expresses_uncertainty"] is True
    assert result["uncertainty_check_passed"] is True

def test_does_not_detect_uncertainty():
    diagnosis = "La causa raíz es un error del Dockerfile."
    expected = {"root_cause_confirmed": False}

    result = evaluate_root_cause(diagnosis, expected)

    assert result["expresses_uncertainty"] is False
    assert result["uncertainty_check_passed"] is False
