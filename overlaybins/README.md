# Overlay Selector Guide
This directory contains various hardware overlays for accelerating neural networks on different platforms.

## Background
Field Programmable Gate Arrays - [FPGA](https://www.xilinx.com/products/silicon-devices/fpga/what-is-an-fpga.html)s -
are semiconductor devices, which by design implement an array of logic blocks with a programmable interconnect.
Unlike "hardened" devices (i.e. CPU/GPU) FPGAs can be programmed to implement a hardware design that does specifically what the user wants.
After the design of the hardware system, the FPGA must be programmed using a binary file. This process is typically referred to as configuration.
Furthermore, in a usecase where there is fixed functionality, and dynamic functionality an FPGA can be partially reconfigured.
In a datacenter environment, the FPGA is always connected to the CPU via PCIe, and it is always connected to external off-chip memory.
Given the above assumption the FPGA binary can be partitioned into a static shell (Xilinx uses the term DSA), and a dynamic overlay (Xilinx uses the term xclbin).
The static shell must be loaded prior to the loading of any overlay. Xilinx's cloud partners have already loaded the shell.
If this explanation seems a bit confusing, don't worry too much about it. All you need to know is that you need to pick an overlay that will best meet your application needs.
It will be loaded by the Python API.

## [AWS](https://aws.amazon.com/ec2/instance-types/f1/) Hardware Overlays (XCLBINs)


| Overlay           | # of PE | Bitwidth | DSP Array Dim. | Max Image H/W | Max Image Depth | On-Chip Activation Memory | Max Filter Size (HxWxD) | DSA Version |
| ----------------- | ------- | -------- | -------------- | ------------- | --------------- | ------------------------- | ----------------------- | ----------- |
| overlay_0.xclbin*  | 4 | 8 | 32x28 | 1023 | 4095 | 4MB | 4608 | 5.0-aws |
| overlay_1.xclbin*  | 4 | 16 | 32x28 | 1023 | 4095 | 4MB | 4608 | 5.0-aws |
| overlay_2.xclbin*  | 1 | 8 | 32x56 | 1023 | 4095 | 5MB | 9792 | 5.0-aws |
| overlay_3.xclbin*  | 1 | 16 | 32x56 | 1023 | 4095 | 5MB | 9792 | 5.0-aws |

***Note:** Currently, only overlay_2 and overlay_3 are available. There is a known issue where you may experience speed degradations. This will be updated shortly. 

| Overlay           | Notes |
| ----------------- | ------- |
| overlay_0.xclbin  | This overlay is best for high throughput applications as it can process 8 images in parallel, it does not support networks with very large filters such as YOLOv2 |
| overlay_1.xclbin  | This overlay is great for high throughput applications as it can process 4 images in parallel, and it will maintain accuracy nearly equivalent to float32 models |
| overlay_2.xclbin  | This overlay is best for high throughput applications as it can process 2 images in parallel at 2x speed compared to 32x28 alternative, the larger DSP compute array provides minimum latency, and the larger supported filter size accomodates large networks like YOLOv2 |
| overlay_3.xclbin  | This overlay is good for high throughput applications as it can process 1 image at a time at 2x speed compared to 32x28 alternative, the larger DSP compute array provides minimum latency, and the larger supported filter size accomodates large networks like YOLOv2, and it will maintain accuracy nearly equivalent to float32 models |



## [NIMBIX](https://www.nimbix.net/xilinx/) Hardware Overlays (XCLBINs)

| Overlay           | # of PE | Bitwidth | DSP Array Dim. | Max Image H/W | Max Image Depth | On-Chip Activation Memory | Max Filter Size (HxWxD) | DSA Version |
| ----------------- | ------- | -------- | -------------- | ------------- | --------------- | ------------------------- | ----------------------- | ----------- |
| overlay_0.xclbin  | 4 | 8 | 32x28 | 1023 | 4095 | 4MB | 4608 | 5.1 |
| overlay_1.xclbin  | 4 | 16 | 32x28 | 1023 | 4095 | 4MB | 4608 | 5.1 |
| overlay_2.xclbin  | 2 | 8 | 32x56 | 1023 | 4095 | 6MB | 9792 | 5.1 |
| overlay_3.xclbin  | 2 | 16 | 32x56 | 1023 | 4095 | 6MB | 9792 | 5.1 |

| Overlay           | Notes |
| ----------------- | ------- |
| overlay_0.xclbin  | This overlay is best for high throughput applications as it can process 8 images in parallel, it does not support networks with very large filters such as YOLOv2 |
| overlay_1.xclbin  | This overlay is great for high throughput applications as it can process 4 images in parallel, and it will maintain accuracy nearly equivalent to float32 models |
| overlay_2.xclbin  | This overlay is best for high throughput applications as it can process 4 images in parallel at 2x speed compared to 32x28 alternative, the larger DSP compute array provides minimum latency, and the larger supported filter size accomodates large networks like YOLOv2 |
| overlay_3.xclbin  | This overlay is great for high throughput applications as it can process 2 images in parallel at 2x speed compared to 32x28 alternative, the larger DSP compute array provides minimum latency, and the larger supported filter size accomodates large networks like YOLOv2, and it will maintain accuracy nearly equivalent to float32 models |

## [VCU1525](https://www.xilinx.com/products/boards-and-kits/vcu1525-a.html) Hardware Overlays (XCLBINs)

| Overlay           | # of PE | Bitwidth | DSP Array Dim. | Max Image H/W | Max Image Depth | On-Chip Activation Memory | Max Filter Size (HxWxD) | DSA Version |
| ----------------- | ------- | -------- | -------------- | ------------- | --------------- | ------------------------- | ----------------------- | ----------- |
| overlay_0.xclbin  | 4 | 8 | 32x28 | 1023 | 4095 | 4MB | 4608 | 5.1 |
| overlay_1.xclbin  | 4 | 16 | 32x28 | 1023 | 4095 | 4MB | 4608 | 5.1 |
| overlay_2.xclbin  | 2 | 8 | 32x56 | 1023 | 4095 | 6MB | 9792 | 5.1 |
| overlay_3.xclbin  | 2 | 16 | 32x56 | 1023 | 4095 | 6MB | 9792 | 5.1 |

| Overlay           | Notes |
| ----------------- | ------- |
| overlay_0.xclbin  | This overlay is best for high throughput applications as it can process 8 images in parallel, it does not support networks with very large filters such as YOLOv2 |
| overlay_1.xclbin  | This overlay is great for high throughput applications as it can process 4 images in parallel, and it will maintain accuracy nearly equivalent to float32 models |
| overlay_2.xclbin  | This overlay is best for high throughput applications as it can process 4 images in parallel at 2x speed compared to 32x28 alternative, the larger DSP compute array provides minimum latency, and the larger supported filter size accomodates large networks like YOLOv2 |
| overlay_3.xclbin  | This overlay is great for high throughput applications as it can process 2 images in parallel at 2x speed compared to 32x28 alternative, the larger DSP compute array provides minimum latency, and the larger supported filter size accomodates large networks like YOLOv2, and it will maintain accuracy nearly equivalent to float32 models |
