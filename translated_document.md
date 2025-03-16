Takeo Sasai $\circledcirc$ , 会员, IEEE, Minami Takahashi, Masanori Nakamura , 会员, IEEE, Etsushi Yamazaki , 会员, IEEE, 和 Yoshiaki Kisaka  

摘要—本文提出了一种用于光纤纵向功率分布估计（PPE）的线性最小二乘法，该方法在相干接收器中估计光纤链路中的光信号功率分布。该方法在纵向功率分布的最小二乘估计中找到全局最优解，因此其结果与真实的光功率分布紧密匹配，并能够以高空间分辨率定位链路中的损耗异常。实验结果表明，该方法实现了与光时间域反射仪（OTDR）相比，均方根误差为0.18 dB的准确PPE。因此，它成功识别出小至0.77 dB的损耗异常，展示了相干接收器在定位拼接和连接器损耗方面的潜力。该方法还在具有最佳系统光纤发射功率的波分复用（WDM）条件下进行了评估，突显了其在实际操作中的可行性。此外，稳定估计的基本限制和基于最小二乘法的PPE的空间分辨率在与PPE的病态性相关的情况下，通过评估非线性扰动矩阵的条件数进行了定量讨论。  

关键词—数字纵向监测，光纤非线性，光纤通信，纵向功率分布估计。  

## I. 引言  

表征传输链路的物理参数是减少冗余操作裕度、识别软网络故障 [2] 和构建光网络数字双胞胎 [3] 的重要任务。已经提出了多种监测方法，通过接收端 $(\operatorname{R}\mathbf{X})$ 数字信号处理（DSP）来估计链路参数，例如光信号噪声比（OSNR）、光纤非线性和色散（CD） [4]。这些基于$\operatorname{Rx}$ -DSP的方法相比于专用硬件方法更具成本效益；然而，它们通常估计整个链路的累积参数。因此，估计参数的空间分辨率通常受到限制，使得定位网络故障变得具有挑战性。如果Rx DSP能够获取分布在光纤纵向方向上的参数，则可以构建一个智能中继器，不仅能够准确预测链路的可达速率，还能够在没有专用硬件设备的情况下定位软故障，从而降低运营成本。  

在这种背景下，关于光纤链路的数字纵向监测（DLM）研究逐渐兴起 [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18]。DLM方法使用相干接收器DSP来监测沿光纤纵向分布的各种链路参数，例如信号功率分布 [5], [6], [7], [8], [9], [10], [11], [12]，跨距色散（CD）图或光纤类型 [5], [9], [10]，单个放大器的增益谱 [5], [13], [14]，单个光学滤波器的响应 [5], [11]，过度偏振依赖损耗的位置 [15], [16], [17]，以及多路径干扰 [18]。DLM的优势在于其能够表征整个多跨距链路，并在不需要专用硬件设备（如光时间域反射仪（OTDR）或光谱分析仪）的情况下定位异常链路组件。这在分散网络场景中尤为有利 [19]，因为多个供应商和领域的网络元素共存，而链路参数并不总是共享。DLM通过使用单个相干接收器端到端监测链路参数，提供了解决此问题的方案，无论来自不同供应商和领域的链路参数是否可用。事实上，该方法在 [20] 中用于演示动态光路径配置，以实现对具有未知接入域的链路的端到端连接。

%6%6%6

在DLM中监测的参数中，光纤纵向功率轮廓估计（PPE）[5]，[6]，[7]，[8]，[9]，[10]，[11]，[12] 尤其重要，因为它在估计光纤非线性干扰和定位损耗（和增益）异常方面具有实用性。PPE通过从$\mathbf{R}\mathbf{x}$信号中估计距离方向的非线性相位旋转$\gamma^{\prime}(z)=\gamma(z)P(z)$来获得光纤纵向光功率轮廓，其中$\gamma(z)$是光纤的非线性常数，$P(z)$是光纤位置$z$处的信号功率。$\gamma^{\prime}(z)$的估计可以视为非线性薛定谔方程的逆问题，其中其系数$\gamma^{\prime}(z)$是从边界条件（即$\mathrm{Tx}$和Rx信号）中估计的[6]。一般来说，解决此类逆问题的常见策略是最小二乘（LS）方法，其中参数被估计为最小化平方误差的最佳值。然而，PPE是一个非线性最小二乘问题，这使得找到全局最优解变得具有挑战性。分步法的梯度下降优化[5]，[9]是一种直接的方法，但它需要迭代优化和对各种超参数（如学习步长、迭代次数和优化器）的仔细选择；否则，估计的功率轮廓很容易陷入局部最小值，从而限制PPE的测量精度。尽管基于相关的方法（CMs）[7]，[8]，[18]可以避免迭代优化，但在[6]中已证明，CMs在无噪声和无失真条件下固有地具有有限的精度和空间分辨率。此外，CMs在没有基于硬件的校准[21]的情况下无法估计$\gamma^{\prime}(z)$的真实值。

在本文中，我们提出并实验演示了一种用于PPE的线性最小二乘法，该方法在非线性相位$\gamma^{\prime}(z)$的最小二乘估计中找到全局最优解。该方法在估计$\gamma^{\prime}(z)$的真实值时实现了高测量精度和空间分辨率。实验结果表明，所提出的方法与OTDR结果良好一致，RMS误差为$0.18\mathrm{dB}$，且无需任何校准。因此，在一个3段链路中成功定位了$0.77~\mathrm{dB}$的损耗异常，从而证明了相干接收器能够像OTDR一样定位多段链路中的劣质接头和连接器。我们首先展示了估计$\gamma^{\prime}(z)$的非线性最小二乘问题可以通过应用一阶正则扰动（RP1）模型简化为线性最小二乘问题。然后我们数值演示了通过线性最小二乘估计的功率轮廓与理论功率轮廓很好地对齐，并且即使是小至$0.2\mathrm{dB}$的损耗异常也可以被定位。此外，通过评估PPE的不适定性，定量讨论了基于LS的PPE的稳定估计的基本限制和空间分辨率。最后，我们在理想和实际配置下展示了我们的实验结果，包括有和没有波长分复用（WDM）通道的情况，以及高功率和最佳光纤发射功率的情况。

本文扩展了[12]，[22]中提出的工作，并进行了以下附加讨论：

- CMs与线性最小二乘之间的联系。
- LS在与PPE的不适定性相关的稳定估计的基本限制。
- LS的可实现空间分辨率。
- 在具有系统最佳发射功率和WDM通道的实际链路条件下的实验结果。

本文的其余部分组织如下。第二节详细介绍了问题的公式化、算法、仿真结果以及所提出的线性最小二乘法的局限性。第三节展示了在高光纤发射功率下的理想条件和在低功率及WDM条件下的实际条件下的实验结果。第四节对本文进行了总结。

%6%6%6

## II. 线性最小二乘法用于PPE  

### A. 问题表述  

PPE可以被表述为非线性薛定谔方程（NLSE）的逆问题，其中非线性系数是从边界条件重建的，即发射（Tx）和接收（Rx）信号。光信号的传播 $A\equiv A(z,t)$  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/230603d473d34de409e2712a034c48796158b551ffafe6e409f759eba2a7d24b.jpg)  
图1. 提出的线性最小二乘法用于PPE的概念。线性最小二乘估计在接收信号和参考信号之间进行，以估计纵向功率分布 $\propto\gamma^{\prime}(z)$。两个信号都用常规扰动模型进行近似。  

在光纤中，位置 $z\in[0,L]$ 和时间 $t$ 的光信号传播由NLSE控制：  

$$
\begin{array}{l}{\displaystyle\frac{\partial A}{\partial z}=\left(j\frac{\beta_{2}\left(z\right)}{2}\frac{\partial^{2}}{\partial t^{2}}+\frac{\beta_{3}\left(z\right)}{2}\frac{\partial^{3}}{\partial t^{3}}\right)A-j\gamma^{\prime}\left(z\right)\left|A\right|^{2}A,\qquad\left(1\right)}\ {\displaystyle\gamma^{\prime}\left(z\right)\equiv\gamma\left(z\right)P\left(0\right)\exp\left(-\int_{0}^{z}\alpha\left(z^{\prime}\right)d z^{\prime}\right)=\gamma\left(z\right)P\left(z\right),}\end{array}\qquad(2)
$$  

其中 $\alpha(z),\beta_{2}(z),\beta_{3}(z),\gamma(z)$ 和 $P(z)$ 分别是光纤损耗、二次/三次色散、非线性常数和位置 $z$ 处的光信号功率。注意，在此表述中，$\alpha(z)$ 被合并到非线性系数 $\gamma^{\prime}(z)$ 中，且 $A$ 的功率被归一化为1，无论位置 $z$ [5]。因此，由光纤损耗和放大引起的所有功率变化仅由 $\gamma^{\prime}(z)$ 控制。因此，可以通过估计 $\gamma^{\prime}(z)$ 来推断 $P(z)$，假设 $\gamma(z)$ 是常数。为简化起见，这里及后续仿真假设为单极化。在实验中，算法在Manakov方程的基础上扩展到双极化情况，而不是NLSE（见附录A）。  

在本工作中，$\gamma^{\prime}(z)$ 被估计为最佳非线性系数，以最佳重现接收信号。图1展示了所提方法的概念。发射信号 $\mathbf{A}[0]=[A(0,0)$ , $\dot{\mathbf{\Psi}}\cdot\dot{\mathbf{\Psi}},\dot{A}(0,n T),\mathbf{\Psi}\cdot\mathbf{\Psi}\cdot\mathbf{\Psi},A(0,(N-1)T)]^{T}$ 被发送到由NLSE控制的光纤链路（上游），并在相干接收器处演变为 $\mathbf{A}[L]$，其中 $n\in[0,N-1]$ 是时间采样编号，$T$ 是采样周期，$(\cdot)^{T}$ 表示矩阵转置，$L$ 是总距离。在另一个支路上，$\mathbf{A}[0]$ 传播一个虚拟链路，该链路在数字域中模拟光纤链路，并演变为参考信号 $\mathbf{A}^{r e f}[L]$。已经提出了几种虚拟链路模型，例如全分步法（SSM） [5], [9]、简化SSM [7], [8]、带有非线性模板的简化SSM [18] 和Volterra级数展开 [11]。在本工作中，虚拟链路由RP1建模 [23], [24]。通过这种方式，获得了对 $\gamma^{\prime}(z)$ 的估计的解析表达式。估计可以被表述为经典的最小二乘问题：  

$$
\widehat{\gamma^{\prime}}=\underset{\gamma^{\prime}}{\mathrm{argmin}}I=\underset{\gamma^{\prime}}{\mathrm{argmin}}\left\|\mathbf{A}\left[L\right]-\mathbf{A}^{r e f}\left[L\right]\right\|^{2}
$$  

其中 $\pmb{\gamma}^{\prime}=[\gamma_{0}^{\prime},\gamma_{1}^{\prime},\dots,\gamma_{K-1}^{\prime}]^{T}$，且 $\gamma_{k}^{\prime}$ 是位置 $z_{k}$ 处 $\gamma^{\prime}(z)$ 的离散化版本，$k\in\{0,\ldots,K-1\}$，因此 $z_{K-1}=L)。\mathbf{A}^{r e f}[L]$ 是经过虚拟链路传播后的模拟接收信号，并且是 $\gamma_{k}^{\prime}$ 的函数。（3）是一个非线性最小二乘问题，因为 $\gamma_{k}^{\prime}$ 出现在非线性相位旋转的指数函数中。然而，通过使用RP1，可以将其简化为线性最小二乘问题，如下一个小节所述。关键在于，在RP1中，扰动信号向量被表示为线性方程组（见（7）），这保证了（3）在解析形式（11）中表达的全局最优解。

%6%6%6

### B. 线性最小二乘法的推导  

在这里，$N{\times}1$ 向量 $\mathbf{A}[L]$ 和 $\mathbf{A}^{r e f}[L]$ 通过使用 RP1 进行建模，使得  

$$
\begin{array}{r l}&{\mathbf{A}\left[L\right]\simeq\mathbf{A}_{0}\left[L\right]+\mathbf{A}_{1}\left[L\right],}\ &{\mathbf{A}^{r e f}\left[L\right]\simeq\mathbf{A}_{0}^{r e f}\left[L\right]+\mathbf{A}_{1}^{r e f}\left[L\right],}\end{array}
$$  

其中，${\bf A}_{0}$ 和 ${\bf A}_{0}^{r e f}$ 是通过对 $\mathrm{Tx}$ 信号应用色散补偿（CD）获得的线性项，而 ${\bf A}_{1}$ 和 ${\bf A}_{1}^{r e f}$ 是一阶扰动项。请注意，以下内容中将省略 $[L]$ 以简化表达，除非另有说明。然后，成本函数 $I$ 在 (3) 中变为  

$$
\begin{array}{r l}&{I\simeq\left\Vert(\mathbf{A}_{0}+\mathbf{A}_{1})-\left(\mathbf{A}_{0}^{r e f}+\mathbf{A}_{1}^{r e f}\right)\right\Vert^{2}}\ &{=\left\Vert\mathbf{A}_{1}-\mathbf{A}_{1}^{r e f}\right\Vert^{2}}\end{array}
$$  

假设 ${\mathbf{A}}_{0}\simeq{\mathbf{A}}_{0}^{r e f}$，因为线性项 ${\bf A}_{0}$ 可以通过在数字域中应用数字滤波器进行色散补偿（CD）来很好地近似 [25], [26]。${\bf A}_{1}^{r e f}$ 在 RP1 中明确表示为：  

$$
{\bf A}_{1}^{r e f}={\bf G}\gamma^{\prime},
$$  

其中  

$$
\begin{array}{r l}&{\mathbf{G}=\left[g_{0},\ldots,g_{k},\ldots,g_{K-1}\right],}\ &{\mathbf{}}\ &{\pmb{g}_{k}=\mathbf{\mu}-j\Delta z_{k}\mathbf{D}_{z_{k}L}\tilde{\ N}\left[\mathbf{D}_{0z_{k}}\mathbf{A}\left[0\right]\right].}\end{array}
$$  

这里，$\Delta z_{k}=z_{k+1}-z_{k},\mathbf{D}_{z_{1}z_{2}}$ 是从 $z_{1}$ 到 $z_{2}$ 的色散补偿（CD）矩阵，而 $\tilde{\mathrm{~N~}}[\cdot]=(|\cdot|^{2}-2\bar{P})$ (·) 是一个具有逐元素乘法的非线性算子，其中 $\bar{P}(=1)$ 是 $\mathbf{E}$ 的功率。通过将 (7) 代入 (6)，成本函数变为  

$$
I\simeq\|\mathbf{A}_{1}-\mathbf{G}\boldsymbol{\gamma}^{\prime}\|^{2}
$$  

这可以通过线性最小二乘法来求解。考虑到 $\gamma^{\prime}$ 是一个实向量，解为（推导见附录 B）：  

$$
\widehat{\gamma^{\prime}}=\left(\mathrm{Re}\left[{\bf G}^{\dagger}{\bf G}\right]\right)^{-1}\mathrm{Re}\left[{\bf G}^{\dagger}{\bf A}_{1}\right].
$$  

这就是提出的线性最小二乘法算法。在接下来的内容中，假设空间步长是均匀的，即 $\Delta z_{k}=\Delta z$。  

备注 $I$：Kim 等人提出了一种更简单的形式 $\widehat{\gamma^{\prime\prime}}=\left(\mathbf{H}^{\dagger}\mathbf{H}\right)^{-1}\mathbf{H}^{\dagger}\mathbf{A}$，通过将矩阵 $\mathbf{G}$ 和系数向量 ${\gamma}^{\prime}$ 扩展为 $\mathrm{~\bf~H~}=[{\bf G}\mathrm{~\bf~A}_{0}]$ 和 $\gamma^{\prime\prime}=c[{\gamma^{\prime}}^{T}1]^{T}$，其中 $c$ 是一个复值缩放因子 [27], [28]。此修改确保估计的 $c$ 自动补偿参考信号 $\mathbf{A}^{r e f}$ 和 $\mathbf{R}\mathbf{x}$ 信号之间的相位不匹配，从而增强了 PPE 对链路条件的鲁棒性。

%6%6%6

### C. 与基于相关的方法的关系  

基于相关的方法被提出作为另一种PPE方法 [7], [8], [18]。在最初提出的修改CM中 [18]，并在 [6] 中详细描述，通过对发射（Tx）信号应用色散（CD）、非线性算子和残余CD，获得参考信号 $\mathbf{A}^{r e f}[L]$。注意，这个操作与公式 (9) 中的 $g_{k}$ 是相同的。然后，从这个参考信号与接收（Rx）信号之间的相关性估计 $z_{k}$ 处的功率，表示为 $\operatorname{Re}[g_{k}^{\dagger}\mathbf{A}]$。这个过程在所有位置 $z_{k}$ 上迭代，以构建功率轮廓 $\mathrm{Re}[\mathbf{G}^{\dagger}\mathbf{A}]$。在假设光纤中的信号是平稳高斯过程的前提下，结果功率轮廓在 [6] 中被解析地证明为真实功率轮廓与源于非线性空间相关性的平滑函数之间的卷积。由于这种卷积效应，CM 的空间分辨率和测量精度受到限制，如后续仿真所示。为了解决这个问题，Hahn 等人应用了对这个平滑函数的去卷积，以增强空间分辨率 [29]。  

有趣的是，CM 与本文中提出的线性最小二乘法之间有着密切的关系。根据 [6]，在高斯信号假设下，线性部分的相关性 $\mathbf{Re}[\mathbf{G}^{\dagger}\mathbf{A}_{0}]$ 为零。因此，CM 的估计功率轮廓可以简化为 Re $[\mathbf{G}^{\dagger}\mathbf{A}]=\mathrm{Re}[\mathbf{G}^{\dagger}\mathbf{A}_{1}]$。注意，这个表达式也出现在推导的线性最小二乘法 (11) 中。这表明线性最小二乘法与CM之间存在强连接，主要区别在于线性最小二乘法中存在逆矩阵 $\left(\mathbf{Re}[\mathbf{G}^{\dagger}\mathbf{G}]\right)^{-1}$ [30]。这个逆矩阵抵消了CM中的卷积效应，使得线性最小二乘法能够实现高空间分辨率和高测量精度。  

备注 2：简单去卷积与CM中应用逆矩阵有什么区别？应用去卷积是应用逆矩阵（即线性最小二乘法）的特例。如果信号满足平稳高斯假设，这些操作是一致的，因为 $\mathbf{Re}[\mathbf{G}^{\dagger}\mathbf{G}]$ 变成了一个托普利茨矩阵（即线性卷积），其逆提供了去卷积 [6]。然而，如果信号不遵循平稳高斯过程，CM 就无法再表示为卷积 [6]。相反，CM的卷积效应变得与位置相关，这不能通过简单的去卷积完全抵消。例如，在实际调制格式如QPSK和16QAM的情况下，CM在链路开始时表现出的功率弱于预期 [6], [31], [32]，如图2(a)所示，这意味着卷积效应与位置和调制格式相关。要完全消除这种与位置相关的卷积，必须应用逆矩阵。这样，CM中过于弱的功率在LS中得到了修正，这也意味着LS不显示显著的调制格式依赖性 [6]。总之，$\left(\mathbf{Re}[\mathbf{G}^{\dagger}\mathbf{G}]\right)^{-1}$ 作为一种广义的去卷积形式，适用于多种调制格式。  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/f1c7ecdcef3a481a9932445afe1b5ce0673042f099513ee56ba2fe3c275132b0.jpg)  
图2. (a) 使用提出的线性最小二乘法（红色）和相关方法（CM，蓝色）对$50\mathrm{-km}\times3$ -段链路的PPE仿真结果，插入了1.0-dB的故意衰减于$75\mathrm{km}$。 (b) 在不同衰减水平下插入损失的放大版本。使用了16QAM 128GBd信号。  

### D. 其他相关工作  

在我们的实验中，我们利用非线性自通道干扰（SCI），包括交叉极化调制（XPolM）来估计功率轮廓，如附录A所述。利用XPolM在正交极化的特殊音调之间估计纵向非线性相位和跨段CD的另一示例可以在 [33] 中找到。[34] 的作者使用WDM通道之间的交叉通道干扰（XCI）来定位损耗异常。由于干扰通道之间的较大走离，这种基于XCI的方法实现了比基于SCI的方法更高的空间分辨率。  

一种基于机器学习的方法也被用于从观察数据中识别NLSE中的光纤系数 [35]。虽然估计的系数是常数且没有纵向分布，但该技术随后被应用于预测$\mathrm{C+L}$波段的功率演变和拉曼增益谱 [36]。尽管异常检测不是他们演示的一部分，但这些方法可以用于估计光路配置的QoT。  

### E. 仿真  

生成了一个根升余弦（RRC）滚降因子为0.1的16QAM 128-GBd信号，并将其发射到$50{\cdot}\mathrm{km}$ $\times3$ -段链路中。在段的开头放置了噪声系数（NF）为$5.0~\mathrm{dB}$的集成放大器。为了模拟光纤传播，使用了分步傅里叶方法，空间步长设置为$50\textrm{m}$，过采样比为8样本/符号。光纤参数为 $\alpha=0.20$ $\mathrm{dB}/\mathrm{km}$，$\beta_{2}=-21.6~\mathrm{ps}^{2}/\mathrm{km}$，和 $\gamma=1.30\mathrm{W^{-1}k m^{-1}}$。假设为单极化传输。在下采样到两个样本/符号后，信号经历了CD补偿、同步和CD重新加载。然后计算扰动向量 $\mathbf{A}_{1}[L]$ 和非线性扰动矩阵 $\mathbf{G}$ 以执行 (11)。前者通过 ${\bf A}_{1}\left[L\right]={\bf A}\left[L\right]-{\bf A}_{0}[L]$ 获得，其中 $\mathbf{A}_{0}[L]$ 来自 $\mathbf{D}_{0L}\mathbf{A}[0]$。这个CD矩阵可以实现为 $\mathbf{D}_{z_{1}z_{2}}=$ $\mathbf{F}^{-1}\tilde{\mathbf{D}}_{z_{1}z_{2}}^{-}\mathbf{F}$，其中 $\mathbf{F}$ 是离散傅里叶矩阵，$\tilde{\mathbf{D}}_{z_{1}z_{2}}=$ $\mathrm{diag}(\exp(-\textstyle{\frac{j\beta_{2}}{2}}\omega_{0}^{2}(z_{2}-z_{1})),\ldots,\exp(-\textstyle{\frac{j\beta_{2}}{2}}\omega_{N-1}^{2}(z_{2}-\bar{z}_{1}\bar{)}))$，$\omega_{n}$ 是角频率。$\mathbf{G}$ 是通过 (8) 和 (9) 从发射信号 $\mathbf{A}[0]$ 计算的。这里，空间粒度 $\Delta z$ 均匀设置为 $0.5\mathrm{~km}$。用于PPE的样本数量为4.2$\mathrm{e}6$，功率轮廓平均50次。  

图2(a)显示了$50{\cdot}\mathrm{km}\times3$ -段链路的模拟纵向功率轮廓。在$75~\mathrm{km}$处插入了1.0-dB的衰减，每个光纤段的发射功率设置为2、4和$0~\mathrm{dBm}$，以测试估计非均匀光功率水平的能力。注意，为了清晰起见，绝对光功率 $\dot{\hat{\mathbf{P}}}=\widehat{\eta^{\prime}}/\gamma$ 显示在第一个垂直轴上，假设 $\gamma$ $(=1.30\mathrm{W}^{-1}\mathrm{km}^{-1})$ 是已知的。CM的功率轮廓 [6], [18] 也显示在图中，使用第二个垂直轴，因为CM不估计信号功率的真实值。提出的线性LS（红色）接近理论线（黑色虚线），提供了对物理链路参数的可靠估计，例如非均匀光纤发射功率、光纤损耗系数、损耗异常的位置和放大器增益。相比之下，CM（蓝色）估计的功率轮廓显示出平滑特性和有限的空间分辨率，这归因于卷积效应。尽管CM显示了信号功率变化的趋势，但估计的功率偏离了真实功率。因此，像 [21] 中提出的校准方法是CM正确估计真实物理参数所必需的。此外，尽管第一段的真实功率比第三段高2-dB，但CM在第一段的功率水平低于第三段。这种差异归因于CM在很大程度上依赖于调制格式，而LS则不，如备注2所讨论的。  

图2(b)显示了在不同衰减水平下插入损失的放大视图。提出的线性LS准确跟踪这些衰减事件，从而允许估计其水平。值得注意的是，该方法可以检测到小至 $0.2~\mathrm{dB}$ 的衰减，这是典型的接头或连接器损耗。这些发现表明线性最小二乘法不仅有潜力测试光功率水平，还可以定位和估计链路中的连接器损耗，类似于OTDR。  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/e8396bc2a31b7051943f4e14f48e585d39da9e551ddc06f2b2df07283ba8f7cc.jpg)  
图3. 对于 $\Delta z=0.25$ 和 $0.20~\mathrm{km}$ 的PPE仿真结果。过于细的空间粒度抑制了稳定的PPE。使用了16QAM 128 GBd信号和 $\beta_{2}=-21.6\mathrm{\dot{ps}}^{2}/\mathrm{km}$。未添加噪声或失真。

%6%6%6

### F. 不适定性及其限制

仿真结果证明了线性最小二乘法在PPE中的有效性。然而，其性能存在一个根本的限制。图3显示了在没有添加噪声或失真的情况下，空间粒度为$\Delta z=0.25$和$0.2~\mathrm{km}$的估计功率剖面。尽管在$\Delta z=0.25~\mathrm{km}$或更大的情况下，估计是稳定的，但在$\Delta z=0.2~\mathrm{km}$时，功率剖面崩溃，这意味着在稳定性方面存在固有的限制。这种不稳定性源于最小二乘问题（10）在更细的$\Delta z$下变得不适定。

（10）的不适定性由非线性扰动矩阵$\mathbf{G}$决定，其列$_{_{g_{k}}}$构成非线性扰动信号向量$\mathbf{A}_{1}[L]$的基。这些列是通过对Tx信号应用CD（色散补偿）这一非线性算子和残余CD生成的，如（9）所示。当这两列接近时，$\mathbf{G}$的条件数增大，从而增加了问题的不适定性。例如，当Δz较小时，$g_{k}$和$g_{k+1}$的线性独立性减弱，因为它们是通过类似的操作生成的：CD $\mathbf{D}_{0z_{k}}$和$\mathbf{D}_{0z_{k+1}}$，非线性，以及残余CD $\mathbf{D}_{z_{k}L}$和$\mathbf{D}_{z_{k+1}L}$。在这种情况下，矩阵$\mathbf{G}$具有较大的条件数，使得估计容易失败。物理理解是，在两个相邻点$z_{k}$和$z_{k+1}$处，信号波形相似，它们激发的光纤非线性（因此光功率）在$\mathbf{R}\mathbf{x}$处难以区分。同样，当CD效应（光纤CD系数或信号带宽）较小时，$\mathbf{\mathit{~\mathbf{~\mathit{~g~}~}}}_{k}$和$g_{k+1}$变得更加依赖，从而增加了不适定性。特别是在具有色散补偿光纤的色散管理（DM）链路中，估计会失败。在DM链路中，具有相反符号CD系数的光纤共存，$\mathbf{G}$中的几列完全匹配，因为链路中的多个位置共享相同的累积CD。这导致这些位置的信号波形相同，激发的非线性无法区分。在这种情况下，$\mathbf{G}$的秩降低（条件数无限大），导致最小二乘估计失败。

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/5bc97e18d29443ea38dedb12a4e73bae47cfc21dccd3fd47789d23c399781687.jpg)  
图4. 非线性扰动矩阵G的条件数作为$\frac{1}{\left|\beta_{2}\right|\mathrm{BW}^{2}\Delta z}$的函数（a）对于不同数量的空间点$K(=L/\Delta z)$，采用高斯信号格式；（b）对于不同调制格式，$K=300$点。插图（a）为$K=300$，$L=300\mathrm{km}$和$\Delta z=1~\mathrm{km}$的功率剖面。

### G. 可实现的空间分辨率

从上述讨论中，可以确定可实现的空间分辨率。图4绘制了通过改变相关参数在仿真中获得的矩阵G的条件数。根据（8）和（9），$\mathbf{G}$依赖于CD系数、链路距离$L$、Tx信号$\mathbf{A}[0]$和空间粒度$\Delta z$。因此，对以下参数的所有可能组合进行了仿真：

CD系数$\beta_{2}\in\{-1,-2,...-41\}\mathrm{ps}^{2}/\mathrm{km}$（假设$\beta_{2}\left(z\right)=c o n s t.$和$\beta_{3}\left(z\right)=0$）  
总距离$L\in\{75,300,1200\}\mathrm{km}$  
调制格式$M\in\mathrm{\{QPSK\}}$，16QAM，64QAM，PCS64QAM $\mathrm{H}=4.347$比特，编码率$=0.826$ [37]，高斯  
信号带宽$\mathrm{BW}\in\{32,64,128,256\}$ GHz  
空间粒度$\Delta z\in\{0.25,0.5,1,2\}$ km。

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/a59d126b8a1aeaa378a3116da88e7362a6e7bdbe6b8c52ce3e055a9df5a65491.jpg)  
图5. (a) 两个1.0-dB衰减相隔$500{\cdot}\mathrm{m}$的PPE仿真结果。(b) (a)的微分，用于检测和定位异常损耗事件。$\Delta z=0.25\mathrm{km}$，128-GBd信号，$\beta_{2}=-21.6~\mathrm{ps}^{2}/\mathrm{km}$。

注意，Tx信号$\mathbf{A}[0]$被整形为矩形谱（奈奎斯特极限），因此，BW等于信号符号率。此外，为了研究PPE执行时空间分辨率的下限，没有添加噪声或失真。选择横轴为$\frac{1}{\left|\beta_{2}\right|\mathrm{BW}^{2}\Delta z}$，因为空间步长中的CD效应决定了条件数，如前一小节所讨论的。图4(a)显示了在固定高斯格式的情况下，不同空间点数量$\begin{array}{r}{K=\frac{L}{\Delta z},}\end{array}$的条件数，而图4(b)则显示了在$K$固定为300的情况下，不同调制格式的条件数。我们发现所有曲线几乎形成一条唯一的线，这表明横轴$|\beta_{2}|\mathrm{BW}^{2}\Delta z$是描述不同调制格式和空间点条件数演变的有效指标。我们还发现，空间点数量$K$和调制格式对条件数有轻微影响；然而，它们在稳定估计范围内并不是决定条件数的主要因素。如插图所示，功率剖面随着条件数的增加而表现出不同的特征。PPE失败的条件数阈值约为104.3。相应地，$\beta_{2} B1W^{2}\Delta z$应满足以下不等式，以确保稳定估计：

$$
\frac{1}{\left|\beta_{2}\right|\mathrm{BW}^{2}\Delta z}<12.84
$$

在本工作中，空间分辨率（SR）被定义为可以区分两个连续功率事件的最小距离。如图5所示，至少需要三个测量点才能区分两个损耗事件，这意味着$\mathrm{SR}>2\Delta z_{l i m i t}$，其中$\Delta z_{l i m i t}$是可实现的空间粒度。因此，最小二乘法的空间分辨率下限可通过变换（12）表示为：

$$
\begin{array}{r l}&{\mathrm{SR}>\frac{0.156}{\vert\beta_{2}\vert\mathrm{BW^{2}}}}\ &{\mathrm{(对于~矩形~谱.)}}\end{array}
$$

同样，在矩形谱情况下，BW等于信号符号率。（13）表明，通过增加光纤CD系数或信号符号率，可以提高可实现的空间分辨率。例如，假设$\beta_{2}=-21.6~\mathrm{ps}^{2}/\mathrm{km}$，64-、128-和256-GBd信号的SR分别为1.76、0.44和$0.11~\mathrm{km}$。作为对（13）的验证，图5(a)显示了两个相隔$0.5\mathrm{km}$的连续1-dB损耗的功率剖面的仿真结果。$\Delta z$、符号率（$={\mathrm{BW}}$）和$\beta_{2}$分别设置为$0.25\mathrm{km}$、$128\mathrm{GBd}$和$\beta_{2}=-21.6~\mathrm{ps}^{2}/\mathrm{km}$。图5(b)是图5(a)的导数，$(\widehat{\gamma_{k}^{\prime}}-\widehat{\gamma_{k+1}^{\prime}})/\Delta z$，其峰值指示损耗事件的位置。对于线性LS，两个峰值清晰出现，区分了两个插入的损耗，空间分辨率为$0.5~\mathrm{km}$。然而，在更细的$\Delta z$（如$0.2~\mathrm{km}$，对应$\mathrm{SR}=0.4\mathrm{km}$）的情况下，功率剖面崩溃，如图3（蓝色）所示。空间分辨率与从（13）计算的值相匹配，$\mathrm{SR}>0.44\mathrm{km}$。对于CMs，仅出现一个峰值，表明空间分辨率更受限。这是由于CMs固有的卷积效应，如第II-C节所讨论的。注意，这里的仿真假设信号具有矩形谱，且$\Delta z_{k}$是均匀的。扩展到一般谱和非均匀$\Delta z_{k}$需要进一步分析。

%6%6%6

## III. 实验  

### A. 实验设置  

实验验证在两种条件下进行：(i) 理想条件下采用单通道传输，具有高光纤发射功率；(ii) 实际条件下采用波分复用（WDM），并使用最佳光纤发射功率。第一种情况是理想的，因为PPE通过利用非线性SCI来估计光功率，并且高光纤发射功率且干扰较小（即交叉信道干扰，XCI）是更可取的。  

图6显示了单通道传输的实验设置。调制格式为PCS 64QAM，滚降因子为0.1。符号速率为100 GBd。发射机的频率响应在实验前进行了估计，并在${\mathrm{Tx}}{\mathrm{DSP}}$中进行了补偿。信号由一个4通道120-GSa/s的任意波形发生器（AWG）发出，通过驱动放大器增强，并通过一个双极化IQ调制器（IQM）转换为光信号。Tx和$\operatorname{Rx}$激光器的线宽为$1\mathrm{-Hz}$，载波频率为$1547.31~\mathrm{nm}$。信号经过掺铒光纤放大器（EDFA）放大后，发射到一个$142.4\ –\mathrm{km}3$的标准单模光纤（SSMF）链路中，光纤损耗系数为$\alpha=0.180~\mathrm{dB/km}$，色散系数为$\beta_{2}=-20.26$ $\mathrm{ps}^{2}/\mathrm{km}$，非线性系数为$\gamma=1.11\mathrm{W^{-1}km^{-1}}$。光纤发射功率设置为$15\mathrm{dBm/ch}$。在$72.2~\mathrm{km}$处插入了一个可变光衰减器（VOA）以模拟光纤异常损耗。在接收端，带外放大自发辐射（ASE）噪声通过光带通滤波器（OBPF）过滤掉。光信号通过$90^{\circ}$混合器、平衡光电探测器（BPDs）和$256\mathrm{-GSa/s}$数字采样示波器（DSO）进行检测。在$\mathbf{R}\mathbf{x}$ DSP中，进行了重采样到2样本/符号、色散补偿、频率偏移（FO）补偿、极化解复用和载波相位恢复（CPR）。然后通过在CPR后重新加载补偿的色散来获得$\mathbf{A}[L]$。为了执行最小二乘估计（11），需要一个扰动向量$\mathbf{A}_{1}[L]$和一个矩阵$\mathbf{G}$。这些是从传输信号$\mathbf{A}[0]$计算得出的，如第II-E节所述。在本实验中，我们假设A[0]是已知的。然而，这并不意味着PPE需要完整的导频信号。这是因为传输信号可以通过标准解调过程在接收端恢复。在$\mathbf{R}\mathbf{x}$ DSP中的所有功能块均以2样本/符号进行处理。空间步长$\Delta z$均匀设置为$1~\mathrm{km}$。由于本实验使用了双极化传输，因此PPE算法基于Manakov方程扩展到双极化情况，如附录A所述。  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/e2cf6d179f40440644f6f4881eeb211cb7d19c9edc0d86c9ad825f4ac2fbc2c9.jpg)  
图6. 基于线性最小二乘法的纵向PPE的实验设置和DSP功能块。  

噪声的存在，如ASE噪声、相位噪声、残余频率偏移和XCI，会降低PPE的性能。然而，这些随机变化的损伤可以通过增加用于PPE的样本数量或通过平均估计的功率轮廓来减轻。有关这些平均数量的详细信息将在后续各小节中描述。  

### B. 理想条件下的实验结果  

首先，在光纤发射功率为15 $\mathrm{dBm/ch}$的单通道传输的理想条件下测试了所提出的方法。图7显示了在一个$142.4\ –\mathrm{km}3$链路上估计的纵向功率轮廓，该链路在72.2 km处插入了1.86 dB的衰减。使用了2.5e6个样本进行PPE，并对100个功率轮廓进行了平均。OTDR损耗轮廓也作为参考显示。功率轮廓重现了前一节中CM和所提出方法的仿真结果。  

尽管CM捕捉了实际功率的整体趋势，但它与OTDR结果偏离，并且难以准确定位损耗异常的位置。因此，之前的CM实验演示[7]，[8]，[15]，[21]依赖于没有任何损耗异常的正常状态参考，并监测从该参考的偏差以定位损耗事件。相比之下，线性LS的结果与OTDR结果紧密对齐；来自OTDR的均方根误差为$0.18~\mathrm{dB}$，最大绝对误差为$0.57\mathrm{dB}$。因此，插入的损耗异常在没有使用任何正常状态参考的情况下被清晰地检测到。请注意，光纤端点的$\pm1~\mathrm{km}$测量死区被排除在误差计算之外。  

为了评估可检测的损耗异常的极限，VOA水平从0.18 dB变化到0.77和1.36 dB。图8(a)展示了通过线性LS获得的60到$85\mathrm{km}$之间功率轮廓的放大视图。这些功率轮廓在所有VOA水平上与OTDR结果相匹配。值得注意的是，即使在VOA水平变化时，估计的功率轮廓也高度可重复，从60 km到$70~\mathrm{km}$的功率可以看出。为了量化可检测的极限，从功率轮廓中减去功率轮廓的倾斜（即固有光纤损耗），从而揭示异常损耗的量（图8(b)）。考虑到功率轮廓的均方根误差为$\sigma=0.18$ dB，损耗检测的阈值设定为$4\sigma$ $=4\times0.18~\mathrm{dB}=0.72$ dB。由于0.77 dB损耗异常（红色）的估计功率轮廓超过了0.72 dB的阈值，因此有效地检测并定位了该0.77 dB的损耗。此外，可以通过从阈值超出点$(74\mathrm{km})$到放大器位置（91 km）简单地平均估计损耗来估计插入的损耗。图8(c)显示了估计损耗与插入损耗的关系。共检查了100个功率轮廓（没有功率轮廓平均），估计的损耗高度稳定，标准偏差为$<0.03$ dB，最大误差为$<0.35$ dB，从而证明了对损耗异常的可靠估计。  

### C. 实际条件下的实验结果  

为了研究所提出的方法在实际条件下的性能，我们在低光纤发射功率的WDM条件下进行了额外实验。图9(a)显示了实验设置。在本实验中，Tx和Rx均使用了$10{\mathrm{-kHz}}$的线宽激光器。链路由三段$50\mathrm{-km~SSMF}$组成，WDM信道通过OBPF形状的ASE源进行模拟。测试信道（CUT）设置在$193.75\mathrm{THz}$，并在C波段的125-GHz网格上排列了20个相邻的WDM信道（图9(b)）。如图9(c)所示，系统的最佳光纤发射功率约为1.5 dBm/ch。使用8.1e5个样本计算功率轮廓，并对50个轮廓进行了平均以增强信噪比。我们以这样的方式确定这些数量，以使功率轮廓充分实现收敛。所有其他条件与之前的实验保持一致。  

图10(a)展示了在光纤发射功率为7.5和$1.5\mathrm{dBm/ch}$的WDM条件下估计的功率轮廓。  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/ec0416d11c4f614889a51c1abe4cbe0ee2b3de75f774034f720347dbbd6600de.jpg)  
图7. 在$72.2\mathrm{km}$处插入1.86 dB衰减的3段链路的PPE实验结果，采用所提出的线性最小二乘法（红色）和相关方法（CM，蓝色）。  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/ae5035784d479f9aa1037a9ac38043a32d9a299be821bb3a9f9f615fa729466d.jpg)  
图8. (a) 各种VOA水平下从60到$85\mathrm{km}$的估计功率轮廓。(b) 通过从功率轮廓中减去倾斜（即固有光纤损耗）来指示异常。损耗检测的阈值设定为$4\sigma=4\times0.18=0.72$ dB。(c) 估计损耗与插入损耗的关系（带有100个功率轮廓的误差条）。  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/65f7178d48b2facebbbefcf0e20c0e48731f793c3a50e48b32a2e04feaf1e142.jpg)  
图9. (a) WDM传输的实验设置。(b) 传输的WDM光谱。(c) 光纤发射功率的星座信噪比。系统最佳发射功率约为$1.5\mathrm{dBm/ch}$。  

%6%6%6

A VOA for loss anomaly emulation was inserted at $70\mathrm{km}$ . At a launch power of $7.5\mathrm{dBm/ch}$ , a stable PPE was observed; however, the power profiles became noisier at the system optimal launch power ( $1.5~\mathrm{dBm/ch}$ ). In particular, the estimated powers in the latter half of the spans were unstable. This instability occurs because an insufficient optical power stimulates weak nonlinearity, which is easily disrupted by link noise and distortion. The “information” of such a weak nonlinearity produced in fibers is challenging to detect at the Rx. In this experiment, the averaging effect (i.e., the number of samples used for PPE and the power-profile averaging) was sufficient to eliminate stochastic noise, such as ASE noise and XCI. Static distortions such as transceiver imperfections were therefore the primary performance-limiting factor. Power profiles at even lower launch powers will experience more degradation.  

然而，即使在 $1.5\mathrm{-dBm/ch}$ 的发射功率下，功率轮廓仍然足够清晰，可以定位到 1.2 和 2.5 dB 的衰减。图 10(b) 通过从 $1.5\mathrm{-dBm/ch}$ 的估计功率轮廓中减去倾斜来显示异常指示。考虑到这些功率轮廓与理想条件下的功率轮廓相比包含更多波动，我们建议一种替代方法来检测损耗异常，其中 $\sigma$ 被计算为损耗事件之前 OTDR 的 RMS 误差。例如，在 $70\mathrm{km}$ 处，$\sigma$ 被计算为从 51 到 $69~\mathrm{km}$ 的 RMS 误差，结果为 $0.20~\mathrm{dB}$。由于 1.2 dB 的衰减水平超过了 $4\sigma$ 阈值 $(0.80~\mathrm{dB})$，因此成功检测并定位了损耗事件。衰减水平通过从 $71\mathrm{km}$ 到 $90\mathrm{km}$ 的平均值进行估计，结果为 $1.9\mathrm{dB}$ 和 $3.6\mathrm{dB}$，分别对应于实际衰减的 $1.2\mathrm{dB}$ 和 2.5 dB。  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/faa46a0a83e6753be457437d6ecf7983699c0079cabc317bcc33098241d167c6.jpg)  
图 10. (a) 在插入各种衰减水平的 WDM 条件下估计的功率轮廓的实验结果。 (b) 通过从 $1.5\mathrm{dBm/ch}$ 的功率轮廓中减去倾斜（即固有光纤损耗）来指示异常。  

我们还发现，为了在 $70~\mathrm{km}$ 处实现 $\sigma=0.5$ dB（对应于 $2.0\mathrm{dB}$ 的损耗异常），对于发射功率为 7.5 和 $1.5\mathrm{dBm}$ 的情况，分别需要大约 5.0e4 和 4.0e5 个样本。在噪声更多的场景中，例如长途传输，需要更多的样本以维持相同的检测阈值。可以推断，随机噪声的两倍增加使得检测相同损耗异常所需的样本数量翻倍。因此，在光噪声占主导的长途系统中，OSNR 降低 $3\mathrm{dB}$ 也会使所需样本量翻倍。  

## IV. 结论  

我们提出了一种基于 Rx-DSP 的光纤纵向 PPE 的线性最小二乘法，该方法估计非线性相位的真实值 $\gamma^{\prime}(z)=\gamma(z)P(z)$。我们展示了 $\gamma^{\prime}(z)$ 的估计，通常被认为是一个非线性最小二乘问题，可以在一阶常规扰动近似下简化为一个简单的线性最小二乘问题。因此，该方法找到了最小二乘估计的全局最优解，确保了高测量精度和空间分辨率。这些特性在模拟和实验中得到了验证。  

模拟结果表明，该方法与真实功率匹配，使得能够精确估计链路中的物理参数，例如光纤发射功率水平、光纤损耗系数、损耗异常的数量和位置以及放大器增益。甚至成功定位了 0.2 dB 的损耗异常。  

我们讨论了基于最小二乘法的方法在 PPE 的病态性方面的基本性能极限。这种病态性使得 PPE 易于失败，当测试链路中的色散效应较弱时，这种趋势会加剧。通过评估非线性扰动矩阵 G 的条件数，对各种链路参数进行了定量评估。因此，所能达到的空间分辨率被证明与 $1/\beta_{2}\mathbf{B}\mathbf{W}^{2}$ 成正比。  

该方法在理想条件下通过高光纤发射功率和单通道传输进行了实验验证。对于 $50\mathrm{km}\times3$ 的链路，估计的功率轮廓达到了 $0.18~\mathrm{dB}$ 的 OTDR RMS 误差，成功定位了小至 $0.77\mathrm{dB}$ 的损耗异常，这在接头和连接器损耗中很常见。这些结果表明，PPE 在其最大性能极限下的操作与 OTDR 类似。  

此外，在实际系统最佳光纤发射功率和 WDM 通道存在的情况下，PPE 的性能也得到了研究。尽管由于光纤非线性不足，功率轮廓的信噪比随着光功率的降低而下降，但估计的轮廓仍然足够清晰，可以定位损耗异常，即使在系统最佳发射功率下。  

性能提升、长途传输下的评估以及噪声和失真的影响需要进一步研究，并构成未来研究的范围。  

### 附录 A 双极化的扩展  

在双极化的情况下，应考虑插值非线性，以正确估计 $\gamma^{\prime}(z)$ 的真实值。为此，(10) 中的最小二乘公式应基于 Manakov 方程 [38]。通过将 $\mathbf{X}-$ 和 y 极化信号向量垂直堆叠，(3) 中的代价函数变为：  

$$
I\simeq\left\Vert\left[\mathbf{A}_{x}\left[L\right]\right]-\left[\mathbf{A}_{x}^{r e f}\left[L\right]\right]\right\Vert^{2}
$$  

然后，$\mathbf{A}_{x/y}$ 和 $\mathbf{A}_{x/y}^{r e f}$ 通过使用 RP1 进行近似，例如 $\mathbf{A}_{x/y}\left[L\right]=\mathbf{A}_{0,x/y}\left[L\right]+\mathbf{A}_{1,x/y}[L]$，其中 ${\bf A}_{0,x/y}$ 是线性项，而 ${\bf A}_{1,x/y}$ 是一阶非线性项。如果我们假设 ${\bf A}_{0,x/y}$ 可以通过使用数字 CD 滤波器很好地近似为 ${\bf A}_{0,x/y}^{r e f}$，即 ${\bf A}_{0,x/y}={\bf A}_{0,x/y}^{r e f}$，那么代价函数就简化为仅比较非线性项：  

$$
I\simeq\mathbb{E}\left[\left\Vert\left[\mathbf{A}_{1,x}\left[L\right]\right]-\left[\mathbf{A}_{1,x}^{r e f}\left[L\right]\right]\right\Vert^{2}\right]
$$  

通过使用 RP1，${\bf A}_{1,x/y}^{r e f}$ 可以以矩阵形式表示，例如 ${\bf A}_{1,x}^{r e f}={\bf G}_{x}\:\gamma^{\prime}$，其中 $\boldsymbol{\gamma}^{\prime}=\left[\boldsymbol{\gamma}_{0}^{\prime},\dots,\boldsymbol{\gamma}_{K-1}^{\prime}\right]^{T}$。第 $k$ 列的 $\mathbf{G}_{x/y}$ 为  

$$
\begin{array}{r l}&{\left({\bf G}_{x/y}\right)_{k}=-j\Delta z{\bf D}_{z_{k}L}\left[\left({\bf A}_{0,x}^{\ast}\left[z_{k}\right]\odot{\bf A}_{0,x}\left[z_{k}\right]\right.\right.}\ &{\left.\left.+{\bf A}_{0,y}^{\ast}\left[z_{k}\right]\odot{\bf A}_{0,y}\left[z_{k}\right]-\frac{3}{2}\bar{P}\right)\odot{\bf A}_{0,x/y}\left[z_{k}\right]\right]}\end{array}
$$  

其中 $\odot$ 表示逐元素乘法，$\mathbf{A}_{0,x/y}\left[z_{k}\right]=\mathbf{D}_{0z_{k}}\mathbf{A}_{x/y}[0]$。代价函数可以进一步转化为  

$$
I\simeq\left\Vert\left[\mathbf{A}_{1,x}\right]-\left[\mathbf{G}_{x}\right]\boldsymbol{\gamma}^{\prime}\right\Vert^{2}.
$$  

%6%6%6

这也可以通过线性最小二乘法来解决。通过表示 $\mathbf{A}_{1}=\left[\mathbf{A}_{1,x}\right]$ 和 $\textbf{G}=\left[\mathbf{G}_{x}\right]$ = Gx ，实值解可以类似于（11）表示为：

$$
\widehat{\gamma^{\prime}}=\left(\mathrm{Re}\left[{\bf G}^{\dagger}{\bf G}\right]\right)^{-1}\mathrm{Re}\left[{\bf G}^{\dagger}{\bf A}_{1}\right].
$$

请注意，在这种情况下，光功率的估计为 $\hat{\pmb{P}}=$ ${\frac{9}{8}}{\frac{\widehat{\gamma^{\prime}}}{\gamma}}$

### 附录 B （11）的推导

代价函数（10）展开如下：

$$
I=\|\mathbf{A}_{1}\|^{2}+\gamma^{'T}\mathbf{G}^{\dagger}\mathbf{G}\gamma^{\prime}-\gamma^{'T}\mathbf{G}^{\dagger}\mathbf{A}_{1}-\mathbf{A}_{1}^{\dagger}\mathbf{G}\gamma^{\prime}.
$$

对 $\gamma^{\prime}$ 求导（19）得到：

$$
\begin{array}{r l}&{\frac{\partial I}{\partial\gamma^{\prime}}=\left(\mathbf{G}^{\dagger}\mathbf{G}+\left(\mathbf{G}^{\dagger}\mathbf{G}\right)^{T}\right)\gamma^{\prime}-\mathbf{G}^{\dagger}\mathbf{A}_{1}-\left(\mathbf{A}_{1}^{\dagger}\mathbf{G}\right)^{T}} &{=2\mathrm{Re}\left[\mathbf{G}^{\dagger}\mathbf{G}\right]\gamma^{\prime}-2\mathrm{Re}\left[\mathbf{G}^{\dagger}\mathbf{A}_{1}\right],}\end{array}
$$

其中，实向量 $\mathbf{x}$ 的公式，如 $\begin{array}{r l}{{\frac{\partial}{\partial\mathbf{x}}}\mathbf{x}^{T}\mathbf{A}\mathbf{x}}&{{}=}\end{array}$ $(\mathbf{A}+\mathbf{A}^{\mathbf{T}})\mathbf{x}$ 和 $\begin{array}{r}{\frac{\partial}{\partial\mathbf{x}}\mathbf{x}^{T}\mathbf{a}=\frac{\partial}{\partial\mathbf{x}}\mathbf{a}^{T}\mathbf{x}=\mathbf{a}}\end{array}$ ∂ aT x = a，均被使用。求解 $\begin{array}{r}{\frac{\partial I}{\partial\eta^{\prime}}=0}\end{array}$ 得到（11）。