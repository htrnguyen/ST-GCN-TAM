import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import sys

sys.path.extend(['../'])
from ntu_gendata import read_xyz
from preprocess import pre_normalization

def plot_skeleton(vertex_info, edge_info):
    ax = plt.axes(projection="3d")
    for i in range(3):
        x,y,z = vertex_info[i][:,0],vertex_info[i][:,1],vertex_info[i][:,2]
        ax.scatter(x,y,z, c='r',s=100)
        for edge in edge_info:
            x_p = [x[edge[0]],x[edge[1]]]
            y_p = [y[edge[0]],y[edge[1]]]
            z_p = [z[edge[0]],z[edge[1]]]
            if i == 0: 
                c_e = 'b'
            elif i == 1:
                c_e = 'y'
            else:
                c_e = 'g'
            ax.plot(x_p,y_p,z_p, color=c_e)
    plt.show()


info = read_xyz('D:\Hoc-tap\KLTN\source-code\kltn\data\S001C001P001R001A001.skeleton')
C, T, V, M = info.shape




inward_ori_index = [(1, 2), (2, 21), (3, 21), (4, 3), (5, 21), (6, 5), (7, 6),
                    (8, 7), (9, 21), (10, 9), (11, 10), (12, 11), (13, 1),
                    (14, 13), (15, 14), (16, 15), (17, 1), (18, 17), (19, 18),
                    (20, 19), (22, 23), (23, 8), (24, 25), (25, 12)]
edge_info = [(i - 1, j - 1) for (i, j) in inward_ori_index]



# visualize
# skeleton orignal
# vertex_info = np.transpose(info, [3, 1, 2, 0])[0]
# plot_skeleton(vertex_info,edge_info)

# normalization skeleton 
# vertex_info_v = np.transpose(pre_normalization(info.reshape(1,C,T,V,M))[0], [3, 1, 2, 0])[0]
# plot_skeleton(vertex_info_v,edge_info)

# print(pre_normalization(info.reshape(1,C,T,V,M)).shape)