# RBNs

A small exploration of RBNs [à la Kauffman](https://doi.org/10.1016/0022-5193(69)90015-0).

A random network of `N x N` nodes is instantiated, with node states $∈ {0, 1}$. Each node forms `K` interactions with other nodes in the net. The output of each node is given by the random allocation of a logic gate, and by the corresponding inputs. There's also another parameter `η`, which represents the fraction of nodes which will have their bits flipped (akin to noise). The choice of gates and interactions between nodes is done in a random manner, but is only instantiated initially.

Will also need the `ffmpeg` writer.

### Some Examples

![K = 2, η = 0](rbn_animations/RBN_K2_n0.mp4)

![K = 2, η = 0.3](rbn_animations/RBN_K2_n03.mp4)

![K = 2, η = 0.8](rbn_animations/RBN_K2_n08.mp4)

![K = 2, η = 1](rbn_animations/RBN_K2_n1.mp4)

![K = 3, η = 0](rbn_animations/RBN_K3_n0.mp4)

![K = 3, η = 0.3](rbn_animations/RBN_K3_n03.mp4)

![K = 3, η = 0.8](rbn_animations/RBN_K3_n08.mp4)

![K = 3, η = 1](rbn_animations/RBN_K3_n1.mp4)

![K = 5, η = 0](rbn_animations/RBN_K5_n0.mp4)

![K = 5, η = 0.3](rbn_animations/RBN_K5_n03.mp4)

![K = 5, η = 0.8](rbn_animations/RBN_K5_n08.mp4)

![K = 5, η = 1](rbn_animations/RBN_K5_n1.mp4)

![K = 10, η = 0](rbn_animations/RBN_K10_n0.mp4)

![K = 10, η = 0.3](rbn_animations/RBN_K10_n03.mp4)

![K = 10, η = 0.8](rbn_animations/RBN_K10_n08.mp4)

![K = 10, η = 1](rbn_animations/RBN_K10_n1.mp4)