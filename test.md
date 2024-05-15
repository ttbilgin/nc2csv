The Radial Basis Function (RBF) kernel is a popular choice for SVMs, particularly when dealing with non-linear problems. The RBF kernel is defined as:
$K(x_i, x_j) = \exp(-\gamma |x_i - x_j|^2)$ (1)
where $x_i$ and $x_j$ are two data points, $|x_i - x_j|^2$ represents the squared Euclidean distance between them, and $\gamma$ is a tunable parameter that controls the influence of individual data points on the kernel.
The SVM objective function with the RBF kernel can be formulated as:
$\min_{w, b, \xi} \frac{1}{2} w^Tw + C\sum_{i=1}^n \xi_i$ (2)
subject to the constraints:
$y_i(w^T\phi(x_i) + b) \geq 1 - \xi_i$ (3)
$\xi_i \geq 0, \quad i = 1, \ldots, n$ (4)
Here, $w$ and $b$ are the weights and bias of the hyperplane, respectively, $\phi(x_i)$ is the non-linear mapping function induced by the RBF kernel, $y_i \in {-1, 1}$ is the class label of the $i$-th data point, $\xi_i$ are the slack variables that allow for some misclassification, and $C$ is a regularization parameter that controls the trade-off between maximizing the margin and minimizing the misclassification error.
By introducing the Lagrange multipliers $\alpha_i \geq 0$, the dual formulation of the SVM problem can be obtained:
$\max_{\alpha} \sum_{i=1}^n \alpha_i - \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \alpha_i\alpha_jy_iy_jK(x_i, x_j)$ (5)
subject to:
$\sum_{i=1}^n \alpha_iy_i = 0$ (6)
$0 \leq \alpha_i \leq C, \quad i = 1, \ldots, n$ (7)
The decision function for classifying a new data point $x$ is given by:
$f(x) = \text{sign}\left(\sum_{i=1}^n \alpha_iy_iK(x_i, x) + b\right)$ (8)
The RBF kernel introduces non-linearity into the SVM model, allowing it to handle complex, non-linear decision boundaries effectively. The parameter $\gamma$ plays a crucial role in controlling the behavior of the RBF kernel, influencing the smoothness of the decision boundary and the model's ability to generalize to unseen data.
