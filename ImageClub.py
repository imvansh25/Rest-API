import cv2


def hconcat_resize_min(img_list, interpolation=cv2.INTER_CUBIC):

    h_min = min(im.shape[0] for im in img_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in img_list]


    im_h_resize = cv2.hconcat(im_list_resize)
    return im_h_resize


def vconcat_resize_min(img_list,interpolation=cv2.INTER_CUBIC):

    w_min = min(im.shape[1] for im in img_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in img_list]
    
    im_v_resize = cv2.vconcat(im_list_resize)
    return im_v_resize

