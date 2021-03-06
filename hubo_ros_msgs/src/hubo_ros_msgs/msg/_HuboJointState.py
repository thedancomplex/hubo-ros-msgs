"""autogenerated by genpy from hubo_ros_msgs/HuboJointState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class HuboJointState(genpy.Message):
  _md5sum = "6cf30dce1dbcdad49065069cd06ff95d"
  _type = "hubo_ros_msgs/HuboJointState"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string name
float64 position
float64 velocity
float64 current
float64 temperature
int32 active
int32 zeroed

"""
  __slots__ = ['name','position','velocity','current','temperature','active','zeroed']
  _slot_types = ['string','float64','float64','float64','float64','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       name,position,velocity,current,temperature,active,zeroed

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HuboJointState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.name is None:
        self.name = ''
      if self.position is None:
        self.position = 0.
      if self.velocity is None:
        self.velocity = 0.
      if self.current is None:
        self.current = 0.
      if self.temperature is None:
        self.temperature = 0.
      if self.active is None:
        self.active = 0
      if self.zeroed is None:
        self.zeroed = 0
    else:
      self.name = ''
      self.position = 0.
      self.velocity = 0.
      self.current = 0.
      self.temperature = 0.
      self.active = 0
      self.zeroed = 0

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
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4d2i.pack(_x.position, _x.velocity, _x.current, _x.temperature, _x.active, _x.zeroed))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.position, _x.velocity, _x.current, _x.temperature, _x.active, _x.zeroed,) = _struct_4d2i.unpack(str[start:end])
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
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4d2i.pack(_x.position, _x.velocity, _x.current, _x.temperature, _x.active, _x.zeroed))
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
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.position, _x.velocity, _x.current, _x.temperature, _x.active, _x.zeroed,) = _struct_4d2i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4d2i = struct.Struct("<4d2i")
