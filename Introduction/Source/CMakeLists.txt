# Program#0
#
# CMakeLists.txt for Program#0

cmake_minimum_required(VERSION 2.8)

project(HelloWorld CXX)

# compile with debugging flags
#set(CMAKE_BUILD_TYPE debug)

# compile without debugging flags
set(CMAKE_BUILD_TYPE release)

# add a compiler flag for the C++2011 standard
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -std=c++0x")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
link_directories(${OpenCV_LIBRARY_DIRS})

add_executable(HelloWorld HelloWorld.cpp)
target_link_libraries(HelloWorld ${OpenCV_LIBS})



