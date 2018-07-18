import os

def select_config(selection):
  # User can choose to run YOLO at different input sizes
  # - 608x608
  # - 224x224
  # User can choose to run YOLO at different quantization precisions
  # - 16b
  # - 8b

  mlsuiteRoot = os.getenv("MLSUITE_ROOT", "../..")

  configs = {
     '608_16b': 
               {'dims': [3, 608, 608], 
                'bitwidths': [16, 16, 16], 
                'network_file': mlsuiteRoot+'/models/yolov2/caffe/fp32/yolo_deploy_608.prototxt', 
                'netcfg': 'yolov2.caffemodel_data/yolo.cmds', 
                'quantizecfg': 'yolov2.caffemodel_data/yolo_deploy_608_16b.json',
                'datadir': 'yolov2.caffemodel_data',
                'firstfpgalayer': 'conv0',
                'classes': 80,
                'memory' : 5,
                'dsp' : 56,
                'ddr' : 256,
                'weights': mlsuiteRoot+'/models/yolov2/caffe/fp32/yolov2.caffemodel'},
     '608_8b': {'dims': [3, 608, 608], 
                'bitwidths': [8, 8, 8], 
                'network_file': mlsuiteRoot+'/models/yolov2/caffe/fp32/yolo_deploy_608.prototxt', 
                'netcfg': 'yolov2.caffemodel_data/yolo.cmds', 
                'quantizecfg': 'yolov2.caffemodel_data/yolo_deploy_608_8b.json',
                'datadir': 'yolov2.caffemodel_data',
                'firstfpgalayer': 'conv0',
                'classes': 80,
                'memory' : 5,
                'dsp' : 56,
                'ddr' : 256,
                'weights': mlsuiteRoot+'/models/yolov2/caffe/fp32/yolov2.caffemodel'},
     '224_16b': {'dims': [3, 224, 224], 
                'bitwidths': [16, 16, 16], 
                'network_file': mlsuiteRoot+'/models/yolov2/caffe/fp32/yolo_deploy_224.prototxt', 
                'netcfg': 'yolov2.caffemodel_data/yolo.cmds', 
                'quantizecfg': 'yolov2.caffemodel_data/yolo_deploy_224_16b.json',
                'datadir': 'yolov2.caffemodel_data',
                'firstfpgalayer': 'conv0',
                'classes': 80,
                'memory' : 5,
                'dsp' : 56,
                'ddr' : None,
                'weights': mlsuiteRoot+'/models/yolov2/caffe/fp32/yolov2.caffemodel'},
      '224_8b': {'dims': [3, 224, 224], 
                 'bitwidths': [8, 8, 8], 
                 'network_file': mlsuiteRoot+'/models/yolov2/caffe/fp32/yolo_deploy_224.prototxt', 
                 'netcfg': 'yolov2.caffemodel_data/yolo.cmds', 
                 'quantizecfg': 'yolov2.caffemodel_data/yolo_deploy_224_8b.json',
                 'datadir': 'yolov2.caffemodel_data',
                 'firstfpgalayer': 'conv0',
                 'classes': 80,
                 'memory' : 5,
                 'dsp' : 56,
                 'ddr' : None,
                 'weights': mlsuiteRoot+'/models/yolov2/caffe/fp32/yolov2.caffemodel'},
      '224_16b_tend': {'dims': [3, 224, 224],
                      'bitwidths': [16, 16, 16],
                      'network_file': 'tend.prototxt',
                      'netcfg': 'work/yolo.cmds',
                      'quantizecfg': 'work/yolo_deploy_224_16b.json',
                      'datadir': 'work/tend.caffemodel_data',
                      'firstfpgalayer': 'layer1-conv',
                      'classes': 9,
                      'memory' : 5,
                      'dsp' : 56,
                      'ddr' : None,
                      'weights': 'tend.caffemodel'},
      '224_8b_tend': {'dims': [3, 224, 224],
                      'bitwidths': [8, 8, 8],
                      'network_file': 'tend.prototxt',
                      'netcfg': 'work/yolo.cmds',
                      'quantizecfg': 'work/yolo_deploy_224_8b.json',
                      'datadir': 'work/tend.caffemodel_data',
                      'firstfpgalayer': 'layer1-conv',
                      'classes': 9,
                      'memory' : 5,
                      'dsp' : 56,
                      'ddr' : None,
                      'weights': 'tend.caffemodel'}}

  # Choose a config here
  if selection in configs:
    config = configs[selection]
    aws = False
    eb = False
    if config['bitwidths'][0] == 8:
      eb = True
    if os.path.exists('/sys/hypervisor/uuid'):
      with open('/sys/hypervisor/uuid') as (file):
        contents = file.read()
        if 'ec2' in contents:
          print 'Runnning on Amazon AWS EC2'
          aws = True
          if eb:
            config["xclbin"] = mlsuiteRoot+'/overlaybins/aws/overlay_2.xclbin'
          else:
            config["xclbin"] = mlsuiteRoot+'/overlaybins/aws/overlay_3.xclbin'
    if not aws:
      if eb:
        config["xclbin"] = mlsuiteRoot+'/overlaybins/1525/overlay_2.xclbin'
      else:
        config["xclbin"] = mlsuiteRoot+'/overlaybins/1525/overlay_3.xclbin'
    return config
  else:
    print("Error: You chose an invalid configuration")
    return None
