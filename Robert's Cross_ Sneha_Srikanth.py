#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from google.colab import drive
drive.mount("/content/drive",force_remount=True)

data_dir = '/content/drive/My Drive'


# In[ ]:


get_ipython().run_line_magic('pylab', 'inline')
im = imread(f'{data_dir}/HenrysPocket_1-e1492452328122.jpg')


# In[ ]:


fig = figure(0, (6,6))
imshow(im); title('Dog!');


# In[ ]:


fig = figure(0, (12,6))
result = hist(im.ravel(), 255); grid(1)


# In[ ]:


im_scaled = im/255


# In[ ]:


im_scaled.dtype


# In[ ]:


fig = figure(0, (12,6))
hist(im_scaled.ravel(), 255); grid(1)


# In[ ]:


x = np.mean(im_scaled, axis=2);
imshow(x,cmap='gray');
colorbar()


# In[ ]:


edges=roberts_cross(x)


# In[ ]:


def roberts_cross(x):
    '''Compute Robert's Cross of input image x.
       Args: x (nxm) grayscale floating point image
       Returns: (n-1) x (m-1) edge image.'''
    
    #Our output will image will be one pixel smaller than our image
    edges = np.zeros((x.shape[0]-1,x.shape[1]-1)) 

    for i in range(x.shape[0]-1):
        for j in range(x.shape[1]-1):
            #Grab Appropriate (2x2) image patch
            image_patch = x[i:i+2, j:j+2]
            # Compute Robert's Cross for image patch
            edges[i, j] = np.sqrt((image_patch[0,0] - image_patch[1, 1])**2 + 
                                   (image_patch[1, 0] - image_patch[0, 1])**2)
            
    return edges

    

    


# In[ ]:


imshow(edges)


# In[ ]:


thresh = 0.001

edges_thresh = edges.copy()
edges_thresh[edges_thresh<thresh] = 0
# My addition

fig = figure(0, (8,8))
imshow(edges_thresh)
colorbar()
title("Edges computed with Robert's Cross thresh");


# In[ ]:


imshow(edges_thresh, cmap = 'gray')

