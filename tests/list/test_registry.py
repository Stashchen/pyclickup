from pyclickup.services.cache import ClientListsRegistry


def test_client_list_registry__new_classes__in_registry(
    client_list_1, client_list_2
):
    assert ClientListsRegistry._storage == {
        "ClientListOne": client_list_1,
        "ClientListTwo": client_list_2
    }
    
