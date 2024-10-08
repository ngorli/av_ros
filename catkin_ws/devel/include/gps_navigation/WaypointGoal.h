// Generated by gencpp from file gps_navigation/WaypointGoal.msg
// DO NOT EDIT!


#ifndef GPS_NAVIGATION_MESSAGE_WAYPOINTGOAL_H
#define GPS_NAVIGATION_MESSAGE_WAYPOINTGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace gps_navigation
{
template <class ContainerAllocator>
struct WaypointGoal_
{
  typedef WaypointGoal_<ContainerAllocator> Type;

  WaypointGoal_()
    : latitude(0.0)
    , longitude(0.0)  {
    }
  WaypointGoal_(const ContainerAllocator& _alloc)
    : latitude(0.0)
    , longitude(0.0)  {
  (void)_alloc;
    }



   typedef double _latitude_type;
  _latitude_type latitude;

   typedef double _longitude_type;
  _longitude_type longitude;





  typedef boost::shared_ptr< ::gps_navigation::WaypointGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::gps_navigation::WaypointGoal_<ContainerAllocator> const> ConstPtr;

}; // struct WaypointGoal_

typedef ::gps_navigation::WaypointGoal_<std::allocator<void> > WaypointGoal;

typedef boost::shared_ptr< ::gps_navigation::WaypointGoal > WaypointGoalPtr;
typedef boost::shared_ptr< ::gps_navigation::WaypointGoal const> WaypointGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::gps_navigation::WaypointGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::gps_navigation::WaypointGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace gps_navigation

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'gps_navigation': ['/home/user/catkin_ws/devel/share/gps_navigation/msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::gps_navigation::WaypointGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::gps_navigation::WaypointGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gps_navigation::WaypointGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gps_navigation::WaypointGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gps_navigation::WaypointGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gps_navigation::WaypointGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::gps_navigation::WaypointGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "680c6dc7da65a2421a822205dcbdb600";
  }

  static const char* value(const ::gps_navigation::WaypointGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x680c6dc7da65a242ULL;
  static const uint64_t static_value2 = 0x1a822205dcbdb600ULL;
};

template<class ContainerAllocator>
struct DataType< ::gps_navigation::WaypointGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "gps_navigation/WaypointGoal";
  }

  static const char* value(const ::gps_navigation::WaypointGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::gps_navigation::WaypointGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# goal\n\
float64 latitude\n\
float64 longitude\n\
\n\
";
  }

  static const char* value(const ::gps_navigation::WaypointGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::gps_navigation::WaypointGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.latitude);
      stream.next(m.longitude);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct WaypointGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::gps_navigation::WaypointGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::gps_navigation::WaypointGoal_<ContainerAllocator>& v)
  {
    s << indent << "latitude: ";
    Printer<double>::stream(s, indent + "  ", v.latitude);
    s << indent << "longitude: ";
    Printer<double>::stream(s, indent + "  ", v.longitude);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GPS_NAVIGATION_MESSAGE_WAYPOINTGOAL_H
