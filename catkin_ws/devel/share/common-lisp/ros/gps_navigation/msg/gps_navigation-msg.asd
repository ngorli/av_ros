
(cl:in-package :asdf)

(defsystem "gps_navigation-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "WaypointAction" :depends-on ("_package_WaypointAction"))
    (:file "_package_WaypointAction" :depends-on ("_package"))
    (:file "WaypointActionFeedback" :depends-on ("_package_WaypointActionFeedback"))
    (:file "_package_WaypointActionFeedback" :depends-on ("_package"))
    (:file "WaypointActionGoal" :depends-on ("_package_WaypointActionGoal"))
    (:file "_package_WaypointActionGoal" :depends-on ("_package"))
    (:file "WaypointActionResult" :depends-on ("_package_WaypointActionResult"))
    (:file "_package_WaypointActionResult" :depends-on ("_package"))
    (:file "WaypointFeedback" :depends-on ("_package_WaypointFeedback"))
    (:file "_package_WaypointFeedback" :depends-on ("_package"))
    (:file "WaypointGoal" :depends-on ("_package_WaypointGoal"))
    (:file "_package_WaypointGoal" :depends-on ("_package"))
    (:file "WaypointResult" :depends-on ("_package_WaypointResult"))
    (:file "_package_WaypointResult" :depends-on ("_package"))
  ))