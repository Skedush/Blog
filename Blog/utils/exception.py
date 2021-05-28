''' 自定义接口异常response'''
from rest_framework.views import exception_handler
from .constant import CODE_NOT_FOUND_ERROR, MSG_NOT_FOUND_ERROR, MSG_UNKNOWN_ERROR, CODE_UNKNOWN_ERROR, \
    CODE_AUTH_ERROR, MSG_AUTH_ERROR, CODE_SERVER_ERROR, MSG_SERVER_ERROR, MSG_REJECT_ERROR, CODE_REJECT_ERROR, \
    CODE_METHOD_ERROR, MSG_METHOD_ERROR, MSG_PARAMETER_ERROR, CODE_PARAMETER_ERROR


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    print('response: ', response)
    errorMessage = response.data.copy()
    if response is not None:
        response.data.clear()
        response.data['success'] = False

        if response.status_code == 404:
            try:
                response.data['message'] = MSG_NOT_FOUND_ERROR
                response.data['code'] = CODE_NOT_FOUND_ERROR
            except KeyError:
                response.data['message'] = MSG_NOT_FOUND_ERROR

        if response.status_code == 400:
            response.data['message'] = MSG_PARAMETER_ERROR
            response.data['code'] = CODE_PARAMETER_ERROR

        elif response.status_code == 401:
            response.data['message'] = MSG_AUTH_ERROR
            response.data['code'] = CODE_AUTH_ERROR

        elif response.status_code == 403:
            response.data['message'] = MSG_REJECT_ERROR
            response.data['code'] = CODE_REJECT_ERROR

        elif response.status_code == 405:
            response.data['message'] = MSG_METHOD_ERROR
            response.data['code'] = CODE_METHOD_ERROR

        elif response.status_code >= 500:
            response.data['message'] = MSG_SERVER_ERROR
            response.data['code'] = CODE_SERVER_ERROR

        response.data['data'] = errorMessage

    return response
