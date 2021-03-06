"""autogenerated by genpy from hubo_ros_msgs/HuboState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import hubo_ros_msgs.msg

class HuboState(genpy.Message):
  _md5sum = "5245526d8ea9b726511504ca60eb9de2"
  _type = "hubo_ros_msgs/HuboState"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """HuboJointState[] joints
HuboHand left_hand
HuboHand right_hand
HuboIMU imu
HuboIMU left_foot
HuboIMU right_foot
HuboFT left_wrist
HuboFT right_wrist
HuboFT left_ankle
HuboFT right_ankle

================================================================================
MSG: hubo_ros_msgs/HuboJointState
string name
float64 position
float64 velocity
float64 current
float64 temperature
int32 active
int32 zeroed

================================================================================
MSG: hubo_ros_msgs/HuboHand
float64 thumb
float64 index
float64 middle
float64 ring
float64 pinky

================================================================================
MSG: hubo_ros_msgs/HuboIMU
float64 x_acceleration
float64 y_acceleration
float64 z_acceleration
float64 x_rotation
float64 y_rotation

================================================================================
MSG: hubo_ros_msgs/HuboFT
float64 Mx
float64 My
float64 Fz

"""
  __slots__ = ['joints','left_hand','right_hand','imu','left_foot','right_foot','left_wrist','right_wrist','left_ankle','right_ankle']
  _slot_types = ['hubo_ros_msgs/HuboJointState[]','hubo_ros_msgs/HuboHand','hubo_ros_msgs/HuboHand','hubo_ros_msgs/HuboIMU','hubo_ros_msgs/HuboIMU','hubo_ros_msgs/HuboIMU','hubo_ros_msgs/HuboFT','hubo_ros_msgs/HuboFT','hubo_ros_msgs/HuboFT','hubo_ros_msgs/HuboFT']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       joints,left_hand,right_hand,imu,left_foot,right_foot,left_wrist,right_wrist,left_ankle,right_ankle

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HuboState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.joints is None:
        self.joints = []
      if self.left_hand is None:
        self.left_hand = hubo_ros_msgs.msg.HuboHand()
      if self.right_hand is None:
        self.right_hand = hubo_ros_msgs.msg.HuboHand()
      if self.imu is None:
        self.imu = hubo_ros_msgs.msg.HuboIMU()
      if self.left_foot is None:
        self.left_foot = hubo_ros_msgs.msg.HuboIMU()
      if self.right_foot is None:
        self.right_foot = hubo_ros_msgs.msg.HuboIMU()
      if self.left_wrist is None:
        self.left_wrist = hubo_ros_msgs.msg.HuboFT()
      if self.right_wrist is None:
        self.right_wrist = hubo_ros_msgs.msg.HuboFT()
      if self.left_ankle is None:
        self.left_ankle = hubo_ros_msgs.msg.HuboFT()
      if self.right_ankle is None:
        self.right_ankle = hubo_ros_msgs.msg.HuboFT()
    else:
      self.joints = []
      self.left_hand = hubo_ros_msgs.msg.HuboHand()
      self.right_hand = hubo_ros_msgs.msg.HuboHand()
      self.imu = hubo_ros_msgs.msg.HuboIMU()
      self.left_foot = hubo_ros_msgs.msg.HuboIMU()
      self.right_foot = hubo_ros_msgs.msg.HuboIMU()
      self.left_wrist = hubo_ros_msgs.msg.HuboFT()
      self.right_wrist = hubo_ros_msgs.msg.HuboFT()
      self.left_ankle = hubo_ros_msgs.msg.HuboFT()
      self.right_ankle = hubo_ros_msgs.msg.HuboFT()

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
        buff.write(_struct_4d2i.pack(_x.position, _x.velocity, _x.current, _x.temperature, _x.active, _x.zeroed))
      _x = self
      buff.write(_struct_37d.pack(_x.left_hand.thumb, _x.left_hand.index, _x.left_hand.middle, _x.left_hand.ring, _x.left_hand.pinky, _x.right_hand.thumb, _x.right_hand.index, _x.right_hand.middle, _x.right_hand.ring, _x.right_hand.pinky, _x.imu.x_acceleration, _x.imu.y_acceleration, _x.imu.z_acceleration, _x.imu.x_rotation, _x.imu.y_rotation, _x.left_foot.x_acceleration, _x.left_foot.y_acceleration, _x.left_foot.z_acceleration, _x.left_foot.x_rotation, _x.left_foot.y_rotation, _x.right_foot.x_acceleration, _x.right_foot.y_acceleration, _x.right_foot.z_acceleration, _x.right_foot.x_rotation, _x.right_foot.y_rotation, _x.left_wrist.Mx, _x.left_wrist.My, _x.left_wrist.Fz, _x.right_wrist.Mx, _x.right_wrist.My, _x.right_wrist.Fz, _x.left_ankle.Mx, _x.left_ankle.My, _x.left_ankle.Fz, _x.right_ankle.Mx, _x.right_ankle.My, _x.right_ankle.Fz))
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
      if self.left_hand is None:
        self.left_hand = hubo_ros_msgs.msg.HuboHand()
      if self.right_hand is None:
        self.right_hand = hubo_ros_msgs.msg.HuboHand()
      if self.imu is None:
        self.imu = hubo_ros_msgs.msg.HuboIMU()
      if self.left_foot is None:
        self.left_foot = hubo_ros_msgs.msg.HuboIMU()
      if self.right_foot is None:
        self.right_foot = hubo_ros_msgs.msg.HuboIMU()
      if self.left_wrist is None:
        self.left_wrist = hubo_ros_msgs.msg.HuboFT()
      if self.right_wrist is None:
        self.right_wrist = hubo_ros_msgs.msg.HuboFT()
      if self.left_ankle is None:
        self.left_ankle = hubo_ros_msgs.msg.HuboFT()
      if self.right_ankle is None:
        self.right_ankle = hubo_ros_msgs.msg.HuboFT()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.joints = []
      for i in range(0, length):
        val1 = hubo_ros_msgs.msg.HuboJointState()
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
        end += 40
        (_x.position, _x.velocity, _x.current, _x.temperature, _x.active, _x.zeroed,) = _struct_4d2i.unpack(str[start:end])
        self.joints.append(val1)
      _x = self
      start = end
      end += 296
      (_x.left_hand.thumb, _x.left_hand.index, _x.left_hand.middle, _x.left_hand.ring, _x.left_hand.pinky, _x.right_hand.thumb, _x.right_hand.index, _x.right_hand.middle, _x.right_hand.ring, _x.right_hand.pinky, _x.imu.x_acceleration, _x.imu.y_acceleration, _x.imu.z_acceleration, _x.imu.x_rotation, _x.imu.y_rotation, _x.left_foot.x_acceleration, _x.left_foot.y_acceleration, _x.left_foot.z_acceleration, _x.left_foot.x_rotation, _x.left_foot.y_rotation, _x.right_foot.x_acceleration, _x.right_foot.y_acceleration, _x.right_foot.z_acceleration, _x.right_foot.x_rotation, _x.right_foot.y_rotation, _x.left_wrist.Mx, _x.left_wrist.My, _x.left_wrist.Fz, _x.right_wrist.Mx, _x.right_wrist.My, _x.right_wrist.Fz, _x.left_ankle.Mx, _x.left_ankle.My, _x.left_ankle.Fz, _x.right_ankle.Mx, _x.right_ankle.My, _x.right_ankle.Fz,) = _struct_37d.unpack(str[start:end])
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
        buff.write(_struct_4d2i.pack(_x.position, _x.velocity, _x.current, _x.temperature, _x.active, _x.zeroed))
      _x = self
      buff.write(_struct_37d.pack(_x.left_hand.thumb, _x.left_hand.index, _x.left_hand.middle, _x.left_hand.ring, _x.left_hand.pinky, _x.right_hand.thumb, _x.right_hand.index, _x.right_hand.middle, _x.right_hand.ring, _x.right_hand.pinky, _x.imu.x_acceleration, _x.imu.y_acceleration, _x.imu.z_acceleration, _x.imu.x_rotation, _x.imu.y_rotation, _x.left_foot.x_acceleration, _x.left_foot.y_acceleration, _x.left_foot.z_acceleration, _x.left_foot.x_rotation, _x.left_foot.y_rotation, _x.right_foot.x_acceleration, _x.right_foot.y_acceleration, _x.right_foot.z_acceleration, _x.right_foot.x_rotation, _x.right_foot.y_rotation, _x.left_wrist.Mx, _x.left_wrist.My, _x.left_wrist.Fz, _x.right_wrist.Mx, _x.right_wrist.My, _x.right_wrist.Fz, _x.left_ankle.Mx, _x.left_ankle.My, _x.left_ankle.Fz, _x.right_ankle.Mx, _x.right_ankle.My, _x.right_ankle.Fz))
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
      if self.left_hand is None:
        self.left_hand = hubo_ros_msgs.msg.HuboHand()
      if self.right_hand is None:
        self.right_hand = hubo_ros_msgs.msg.HuboHand()
      if self.imu is None:
        self.imu = hubo_ros_msgs.msg.HuboIMU()
      if self.left_foot is None:
        self.left_foot = hubo_ros_msgs.msg.HuboIMU()
      if self.right_foot is None:
        self.right_foot = hubo_ros_msgs.msg.HuboIMU()
      if self.left_wrist is None:
        self.left_wrist = hubo_ros_msgs.msg.HuboFT()
      if self.right_wrist is None:
        self.right_wrist = hubo_ros_msgs.msg.HuboFT()
      if self.left_ankle is None:
        self.left_ankle = hubo_ros_msgs.msg.HuboFT()
      if self.right_ankle is None:
        self.right_ankle = hubo_ros_msgs.msg.HuboFT()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.joints = []
      for i in range(0, length):
        val1 = hubo_ros_msgs.msg.HuboJointState()
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
        end += 40
        (_x.position, _x.velocity, _x.current, _x.temperature, _x.active, _x.zeroed,) = _struct_4d2i.unpack(str[start:end])
        self.joints.append(val1)
      _x = self
      start = end
      end += 296
      (_x.left_hand.thumb, _x.left_hand.index, _x.left_hand.middle, _x.left_hand.ring, _x.left_hand.pinky, _x.right_hand.thumb, _x.right_hand.index, _x.right_hand.middle, _x.right_hand.ring, _x.right_hand.pinky, _x.imu.x_acceleration, _x.imu.y_acceleration, _x.imu.z_acceleration, _x.imu.x_rotation, _x.imu.y_rotation, _x.left_foot.x_acceleration, _x.left_foot.y_acceleration, _x.left_foot.z_acceleration, _x.left_foot.x_rotation, _x.left_foot.y_rotation, _x.right_foot.x_acceleration, _x.right_foot.y_acceleration, _x.right_foot.z_acceleration, _x.right_foot.x_rotation, _x.right_foot.y_rotation, _x.left_wrist.Mx, _x.left_wrist.My, _x.left_wrist.Fz, _x.right_wrist.Mx, _x.right_wrist.My, _x.right_wrist.Fz, _x.left_ankle.Mx, _x.left_ankle.My, _x.left_ankle.Fz, _x.right_ankle.Mx, _x.right_ankle.My, _x.right_ankle.Fz,) = _struct_37d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4d2i = struct.Struct("<4d2i")
_struct_37d = struct.Struct("<37d")
