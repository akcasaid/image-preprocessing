def resize_image_with_crop_or_pad(image, img_size=(64, 64, 64), **kwargs):
    """Image resizing. Resizes image by cropping or padding dimension
     to fit specified size.
    Args:
        image (np.ndarray): image to be resized
        img_size (list or tuple): new image size
        kwargs (): additional arguments to be passed to np.pad
    Returns:
        np.ndarray: resized image
    """

    assert isinstance(image, (np.ndarray, np.generic))
    assert (image.ndim - 1 == len(img_size) or image.ndim == len(img_size)), \
        'Example size doesnt fit image size'

    # Get the image dimensionality
    rank = len(img_size)

    # Create placeholders for the new shape
    from_indices = [[0, image.shape[dim]] for dim in range(rank)]
    to_padding = [[0, 0] for dim in range(rank)]

    slicer = [slice(None)] * rank

    # For each dimensions find whether it is supposed to be cropped or padded
    for i in range(rank):
        if image.shape[i] < img_size[i]:
            to_padding[i][0] = (img_size[i] - image.shape[i]) // 2
            to_padding[i][1] = img_size[i] - image.shape[i] - to_padding[i][0]
        else:
            from_indices[i][0] = int(np.floor((image.shape[i] - img_size[i]) / 2.))
            from_indices[i][1] = from_indices[i][0] + img_size[i]

        # Create slicer object to crop or leave each dimension
        slicer[i] = slice(from_indices[i][0], from_indices[i][1])

    # Pad the cropped image to extend the missing dimension
    return np.pad(image[slicer], to_padding, **kwargs)


# Crop to [64, 64, 64]
img_cropped = resize_image_with_crop_or_pad(image, [96, 96, 96], mode='symmetric')

# Resizing image to [128, 256, 256] required padding
img_padded = resize_image_with_crop_or_pad(image, [256, 544, 544], mode='symmetric')

# Visualise using matplotlib.
f, axarr = plt.subplots(1, 3, figsize=(15,15));
axarr[0].imshow(np.squeeze(image[100, :, :]), cmap='gray',origin='lower');
axarr[0].axis('off')
axarr[0].set_title('Original image {}'.format(image.shape))

axarr[1].imshow(np.squeeze(img_cropped[32, :, :]), cmap='gray',origin='lower');
axarr[1].axis('off')
axarr[1].set_title('Cropped to {}'.format(img_cropped.shape))

axarr[2].imshow(np.squeeze(img_padded[140, :, :]), cmap='gray',origin='lower');
axarr[2].axis('off')
axarr[2].set_title('Padded to {}'.format(img_padded.shape))
plt.tight_layout()
plt.subplots_adjust(wspace=0, hspace=0)
