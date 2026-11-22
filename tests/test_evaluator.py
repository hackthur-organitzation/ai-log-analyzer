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


def test_check_for_uncertainty():
    diagnosis = "No se puede determinar la causa raíz con estos logs."
    expected = {"root_cause_confirmed": False}

    result = evaluate_root_cause(diagnosis, expected)

    assert result["expresses_uncertainty"] is True
    assert result["uncertainty_check_passed"] is True

def test_check_for_data_insufficient():
    diagnosis = "No se puede determinar la causa raíz. Definitivamente falta una variable de entorno."
    expected = {"root_cause_confirmed": False}

    result = evaluate_root_cause(diagnosis, expected)

    assert result["expresses_uncertainty"] is True
    assert result["uncertainty_check_passed"] is True


def test_check_variable_environment():
    diagnosis = "La causa es una variable de entorno ausente."
    expected = {"root_cause_confirmed": False}

    result = evaluate_root_cause(diagnosis, expected)

    assert result["expresses_uncertainty"] is False
    assert result["uncertainty_check_passed"] is False




#======================================================================================================



def test_confirmed_cause_skips_uncertainty_check():
    diagnosis = "La aplicación reporta que falta DATABASE_URL."
    expected = {"root_cause_confirmed": True}

    result = evaluate_root_cause(diagnosis, expected)

    assert result["root_cause_confirmed"] is True
    assert result["expresses_uncertainty"] is False
    assert result["uncertainty_check_passed"] is None

# ==============


def test_confirmed_cause_with_uncertainty_also_skips_check():
    diagnosis = "No se puede determinar la causa."
    expected = {"root_cause_confirmed": True}

    result = evaluate_root_cause(diagnosis, expected)

    assert result["expresses_uncertainty"] is True
    assert result["uncertainty_check_passed"] is None

# ==============


def test_detects_uncertainty_in_uppercase():
    diagnosis = "NO SE PUEDE DETERMINAR LA CAUSA."
    expected = {"root_cause_confirmed": False}

    result = evaluate_root_cause(diagnosis, expected)

    assert result["expresses_uncertainty"] is True
    assert result["uncertainty_check_passed"] is True

# ==============


def test_empty_diagnosis_does_not_pass():
    diagnosis = ""
    expected = {"root_cause_confirmed": False}

    result = evaluate_root_cause(diagnosis, expected)

    assert result["expresses_uncertainty"] is False
    assert result["uncertainty_check_passed"] is False

# ==============


def test_detects_insufficient_evidence():
    diagnosis = "No hay evidencia suficiente para confirmar la causa."
    expected = {"root_cause_confirmed": False}

    result = evaluate_root_cause(diagnosis, expected)

    assert result["expresses_uncertainty"] is True
    assert result["uncertainty_check_passed"] is True

# ==============



def test_detects_alternative_uncertainty_expressions():
    diagnosis = "Estos datos no permiten establecer el origen del fallo."
    expected = {"root_cause_confirmed": False}

    result = evaluate_root_cause(diagnosis, expected)

    assert result["expresses_uncertainty"] is True
    assert result["uncertainty_check_passed"] is True


