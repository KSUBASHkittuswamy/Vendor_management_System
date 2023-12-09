
import traceback
from rest_framework.response import Response
from rest_framework import status



class VendorResponse:
    
    @staticmethod
    def serializer_error(className, request, serializer, user_id=None):
        Ip = request.META['REMOTE_ADDR']
        msg = {'status': status.HTTP_400_BAD_REQUEST,'message': serializer.errors}
        print(msg,'------------serializer--error')
    
    @staticmethod
    def exception_error(className, request, e, user_id=None):
        msg={'error':str(e),'traceback':traceback.format_exc()}
        Ip = request.META['REMOTE_ADDR']
        print(msg,'-------------exception--error')
        return Response(msg,status=status.HTTP_400_BAD_REQUEST)
    
    @staticmethod
    def restricted_error(className, request, errorName, user_id=None):
        Ip = request.META['REMOTE_ADDR']
        error_message = f'{errorName} is being referenced with another instance'
        print(error_message,'-----------Restrict--Error')
        error_data = {'status': status.HTTP_400_BAD_REQUEST, 'message': error_message}
    
    @staticmethod
    def deleted_successfully(className, request, modalName, user_id=None):
        Ip = request.META['REMOTE_ADDR']
        error = {'status': status.HTTP_202_ACCEPTED,'message': f'{modalName} Deleted successfully'}
        print(error,'----------delete-------------')
    
    @staticmethod
    def created_successfully(className, request, modalName, user_id=None):
        Ip = request.META['REMOTE_ADDR']
        error = {'status': status.HTTP_202_ACCEPTED,'message': f'{modalName} Created successfully'}
        print(error, '------------create-------------')
    
    @staticmethod
    def updated_successfully(className, request, modalName, user_id=None):
        Ip = request.META['REMOTE_ADDR']
        error = {'status': status.HTTP_202_ACCEPTED,'message': f'{modalName} Updated successfully'}
        print(error, '------------create-------------')
        