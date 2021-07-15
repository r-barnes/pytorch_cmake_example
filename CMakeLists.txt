cmake_minimum_required (VERSION 3.9)

project(pytorch_cmake_example LANGUAGES CXX CUDA)

find_package(Python REQUIRED COMPONENTS Development)
find_package(Torch REQUIRED)

if(NOT DEFINED CMAKE_CUDA_ARCHITECTURES)
  set(CMAKE_CUDA_ARCHITECTURES 61)
endif()

add_library(pytorch_cmake_example SHARED
  main.cu
)
target_compile_features(pytorch_cmake_example PRIVATE cxx_std_11)
target_link_libraries(pytorch_cmake_example PRIVATE ${TORCH_LIBRARIES} Python::Python)

# Use if the default GCC version gives issues
target_compile_options(pytorch_cmake_example PRIVATE $<$<COMPILE_LANGUAGE:CUDA>:-ccbin g++-9>)

# Use a variant of this if you're on an earlier cmake than 3.18
# target_compile_options(pytorch_cmake_example PRIVATE $<$<COMPILE_LANGUAGE:CUDA>:-gencode arch=compute_61,code=sm_61>)
