from DsCML.models.xmuda_arch import Net2DSeg, Net3DSeg, L2G_classifier_2D, L2G_classifier_3D
from DsCML.models.metric import SegIoU


def build_model_2d(cfg):
    model = Net2DSeg(num_classes=cfg.MODEL_2D.NUM_CLASSES,
                     backbone_2d=cfg.MODEL_2D.TYPE,
                     backbone_2d_kwargs=cfg.MODEL_2D[cfg.MODEL_2D.TYPE],
                     dual_head=cfg.MODEL_2D.DUAL_HEAD
                     )
    train_metric = SegIoU(cfg.MODEL_2D.NUM_CLASSES, name='seg_iou_2d')
    return model, train_metric

def build_2d_L2G(cfg):
    model = L2G_classifier_2D(input_channels=64,
                           num_classes=cfg.MODEL_2D.NUM_CLASSES
    )
    return model

def build_3d_L2G(cfg):
    model = L2G_classifier_3D(input_channels=16,
                           num_classes=cfg.MODEL_2D.NUM_CLASSES
    )
    return model

def build_model_3d(cfg):
    model = Net3DSeg(num_classes=cfg.MODEL_3D.NUM_CLASSES,
                     backbone_3d=cfg.MODEL_3D.TYPE,
                     backbone_3d_kwargs=cfg.MODEL_3D[cfg.MODEL_3D.TYPE],
                     dual_head=cfg.MODEL_3D.DUAL_HEAD
                     )
    train_metric = SegIoU(cfg.MODEL_3D.NUM_CLASSES, name='seg_iou_3d')
    return model, train_metric
