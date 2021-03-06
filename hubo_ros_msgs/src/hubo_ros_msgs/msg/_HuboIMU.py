"""autogenerated by genpy from hubo_ros_msgs/HuboIMU.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class HuboIMU(genpy.Message):
  _md5sum = "9c14264f3bcdc765b4eeefc475d9111c"
  _type = "hubo_ros_msgs/HuboIMU"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 x_acceleration
float64 y_acceleration
float64 z_acceleration
float64 x_rotation
float64 y_rotation

"""
  __slots__ = ['x_acceleration','y_acceleration','z_acceleration','x_rotation','y_rotation']
  _slot_types = ['float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x_acceleration,y_acceleration,z_acceleration,x_rotation,y_rotation

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HuboIMU, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x_acceleration is None:
        self.x_acceleration = 0.
      if self.y_acceleration is None:
        self.y_acceleration = 0.
      if self.z_acceleration is None:
        self.z_acceleration = 0.
      if self.x_rotation is None:
        self.x_rotation = 0.
      if self.y_rotation is None:
        self.y_rotation = 0.
    else:
      self.x_acceleration = 0.
      self.y_acceleration = 0.
      self.z_acceleration = 0.
      self.x_rotation = 0.
      self.y_rotation = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_5d.pack(_x.x_acceleration, _x.y_acceleration, _x.z_acceleration, _x.x_rotation, _x.y_rotation))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 40
      (_x.x_acceleration, _x.y_acceleration, _x.z_acceleration, _x.x_rotation, _x.y_rotation,) = _struct_5d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_5d.pack(_x.x_acceleration, _x.y_acceleration, _x.z_acceleration, _x.x_rotation, _x.y_rotation))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 40
      (_x.x_acceleration, _x.y_acceleration, _x.z_acceleration, _x.x_rotation, _x.y_rotation,) = _struct_5d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_5d = struct.Struct("<5d")
