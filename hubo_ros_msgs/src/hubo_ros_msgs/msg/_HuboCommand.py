"""autogenerated by genpy from hubo_ros_msgs/HuboCommand.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import hubo_ros_msgs.msg

class HuboCommand(genpy.Message):
  _md5sum = "e1b182ddb50fa4986084202886606609"
  _type = "hubo_ros_msgs/HuboCommand"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """HuboJointCommand[] joints
int32 num_joints

================================================================================
MSG: hubo_ros_msgs/HuboJointCommand
string name
float64 position
float64 velocity

"""
  __slots__ = ['joints','num_joints']
  _slot_types = ['hubo_ros_msgs/HuboJointCommand[]','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       joints,num_joints

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HuboCommand, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.joints is None:
        self.joints = []
      if self.num_joints is None:
        self.num_joints = 0
    else:
      self.joints = []
      self.num_joints = 0

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
      length = len(self.joints)
      buff.write(_struct_I.pack(length))
      for val1 in self.joints:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_2d.pack(_x.position, _x.velocity))
      buff.write(_struct_i.pack(self.num_joints))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.joints is None:
        self.joints = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.joints = []
      for i in range(0, length):
        val1 = hubo_ros_msgs.msg.HuboJointCommand()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        _x = val1
        start = end
        end += 16
        (_x.position, _x.velocity,) = _struct_2d.unpack(str[start:end])
        self.joints.append(val1)
      start = end
      end += 4
      (self.num_joints,) = _struct_i.unpack(str[start:end])
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
      length = len(self.joints)
      buff.write(_struct_I.pack(length))
      for val1 in self.joints:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_2d.pack(_x.position, _x.velocity))
      buff.write(_struct_i.pack(self.num_joints))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.joints is None:
        self.joints = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.joints = []
      for i in range(0, length):
        val1 = hubo_ros_msgs.msg.HuboJointCommand()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        _x = val1
        start = end
        end += 16
        (_x.position, _x.velocity,) = _struct_2d.unpack(str[start:end])
        self.joints.append(val1)
      start = end
      end += 4
      (self.num_joints,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2d = struct.Struct("<2d")
_struct_i = struct.Struct("<i")