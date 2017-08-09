#
#  api_exceptions.py
#  ~~~~~~~~~~~~~~~~~
#

##
#  @file api_exceptions.py
#  @author Andrew Milligan
#
#  Exception classes for Solaflect API interaction

## @class APIException
#
#  Abstract class for API exceptions.
#
class APIException(Exception):
  msg = ''
  code = ''
  def __init__(self):
    pass

## @class RequestError class.
#
#  This exception class is raised when there is an exception thrown by
#  the underlying Requests module. The RequestError object saves the
#  error object created by the Requests module.
#
class RequestError(APIException):
  error = ''
  def __init__(self, error, url):
    cls = str(type(self).__name__)
    self.error = error
    self.msg = cls + " requests error for URL '" + str(url) + \
            "': " + str(error)
    Exception.__init__(self, self.msg)
    self.code = 1

## @class MaintenanceError
#
#  This exception type is thrown when an API request is attempted
#  during the API server's maintenance window.
#
class MaintenanceError(APIException):
  def __init__(self):
    cls = str(type(self).__name__)
    self.msg = cls + ": server maintenance window"
    Exception.__init__(self, self.msg)
    self.code = 2

## @class FileError
#
#  This exception type is thrown when there was a problem reading a file.
#
class FileError(APIException):
  filename = ''
  def __init__(self, filename):
    cls = str(type(self).__name__)
    self.filename = filename
    self.msg = cls + ":error reading file '" + self.filename + "'"
    Exception.__init__(self, self.msg)
    self.code = 3

## @class APIValueError
#
#  This exception type is thrown when an API request cannot be
#  interpreted in the expected way.
#
class APIValueError(APIException):
  err = ''
  def __init__(self, err):
    cls = str(type(self).__name__)
    self.err = err
    self.msg = cls + ": error decoding response: " + str(err)
    Exception.__init__(self, self.msg)
    self.code = 4

## @class CacheError
#
#  This exception type is thrown when the API Bot's cache throws an
#  error. The original error is saved.
#
class CacheError(APIException):
  err = ''
  def __init__(self, err):
    cls = str(type(self).__name__)
    self.err = err
    self.msg = cls + ": thrown by cache: " + str(err)
    Exception.__init__(self, self.msg)
    self.code = 5
