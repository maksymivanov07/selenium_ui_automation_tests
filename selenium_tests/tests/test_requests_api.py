from http import HTTPStatus

from api_collections.user_collection import ReqRes


def test_get_user_by_id():
    """
    Make request on endpoint and get user if exist
    :return: Return 200 ok if user exist
    """
    response = ReqRes().get_user_by_id(1)
    assert response.status_code == HTTPStatus.OK


def test_register_user():
    """
      note: This API pass only one defined user.
      Make request and post new user
      :return: Return 200 ok all information correct
    """
    response = ReqRes().post_create_user()
    assert response.status_code == HTTPStatus.OK


def test_delete_user():
    """
       note: Make request on endpoint by user id and delete it if exist
       :return: Return error 204
     """
    response = ReqRes().delete(2)
    assert response.status_code == HTTPStatus.NO_CONTENT
