## 1. tensorboard使用
    from torch.utils.tensorboard import SummaryWriter
    writer = SummaryWriter('./path/to/log')
    writer.add_scalar(tag, scalar_value, global_step=None, walltime=None)
    
    for epoch in range(100):
        mAP = eval(model)
        writer.add_scalar('mAP', mAP, epoch)

    writer.add_image(tag, img_tensor, global_step=None,
                    walltime=None, dataformats='CHW')
    writer.add_images(tag, img_tensor, global_step=None,
                    walltime=None, dataformats='NCHW')
   
   
     $ tensorboard - -logdir = ./path/to/the/folder - -port 8123
