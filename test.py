import torch
torch.ops.load_library("build/libpytorch_cmake_example.so")

shape = (3,3,3)
a = torch.randint(0, 10, shape, dtype=torch.float).cuda()
a_plus_one = torch.ops.pytorch_cmake_example.add_one(a)
