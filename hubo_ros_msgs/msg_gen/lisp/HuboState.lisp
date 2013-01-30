; Auto-generated. Do not edit!


(cl:in-package hubo_ros_msgs-msg)


;//! \htmlinclude HuboState.msg.html

(cl:defclass <HuboState> (roslisp-msg-protocol:ros-message)
  ((joints
    :reader joints
    :initarg :joints
    :type (cl:vector hubo_ros_msgs-msg:HuboJointState)
   :initform (cl:make-array 0 :element-type 'hubo_ros_msgs-msg:HuboJointState :initial-element (cl:make-instance 'hubo_ros_msgs-msg:HuboJointState)))
   (left_hand
    :reader left_hand
    :initarg :left_hand
    :type hubo_ros_msgs-msg:HuboHand
    :initform (cl:make-instance 'hubo_ros_msgs-msg:HuboHand))
   (right_hand
    :reader right_hand
    :initarg :right_hand
    :type hubo_ros_msgs-msg:HuboHand
    :initform (cl:make-instance 'hubo_ros_msgs-msg:HuboHand))
   (imu
    :reader imu
    :initarg :imu
    :type hubo_ros_msgs-msg:HuboIMU
    :initform (cl:make-instance 'hubo_ros_msgs-msg:HuboIMU))
   (left_foot
    :reader left_foot
    :initarg :left_foot
    :type hubo_ros_msgs-msg:HuboIMU
    :initform (cl:make-instance 'hubo_ros_msgs-msg:HuboIMU))
   (right_foot
    :reader right_foot
    :initarg :right_foot
    :type hubo_ros_msgs-msg:HuboIMU
    :initform (cl:make-instance 'hubo_ros_msgs-msg:HuboIMU))
   (left_wrist
    :reader left_wrist
    :initarg :left_wrist
    :type hubo_ros_msgs-msg:HuboFT
    :initform (cl:make-instance 'hubo_ros_msgs-msg:HuboFT))
   (right_wrist
    :reader right_wrist
    :initarg :right_wrist
    :type hubo_ros_msgs-msg:HuboFT
    :initform (cl:make-instance 'hubo_ros_msgs-msg:HuboFT))
   (left_ankle
    :reader left_ankle
    :initarg :left_ankle
    :type hubo_ros_msgs-msg:HuboFT
    :initform (cl:make-instance 'hubo_ros_msgs-msg:HuboFT))
   (right_ankle
    :reader right_ankle
    :initarg :right_ankle
    :type hubo_ros_msgs-msg:HuboFT
    :initform (cl:make-instance 'hubo_ros_msgs-msg:HuboFT)))
)

(cl:defclass HuboState (<HuboState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <HuboState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'HuboState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hubo_ros_msgs-msg:<HuboState> is deprecated: use hubo_ros_msgs-msg:HuboState instead.")))

(cl:ensure-generic-function 'joints-val :lambda-list '(m))
(cl:defmethod joints-val ((m <HuboState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hubo_ros_msgs-msg:joints-val is deprecated.  Use hubo_ros_msgs-msg:joints instead.")
  (joints m))

(cl:ensure-generic-function 'left_hand-val :lambda-list '(m))
(cl:defmethod left_hand-val ((m <HuboState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hubo_ros_msgs-msg:left_hand-val is deprecated.  Use hubo_ros_msgs-msg:left_hand instead.")
  (left_hand m))

(cl:ensure-generic-function 'right_hand-val :lambda-list '(m))
(cl:defmethod right_hand-val ((m <HuboState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hubo_ros_msgs-msg:right_hand-val is deprecated.  Use hubo_ros_msgs-msg:right_hand instead.")
  (right_hand m))

(cl:ensure-generic-function 'imu-val :lambda-list '(m))
(cl:defmethod imu-val ((m <HuboState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hubo_ros_msgs-msg:imu-val is deprecated.  Use hubo_ros_msgs-msg:imu instead.")
  (imu m))

(cl:ensure-generic-function 'left_foot-val :lambda-list '(m))
(cl:defmethod left_foot-val ((m <HuboState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hubo_ros_msgs-msg:left_foot-val is deprecated.  Use hubo_ros_msgs-msg:left_foot instead.")
  (left_foot m))

(cl:ensure-generic-function 'right_foot-val :lambda-list '(m))
(cl:defmethod right_foot-val ((m <HuboState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hubo_ros_msgs-msg:right_foot-val is deprecated.  Use hubo_ros_msgs-msg:right_foot instead.")
  (right_foot m))

(cl:ensure-generic-function 'left_wrist-val :lambda-list '(m))
(cl:defmethod left_wrist-val ((m <HuboState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hubo_ros_msgs-msg:left_wrist-val is deprecated.  Use hubo_ros_msgs-msg:left_wrist instead.")
  (left_wrist m))

(cl:ensure-generic-function 'right_wrist-val :lambda-list '(m))
(cl:defmethod right_wrist-val ((m <HuboState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hubo_ros_msgs-msg:right_wrist-val is deprecated.  Use hubo_ros_msgs-msg:right_wrist instead.")
  (right_wrist m))

(cl:ensure-generic-function 'left_ankle-val :lambda-list '(m))
(cl:defmethod left_ankle-val ((m <HuboState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hubo_ros_msgs-msg:left_ankle-val is deprecated.  Use hubo_ros_msgs-msg:left_ankle instead.")
  (left_ankle m))

(cl:ensure-generic-function 'right_ankle-val :lambda-list '(m))
(cl:defmethod right_ankle-val ((m <HuboState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hubo_ros_msgs-msg:right_ankle-val is deprecated.  Use hubo_ros_msgs-msg:right_ankle instead.")
  (right_ankle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <HuboState>) ostream)
  "Serializes a message object of type '<HuboState>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'joints))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'joints))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'left_hand) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'right_hand) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'imu) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'left_foot) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'right_foot) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'left_wrist) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'right_wrist) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'left_ankle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'right_ankle) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <HuboState>) istream)
  "Deserializes a message object of type '<HuboState>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'joints) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'joints)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'hubo_ros_msgs-msg:HuboJointState))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'left_hand) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'right_hand) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'imu) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'left_foot) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'right_foot) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'left_wrist) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'right_wrist) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'left_ankle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'right_ankle) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<HuboState>)))
  "Returns string type for a message object of type '<HuboState>"
  "hubo_ros_msgs/HuboState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'HuboState)))
  "Returns string type for a message object of type 'HuboState"
  "hubo_ros_msgs/HuboState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<HuboState>)))
  "Returns md5sum for a message object of type '<HuboState>"
  "5245526d8ea9b726511504ca60eb9de2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'HuboState)))
  "Returns md5sum for a message object of type 'HuboState"
  "5245526d8ea9b726511504ca60eb9de2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<HuboState>)))
  "Returns full string definition for message of type '<HuboState>"
  (cl:format cl:nil "HuboJointState[] joints~%HuboHand left_hand~%HuboHand right_hand~%HuboIMU imu~%HuboIMU left_foot~%HuboIMU right_foot~%HuboFT left_wrist~%HuboFT right_wrist~%HuboFT left_ankle~%HuboFT right_ankle~%~%================================================================================~%MSG: hubo_ros_msgs/HuboJointState~%string name~%float64 position~%float64 velocity~%float64 current~%float64 temperature~%int32 active~%int32 zeroed~%~%================================================================================~%MSG: hubo_ros_msgs/HuboHand~%float64 thumb~%float64 index~%float64 middle~%float64 ring~%float64 pinky~%~%================================================================================~%MSG: hubo_ros_msgs/HuboIMU~%float64 x_acceleration~%float64 y_acceleration~%float64 z_acceleration~%float64 x_rotation~%float64 y_rotation~%~%================================================================================~%MSG: hubo_ros_msgs/HuboFT~%float64 Mx~%float64 My~%float64 Fz~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'HuboState)))
  "Returns full string definition for message of type 'HuboState"
  (cl:format cl:nil "HuboJointState[] joints~%HuboHand left_hand~%HuboHand right_hand~%HuboIMU imu~%HuboIMU left_foot~%HuboIMU right_foot~%HuboFT left_wrist~%HuboFT right_wrist~%HuboFT left_ankle~%HuboFT right_ankle~%~%================================================================================~%MSG: hubo_ros_msgs/HuboJointState~%string name~%float64 position~%float64 velocity~%float64 current~%float64 temperature~%int32 active~%int32 zeroed~%~%================================================================================~%MSG: hubo_ros_msgs/HuboHand~%float64 thumb~%float64 index~%float64 middle~%float64 ring~%float64 pinky~%~%================================================================================~%MSG: hubo_ros_msgs/HuboIMU~%float64 x_acceleration~%float64 y_acceleration~%float64 z_acceleration~%float64 x_rotation~%float64 y_rotation~%~%================================================================================~%MSG: hubo_ros_msgs/HuboFT~%float64 Mx~%float64 My~%float64 Fz~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <HuboState>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'joints) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'left_hand))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'right_hand))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'imu))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'left_foot))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'right_foot))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'left_wrist))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'right_wrist))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'left_ankle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'right_ankle))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <HuboState>))
  "Converts a ROS message object to a list"
  (cl:list 'HuboState
    (cl:cons ':joints (joints msg))
    (cl:cons ':left_hand (left_hand msg))
    (cl:cons ':right_hand (right_hand msg))
    (cl:cons ':imu (imu msg))
    (cl:cons ':left_foot (left_foot msg))
    (cl:cons ':right_foot (right_foot msg))
    (cl:cons ':left_wrist (left_wrist msg))
    (cl:cons ':right_wrist (right_wrist msg))
    (cl:cons ':left_ankle (left_ankle msg))
    (cl:cons ':right_ankle (right_ankle msg))
))
