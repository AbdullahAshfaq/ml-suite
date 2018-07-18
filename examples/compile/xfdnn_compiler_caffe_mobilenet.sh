#!/bin/bash

for DSP_WIDTH in 28 56; do
    python $MLSUITE_ROOT/xfdnn/tools/compile/bin/xfdnn_compiler_caffe.py \
        -n $MLSUITE_ROOT/models/caffe/mobilenet/fp32/mobilenet_without_bn_deploy.prototxt \
        -g $MLSUITE_ROOT/examples/compile/work/caffe/mobilenet/fp32/mobilenet_without_bn_deploy_${DSP_WIDTH}.cmds \
        -w $MLSUITE_ROOT/models/caffe/mobilenet/fp32/mobilenet_without_bn.caffemodel \
        -s all \
        -i ${DSP_WIDTH} \
        -m 4 \
        -d 0
done

