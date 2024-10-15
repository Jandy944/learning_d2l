# 矩阵、向量求导
* 例1: $\mathbf{x}, \mathbf{w} \in \mathbb{R}^n, y \in R, z = (\langle\mathbf{x}, \mathbf{w} \rangle - y)^2$，求$\frac{\partial z}{\partial \mathbf{w}}$

$\frac{\partial{z}}{\partial{\mathbf{w}}}$是一个向量，第i个元素为$\frac{ \partial z }{ \partial w_{i} }$，因此我们先把$z$写成各分量的形式：
$$
z = ((\sum_{i} x_{i} w_{i}) - y)^2  \tag{1}
$$
因此
$$
\frac{ \partial z }{ \partial w_{i} } =
    2\left( \mathbf{x}^T \mathbf{w} -y \right) x_{i} \tag{2}
$$
那么
$$
\frac{ \partial z }{ \partial \mathbf{w} }  =
	2(\mathbf{x}^T \mathbf{w} -y) \mathbf{x}^T \tag{3}
$$

* 例2：$\mathbf{X} \in \mathbb{R}^{m\times n}, \mathbf{w} \in \mathbb{R}^n \mathbf{y} \in \mathbb{R}^m, z = ||\mathbf{X}\mathbf{w} - \mathbf{y}||^2$，计算$\frac{ \partial z }{ \partial \mathbf{w} }$
这里需要先引入下**向量对向量的求导**，我们把它定义为一个张量：
外层为分子的维度，内层为分母的维度
$$
\begin{align}

\frac{ \partial \mathbf{y} }{ \partial \mathbf{x } } &= 
\begin{bmatrix}   
    \begin{bmatrix}
    \frac{ \partial   y_{0} }{ \partial \mathbf{x} } 
    \end{bmatrix}  \\ 
     \vdots  \\
    \begin{bmatrix}
    \frac{ \partial y_{i} }{ \partial \mathbf{x} } 
    \end{bmatrix}   \\
    \vdots  \\
    \begin{bmatrix}
     \frac{ \partial y_{m} }{ \partial \mathbf{x} } 
    \end{bmatrix}
\end{bmatrix} \\  
& =\begin{bmatrix}
   \begin{bmatrix}
    \frac{ \partial y_{0} }{ \partial x_{0}   } \cdots \frac{ \partial y_{0} }{ \partial x_{i} } \dots  \frac{ \partial y_{0} }{ \partial x_{n} } 
   \end{bmatrix}  \\ 
    \vdots   \\
   \begin{bmatrix}
    \frac{ \partial y_{j} }{ \partial x_{0}   } \cdots \frac{ \partial y_{j} }{ \partial x_{i} } \dots  \frac{ \partial y_{j} }{ \partial x_{n} } 
   \end{bmatrix} \\
    \vdots   \\
   \begin{bmatrix}
    \frac{ \partial y_{m} }{ \partial x_{0}   } \cdots \frac{ \partial y_{n} }{ \partial x_{i} } \dots  \frac{ \partial y_{n} }{ \partial x_{n} } 
   \end{bmatrix} \\

\end{bmatrix}
\end{align} \tag{2-1}
$$
记$\mathbf{a} = \mathbf{Xw} - \mathbf{y}$, 则
$$
\frac{ \partial z }{ \partial \mathbf{w} }  = \frac{ \partial z }{ \partial \mathbf{a} } \frac{ \partial \mathbf{a} }{ \partial \mathbf{w} } \tag{2-2}
$$
又$z = \mathbf{a}^T \mathbf{a}$， 有：
$$
\frac{ \partial z }{ \partial a_{i} }  = \frac{ \partial \sum_{k} a_{k}^2  }{ \partial a_{i} } = 2 a_{i} \tag{2-3}
$$
故向量的形式为：
$$
\frac{ \partial z }{ \partial \mathbf{a} } = 2 \mathbf{a}^T  \tag{2-4}
$$
又由
$$
\frac{ \partial \mathbf{a}_{i} }{ \partial \mathbf{w}_{j} } = \frac{ \partial \sum_{k} x_{ik} w_{k} - y_{i} }{ \partial w_{j} } = x_{ij}  \tag{2-5}
$$
有:
$$
\frac{ \partial \mathbf{a} }{ \partial \mathbf{w} } = \mathbf{X} \tag{2-6}
$$
最终$\frac{\partial{z}}{\partial{ \mathbf{w} }}$可以写为：
$$
\frac{ \partial z }{ \partial \mathbf{w} }  =  2\mathbf{a}^T\mathbf{X} = 2 (\mathbf{Xw - y})^T\mathbf{X} \tag{2-7}

$$
事实上还需推导向量的链式求导结果为什么是(2-2)的形式。


# 自动求导

* 自动计算一个函数在指定值上的导数
* 但它有别于符号求导和数值求导：
	符号求导：
	$$
     d[4 x^3 + x^2 + 3] / dx = 12 x^2 + 2x
     $$
	数值求导：
	$$
    \frac{ \partial f(x) }{ \partial x } = \lim_{ h \to \infty } \frac{f(x+h) -f(x) }{h} 
    $$

## 自动求导实现

* 计算图
![[Pasted image 20240912230841.png|275]]
![[Pasted image 20240912231918.png|325]]
也就是说代码会构建每个操作子之间的计算图，而定义的操作子也会定义其对应的导数计算操作。那么计算这个值的导数的时候，只需将这个值带入导数的计算表达式中即可。
