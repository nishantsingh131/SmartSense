# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\SensorTest_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\SensorTest_autogen.dir\\ParseCache.txt"
  "SensorTest_autogen"
  )
endif()
