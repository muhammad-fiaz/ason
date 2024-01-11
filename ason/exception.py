# exception.py
class AsonException(Exception):
    pass

class SetOperationException(AsonException):
    pass

class GetOperationException(AsonException):
    pass

class ProcessPlaceholderOperationException(AsonException):
    pass

class ReplaceOperationException(AsonException):
    pass

class AppendOperationException(AsonException):
    pass

class DumpsOperationException(AsonException):
    pass

class LoadsOperationException(AsonException):
    pass

class GetItemOperationException(AsonException):
    pass

class SetItemOperationException(AsonException):
    pass
