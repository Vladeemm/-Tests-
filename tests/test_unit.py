# python -m pytest --tb=short -v
import pytest
from unit import get_doc_owner_name, get_all_doc_owners_names, \
    show_document_info, add_new_doc, delete_doc, documents
from unittest.mock import patch


def test_displaying_list_document_owners():
    assert get_all_doc_owners_names() != set()


def test_output_person_name_by_number():
    with patch('builtins.input', return_value='11-2'):
        assert get_doc_owner_name() == "Геннадий Покемонов"


@pytest.mark.parametrize(
    'documents',
    [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]
)
def test_check_order_output_info_document(documents):
    result = '{} "{}" "{}"'.format(documents['type'], documents['number'], documents['name'])
    assert show_document_info(documents) == result


def test_check_add_new_doc_in_shelf():
    with patch('builtins.input', side_effect=['5555 654321', 'passport', 'Вениамин Маск', '3']):
        assert add_new_doc() == '3'


def my_document(number):
    for document in documents:
        doc_number = document['number']
        if doc_number == number:
            return True
    return False


def test_check_delete_doc():
    assert my_document('11-2') == True
    with patch('builtins.input', return_value='11-2'):
        delete_doc()
        assert my_document('11-2') == False
