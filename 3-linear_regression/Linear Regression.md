# 线性回归模型

已知$n$个样本$\{\mathbf{x_0}, \mathbf{x_1}, \cdots \mathbf{x_i}, \cdots,   \mathbf{x_n} \}$， 每个样本都是$d$维的，也就是说有$d$个特征，将其按行排列组成$\mathbf{X} \in \mathbb{R}^{n \times d}$。并且知道每个样本对应的输出是个标量$y_i$, 将所有$y_i$组成向量$\mathbf{y} \in \mathbb{R}^n$。线性回归模型就是要找到一组公共的权重$\mathbf{{w}}$和标量偏置${b}$，使得$\hat{\mathbf{y}} = \mathbf{Xw} + b \mathbf{I}$尽可能接近真实的$\mathbf{y}$。

既然我们想要使得$\hat{\mathbf{y}}$接近$\mathbf{y}$，那这个接近程度就需要有一个度量，一般我们采用**平方误差**来度量：
* 平方误差：
$$
l_{i}(\mathbf{w}, b) = \frac{1}{2}(\hat{y}_{i} - y_{i})^2 \tag{eq-squared-error}
$$
其中系数$\frac{1}{2}$不会带来本质差别，只是为了方便求导。
在1维的情况，误差可以可视化为：
![[Pasted image 20240913235436.png|254]]
[图1. 用线性模型拟合数据]

为了度量在所有样本上的误差，我们将每个样本的误差求均值：
$$
L(\mathbf{w}, b) = \frac{1}{n} \sum_{i}^n l_{i}(\mathbf{w}, b)  = \frac{1}{n} \sum_{i}^n \frac{1}{2}(\mathbf{w}^T \mathbf{x}_{i} + b - y_{i})^2
$$
最终，线性回归模型可以归结为，寻找一组参数$(\mathbf{w}^*, b^*)$, 使得$L(\mathbf{w}, b)$最小：
$$
\mathbf{w}^*, b^* = {argmin}_{\mathbf{w}, b} L(\mathbf{w}, b)
$$

# 线性回归模型的解析解

我们可以将b合入$\mathbf{w}$, 具体做法是在$\mathbf{w}$中增加一行，样本$\mathbf{x}$中增加一维，其值永远为1。这样原来的$\hat{\mathbf{y}} = \mathbf{X}\mathbf{w} + b\mathbf{I}$就表示为$\hat{\mathbf{y}} = \mathbf{Xw}$。使用最小二乘得到解析解：
$$
\mathbf{w}^* = (\mathbf{X^T X})^{-1} \mathbf{X}^T \mathbf{y}
$$
# 随机梯度下降算法

由于不是所有的模型都有解析解，我们需要一个更通用的方法来获得解。**梯度下降（gradient descent）** 就是一种比较通用的解法。

使用梯度下降算法，我们需要知道损失函数以及损失函数对参数的导数（这就是深度学习框架为什么都提供自动微分的原因！）。
* 随机梯度下降算法：
$$
(\mathbf{w}^{k+1}, b^{k+1}) = (\mathbf{w}^k, b^{k}) - \frac{\eta}{|\mathit{B}|} \sum_{i \in \mathit{B}}\left( \frac{ \partial l_{i}(\mathbf{w}, b)} { \partial \mathbf{w} }, \frac{ \partial l_{i}(\mathbf{w}, b) }{ \partial b }   \right)
$$


