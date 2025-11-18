import pytest
def test_immerWahr():
    """ assert prüft den Aussdruck auf Wahrheitswert = True """
    assert True

def test_sample():
    """ Rechnungsbeispiel für eine Summe """
    assert 1 + 1 == 2

def test_another_sample():
    """ Beispiel für String-Operation """
    assert "hello".upper() == "HELLO"
    
def test_list_length():
    """ Beispiel für Datentyp Liste und Längenbestimmung """
    sample_list = [1, 2, 3, 4, 5]
    assert len(sample_list) == len(sample_list)

from quizzSchweiz import anzahlPassstrassen, passVonNach
def test_anzahlPassstrassen():
    assert anzahlPassstrassen() > 0  # Assuming there is at least one pass in the database

def test_passVonNach():
    assert passVonNach('Andermatt', 'Disentis') == 'Oberalppass'  # Example
