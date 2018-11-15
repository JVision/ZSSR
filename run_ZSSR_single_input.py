import sys
import os
import configs
import ZSSR


def main(input_img, ground_truth = None, kernels = None, gpu = None, conf_str = None, results_path = './'):
    # Choose the wanted GPU
    if gpu is not None:
        os.environ["CUDA_VISIBLE_DEVICES"] = '%s' % gpu

    # 0 input for ground-truth or kernels means None
    #ground_truth = None if ground_truth == '0' else ground_truth
    
    if (kernels is not None):
        print ('*****', kernels)
        kernels.split(';')[:-1]

    # Setup configuration and results directory
    conf = configs.Config()
    if conf_str is not None:
        exec ('conf = configs.%s' % conf_str)
    conf.result_path = results_path

    # Run ZSSR on the image
    net = ZSSR.ZSSR(input_img, conf, ground_truth, kernels)
    net.run()


if __name__ == '__main__':
    #main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    main(sys.argv[1], gpu = 1, conf_str="X2_REAL_CONF", results_path = './' )
