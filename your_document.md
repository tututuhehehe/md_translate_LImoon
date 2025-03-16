
Takeo Sasai $\circledcirc$ , Member, IEEE, Minami Takahashi, Masanori Nakamura , Member, IEEE, Etsushi Yamazaki , Member, IEEE, and Yoshiaki Kisaka  

Abstract—This paper presents a linear least squares method for fiber-longitudinal power profile estimation (PPE), which estimates the optical signal power distribution throughout a fiber-optic link at a coherent receiver. The method finds the global optimum in the least squares estimation of the longitudinal power profiles; thus, its results closely match the true optical power profiles and locate loss anomalies in a link with high spatial resolution. Experimental results show that the method achieves accurate PPE with an RMS error of 0.18 dB from OTDR. Consequently, it successfully identifies a loss anomaly as small as 0.77 dB, demonstrating the potential of a coherent receiver in locating even splice and connector losses. The method is also evaluated under WDM conditions with optimal system fiber launch power, highlighting its feasibility for use in practical operations. Furthermore, the fundamental limit for stable estimation and the spatial resolution of least-squares-based PPE are quantitatively discussed in relation to the ill-posedness of the PPE by evaluating the condition number of the nonlinear perturbation matrix.  

Index Terms—Digital longitudinal monitoring, Fiber nonlinearity, Fiber-optic communication, Longitudinal power profile estimation.  

## I. INTRODUCTION  

CHARACTERIZING the physical parameters of transmission links is an essential task to reduce redundant operational margins , identify soft network failures [2], and construct digital-twins of optical networks [3]. Various monitoring methods have been proposed for estimating link parameters, such as the optical signal-to-noise ratio (OSNR), fiber nonlinearity, and chromatic dispersion (CD), by using receiver-side $(\operatorname{R}\mathbf{X})$ digital signal processing (DSP) [4]. These $\operatorname{Rx}$ -DSP-based approaches are more cost-effective compared to dedicated hardware-based approaches; however, they typically estimate cumulative parameters of the entire link. Consequently, the spatial resolution of the estimated parameters is often limited, making the pinpointing of network faults challenging. If the Rx DSP were able to obtain the parameters distributed in the fiber-longitudinal direction, an intelligent transponder could be  

built that not only accurately predicts the achievable rate of a link, but also locates soft failures without dedicated hardware devices, thereby reducing operational costs.  

Within this context, studies have emerged on digital longitudinal monitoring (DLM) of fiber-optic links [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18]. The DLM approach uses a coherent Rx DSP to monitor various link parameters longitudinally distributed along fibers, such as signal power profiles [5], [6], [7], [8], [9], [10], [11], [12], span-wise CD maps or fiber types [5], [9], [10], gain spectra of individual amplifiers [5], [13], [14], responses of individual optical filters [5], [11], locations of excessive polarization dependent loss [15], [16], [17], and multi-path interference [18]. The advantages of DLM lie in its capability of characterizing an entire multi-span link and locating anomalous link components without the need for dedicated hardware devices, such as optical time domain reflectometers (OTDR) or optical spectrum analyzers. This is particularly beneficial in disaggregated network scenarios [19], where network elements of multiple vendors and domains coexist and the link parameters are not always shared. DLM offers a solution to this issue by using a single coherent receiver to monitor the link parameters end-to-end, regardless of the availability of link parameters from different vendors and domains. In fact, this approach was used in a demonstration of dynamic optical path provisioning for an end-to-end connection over links with unknown access domains in [20].  
%6%6%6
Among the parameters monitored in DLM, the fiberlongitudinal power profile estimation (PPE) [5], [6], [7], [8], [9], [10], [11], [12] is of particular importance due to its utility in estimating fiber nonlinear interference and locating loss (and gain) anomalies. PPE obtains the fiber-longitudinal optical power profile by estimating distance-wise nonlinear phase rotations $\gamma^{\prime}(z)=\gamma(z)P(z)$ from $\mathbf{R}\mathbf{x}$ signals, where $\gamma(z)$ and $P(z)$ are the nonlinear constant of a fiber and the signal power at position $z$ on the fiber, respectively. The estimation of $\gamma^{\prime}(z)$ can be regarded as the inverse problem of the nonlinear Schrödinger equation, where its coefficient $\gamma^{\prime}(z)$ is estimated from the boundary conditions (i.e., the $\mathrm{Tx}$ and Rx signals) [6]. In general, a common strategy for solving such an inverse problem is the least squares (LS) method, where parameters are estimated as the optimum values that minimize the squared errors. However, PPE is a nonlinear least squares problem, which makes finding the global optimum challenging. Gradient descent optimization of the split-step method [5], [9] is a straightforward approach, but it requires iterative optimization and careful selection of various hyperparameters, such as the learning step size, number of iterations, and optimizer; otherwise, the estimated power profiles would easily become trapped in a local minimum, thereby limiting the measurement accuracy of PPE. Although correlation-based methods (CMs) [7], [8], [18] can avoid the iterative optimization, it has been shown in [6] that CMs inherently have limited accuracy and spatial resolution even under noiseless and distortionless conditions. Additionally, CMs do not estimate the true value of $\gamma^{\prime}(z)$ without a hardware-based calibration [21].  

In this paper, we propose and experimentally demonstrate a linear least squares method for PPE that finds the global optimum in the least squares estimation of the nonlinear phase $\gamma^{\prime}(z)$ . This method achieves high measurement accuracy and spatial resolution in estimating the true value of $\gamma^{\prime}(z)$ . Experimental results show that the proposed method achieves good agreement with OTDR results, with an RMS error of $0.18\mathrm{dB}$ without any calibration. Consequently, a loss anomaly of $0.77~\mathrm{dB}$ is successfully located in a 3-span link, thereby demonstrating that a coherent receiver can locate even poor splices and connectors in multi-span links as OTDR does. We first show that the nonlinear least squares problem of estimating $\gamma^{\prime}(z)$ can be reduced to a linear least squares problem by applying the first-order regular perturbation (RP1) model. We then numerically demonstrate that the power profiles estimated by the linear least squares align well with the theoretical power profiles, and that even a loss anomaly as small as $0.2\mathrm{dB}$ can be located. Moreover, the fundamental limit for stable estimation and the spatial resolution of the LS-based PPE are quantitatively discussed by evaluating the ill-posedness of the PPE. Finally, we present our experimental results under both ideal and practical configurations, including for situations with and without wavelength division multiplexing (WDM) channels, as well as for high and optimum fiber launch powers.  

This paper extends the work presented in [12], [22] with the following additional discussions:  

The connection between CMs and linear least squares. r The fundamental limit for stable estimation of LSs in relation to the ill-posedness of PPE. r The achievable spatial resolution of LSs. r Experimental results under practical link conditions with the system-optimal launch power and WDM channels.  

The remainder of this paper is organized as follows. Section II details the problem formulation, the algorithm, and simulation results as well as the limitations of the proposed linear least squares. Section III presents experimental results under ideal conditions with high fiber launch power and under practical conditions with low power and WDM conditions. Section IV concludes the paper.  
%6%6%6
## II. LINEAR LEAST SQUARES FOR PPE  

### A. Problem Formulation  

PPE can be formulated as an inverse problem of the nonlinear Schrödinger equation (NLSE), where the nonlinear coefficients are reconstructed from the boundary conditions, i.e., the Tx and Rx signals. The propagation of the optical signals $A\equiv A(z,t)$  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/230603d473d34de409e2712a034c48796158b551ffafe6e409f759eba2a7d24b.jpg)  
Fig. 1. Concept of the proposed linear least squares for PPE. The linear least squares estimation is performed between Rx and reference signals in order to estimate longitudinal power profile $\propto\gamma^{\prime}(z)$ . Both signals are approximated with a regular perturbation model.  

in optical fibers at position $z\in[0,L]$ and time $t$ is governed by the NLSE:  

$$
\begin{array}{l}{\displaystyle\frac{\partial A}{\partial z}=\left(j\frac{\beta_{2}\left(z\right)}{2}\frac{\partial^{2}}{\partial t^{2}}+\frac{\beta_{3}\left(z\right)}{2}\frac{\partial^{3}}{\partial t^{3}}\right)A-j\gamma^{\prime}\left(z\right)\left|A\right|^{2}A,\qquad\left(1\right)}\ {\displaystyle\gamma^{\prime}\left(z\right)\equiv\gamma\left(z\right)P\left(0\right)\exp\left(-\int_{0}^{z}\alpha\left(z^{\prime}\right)d z^{\prime}\right)=\gamma\left(z\right)P\left(z\right),}\end{array}\qquad(2)
$$  

where $\alpha(z),\beta_{2}(z),\beta_{3}(z),\gamma(z)$ , and $P(z)$ are the fiber loss, second/third dispersion, nonlinear constant, and optical signal power at $z$ , respectively. Note that, in this formulation, $\alpha(z)$ is merged into the nonlinear coefficient $\gamma^{\prime}(z)$ , and the power of $A$ is normalized to 1 regardless of the position $z$ [5]. In turn, all the power variation due to the fiber loss and amplification is governed only by $\gamma^{\prime}(z)$ . Thus, $P(z)$ can be inferred by estimating $\gamma^{\prime}(z)$ , assuming that $\gamma(z)$ is constant. For simplicity, single polarization is assumed here and in subsequent simulations. In experiments, the algorithm is extended to the dual polarization case on the basis of the Manakov equation instead of the NLSE (see Appendix A).  

In this work, $\gamma^{\prime}(z)$ is estimated as the optimal nonlinear coefficient that best reproduces the received signals. Fig. 1 shows the concept of the proposed method. The transmitted signals $\mathbf{A}[0]=[A(0,0)$ , $\dot{\mathbf{\Psi}}\cdot\dot{\mathbf{\Psi}},\dot{A}(0,n T),\mathbf{\Psi}\cdot\mathbf{\Psi}\cdot\mathbf{\Psi},A(0,(N-1)T)]^{T}$ are launched into a fiber link governed by the NLSE (upper tributary) and evolve into $\mathbf{A}[L]$ at a coherent receiver, where $n\in[0,N-1]$ is the time sample number, $T$ is the sampling period, $(\cdot)^{T}$ denotes the matrix transpose, and $L$ is the total distance. On the other tributary, $\mathbf{A}[0]$ propagates a virtual link that emulates the fiber link in the digital domain and evolves into a reference $\mathbf{A}^{r e f}[L]$ . Several models for the virtual link have been proposed, such as the full split-step method (SSM) [5], [9], simplified SSM [7], [8], simplified SSM with nonlinear template [18], and Volterra series expansion [11]. In this work, the virtual link is modeled by RP1 [23], [24]. In so doing, an analytical expression for the estimation of $\gamma^{\prime}(z)$ is obtained. The estimation can be formulated as a classical least squares problem:  

$$
\widehat{\gamma^{\prime}}=\underset{\gamma^{\prime}}{\mathrm{argmin}}I=\underset{\gamma^{\prime}}{\mathrm{argmin}}\left\|\mathbf{A}\left[L\right]-\mathbf{A}^{r e f}\left[L\right]\right\|^{2}
$$  

where $\pmb{\gamma}^{\prime}=[\gamma_{0}^{\prime},\gamma_{1}^{\prime},\dots,\gamma_{K-1}^{\prime}]^{T}$ , and $\gamma_{k}^{\prime}$ is the discretized version of $\gamma^{\prime}(z)$ at position $z_{k}$ $k\in\{0,\ldots,K-1\}$ , and thus $z_{K-1}=L).\mathbf{A}^{r e f}[L]$ is the emulated Rx signal after propagating through the virtual link and is a function of $\gamma_{k}^{\prime}$ . (3) is a nonlinear least squares problem since $\gamma_{k}^{\prime}$ appears in the exponential functions for the nonlinear phase rotations. However, it can be reduced to a linear least squares problem by using RP1, as described in the following subsection. The essence is that, in RP1, the perturbation signal vector is expressed as a linear system of equations (see (7)), which guarantees the global optimal solution of (3) expressed in an analytical form (11).  
%6%6%6
### B. Derivation of Linear Least Squares  

Here, the $N{\times}1$ vectors $\mathbf{A}[L]$ and $\mathbf{A}^{r e f}[L]$ are modelled by using RP1 such that  

$$
\begin{array}{r l}&{\mathbf{A}\left[L\right]\simeq\mathbf{A}_{0}\left[L\right]+\mathbf{A}_{1}\left[L\right],}\ &{\mathbf{A}^{r e f}\left[L\right]\simeq\mathbf{A}_{0}^{r e f}\left[L\right]+\mathbf{A}_{1}^{r e f}\left[L\right],}\end{array}
$$  

where ${\bf A}_{0}$ and ${\bf A}_{0}^{r e f}$ are the linear terms obtained by applying CD to the $\mathrm{Tx}$ signals, while ${\bf A}_{1}$ and ${\bf A}_{1}^{r e f}$ are the first-order perturbation terms. Note that, in what follows, $[L]$ will be omitted for simplicity unless specified. Then, the cost function $I$ in (3) becomes  

$$
\begin{array}{r l}&{I\simeq\left\Vert(\mathbf{A}_{0}+\mathbf{A}_{1})-\left(\mathbf{A}_{0}^{r e f}+\mathbf{A}_{1}^{r e f}\right)\right\Vert^{2}}\ &{=\left\Vert\mathbf{A}_{1}-\mathbf{A}_{1}^{r e f}\right\Vert^{2}}\end{array}
$$  

where ${\mathbf{A}}_{0}\simeq{\mathbf{A}}_{0}^{r e f}$ is assumed, since the linear term ${\bf A}_{0}$ can be well approximated in the digital domain by applying digital filters for CD [25], [26]. ${\bf A}_{1}^{r e f}$ is explicitly expressed in RP1 as:  

$$
{\bf A}_{1}^{r e f}={\bf G}\gamma^{\prime},
$$  

where  

$$
\begin{array}{r l}&{\mathbf{G}=\left[g_{0},\ldots,g_{k},\ldots,g_{K-1}\right],}\ &{\mathbf{}}\ &{\pmb{g}_{k}=\mathbf{\mu}-j\Delta z_{k}\mathbf{D}_{z_{k}L}\tilde{\ N}\left[\mathbf{D}_{0z_{k}}\mathbf{A}\left[0\right]\right].}\end{array}
$$  

Here, $\Delta z_{k}=z_{k+1}-z_{k},\mathbf{D}_{z_{1}z_{2}}$ is the matrix for CD from $z_{1}$ to $z_{2}$ , and $\tilde{\mathrm{~N~}}[\cdot]=(|\cdot|^{2}-2\bar{P})$ (·) is a nonlinear operator with element-wise multiplication, where $\bar{P}(=1)$ is the power of $\mathbf{E}$ . By substituting (7) into (6), the cost function becomes  

$$
I\simeq\|\mathbf{A}_{1}-\mathbf{G}\boldsymbol{\gamma}^{\prime}\|^{2}
$$  

This can be solved by linear least squares. Considering that $\gamma^{\prime}$ is a real vector, the solution is as follows (see Appendix B for the derivation):  

$$
\widehat{\gamma^{\prime}}=\left(\mathrm{Re}\left[{\bf G}^{\dagger}{\bf G}\right]\right)^{-1}\mathrm{Re}\left[{\bf G}^{\dagger}{\bf A}_{1}\right].
$$  

This is the proposed linear least squares algorithm. In the following, the spatial step size is assumed to be uniform, i.e., $\Delta z_{k}=\Delta z$ .  

Remark $I$ : Instead of taking the real parts as in (11), Kim et al. proposed a simpler form $\widehat{\gamma^{\prime\prime}}=\left(\mathbf{H}^{\dagger}\mathbf{H}\right)^{-1}\mathbf{H}^{\dagger}\mathbf{A}$ by augmenting the matrix $\mathbf{G}$ and coefficient vector ${\gamma}^{\prime}$ as $\mathrm{~\bf~H~}=[{\bf G}\mathrm{~\bf~A}_{0}]$ and $\gamma^{\prime\prime}=c[{\gamma^{\prime}}^{T}1]^{T}$ , where $c$ is a complex-valued scaling factor [27], [28]. This modification ensures that the estimated $c$ automatically compensates for a phase mismatch between the reference $\mathbf{A}^{r e f}$ and $\mathbf{R}\mathbf{x}$ signals after the carrier phase recovery A, thereby enhancing the robustness of PPE to the link conditions.  
%6%6%6
### C. Relation to Correlation-Based Methods  

Correlation-based methods have been proposed as another kind of PPE method [7], [8], [18]. In the modified CM originally proposed in [18] and detailed in [6], a reference $\mathbf{A}^{r e f}[L]$ is obtained by applying CD, the nonlinear operator, and residual CD to the Tx signals. Notice that this operation is the same as $g_{k}$ in (9). The power at $z_{k}$ is then estimated from the correlation between this reference and the $\operatorname{Rx}$ signals as $\operatorname{Re}[g_{k}^{\dagger}\mathbf{A}]$ . This process is iterated for all positions $z_{k}$ to construct a power profile $\mathrm{Re}[\mathbf{G}^{\dagger}\mathbf{A}]$ . Under the assumption that signals in fibers are a stationary Gaussian process, the resulting power profile was analytically shown in [6] to be a convolution between the true power profile and a smoothing function originating from the spatial correlation of the nonlinearity. Because of this convolution effect, the spatial resolution and measurement accuracy of CMs are limited, as shown in the subsequent simulation. To address this issue, Hahn et al. applied a deconvolution of this smoothing function in order to enhance the spatial resolution [29].  

Interestingly, CMs have a close relationship to the linear least squares presented in this work. According to [6], the correlation for the linear part, $\mathbf{Re}[\mathbf{G}^{\dagger}\mathbf{A}_{0}]$ , is zero under the Gaussian signal assumption. Therefore, the estimated power profile of CMs can be reduced to Re $[\mathbf{G}^{\dagger}\mathbf{A}]=\mathrm{Re}[\mathbf{G}^{\dagger}\mathbf{A}_{1}]$ . Notice that this expression also appears in the derived linear least squares (11). This suggests that there is a strong connection between the linear least squares and CMs, the primary distinction being the presence of the inverse $\left(\mathbf{Re}[\mathbf{G}^{\dagger}\mathbf{G}]\right)^{-1}$ in linear least squares [30]. This inverse matrix cancels the convolution effect in CMs, allowing the linear least squares to achieve high spatial resolution and high measurement accuracy.  

Remark 2: What is the difference between applying a simple deconvolution and the inverse matrix to CMs? Applying a deconvolution is a special case of applying the inverse matrix (i.e., linear least squares). If signals satisfy the stationary Gaussian assumption, these operations coincide, since $\mathbf{Re}[\mathbf{G}^{\dagger}\mathbf{G}]$ becomes a Toeplitz matrix (i.e., a linear convolution) and its inverse provides a deconvolution [6]. However, if signals do not follow a stationary Gaussian process, CMs can no longer be expressed as a convolution [6]. Instead, the convolution effect of CMs becomes position-dependent, which cannot be fully canceled by a simple deconvolution. For instance, in the case of practical modulation formats such as QPSK and 16QAM, CMs exhibit weaker power than expected one at the beginning of the link [6], [31], [32], as shown in Fig. 2(a), which means the convolution effect is position-dependent and modulation-format-dependent. To fully remove such a position-dependent convolution, one should apply the inverse matrix. In so doing, the excessively weak power in CMs is corrected in the LS, which also implies that the LS does not show significant modulation format dependency [6]. In summary, $\left(\mathbf{Re}[\mathbf{G}^{\dagger}\mathbf{G}]\right)^{-1}$ serves as a generalized form of deconvolution that is applicable to a wide range of modulation formats.  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/f1c7ecdcef3a481a9932445afe1b5ce0673042f099513ee56ba2fe3c275132b0.jpg)  
Fig. 2. (a) Simulation results of PPE for $50\mathrm{-km}\times3$ -span link using the proposed linear least squares (red) and correlation method (CM, blue) with 1.0-dB intentional attenuation inserted at $75\mathrm{km}$ . (b) Magnified version around inserted loss with various attenuation levels. 16QAM 128GBd signals were used.  

### D. Other Related Work  

In our experiments, we leverage nonlinear self-channel interference (SCI) including cross-polarization modulation (XPolM) to estimate the power profiles, as described in Appendix A. Another demonstration of estimating longitudinal nonlinear phases and span-wise CDs using XPolM between orthogonally polarized special tones can be found in [33]. The authors of [34] used cross-channel interference (XCI) between WDM channels to locate a loss anomaly. This XCI-based approach achieves higher spatial resolution than SCI-based methods due to a larger walk-off between interfering channels.  

A machine-learning-based method has also been used to identify the fiber coefficients in the NLSE from observation data [35]. While the estimated coefficients were constant and not longitudinally distributed, the technique was then applied to predict a power evolution and the Raman gain spectrum in the $\mathrm{C+L}$ band [36]. Even though anomaly detection was not part of their demonstrations, these approaches can be used to estimate QoT for optical path provisioning.  

### E. Simulation  

A 16QAM 128-GBd signal with a root-raised-cosine (RRC) roll-off factor of 0.1 was generated and launched into a $50{\cdot}\mathrm{km}$ $\times3$ -span link. Lumped amplifications with a noise figure (NF) of $5.0~\mathrm{dB}$ were placed at the beginning of the spans. To emulate fiber propagation, the split-step Fourier method was used with a spatial step size of $50\textrm{m}$ and an oversampling ratio of 8 samples/symbol. The fiber parameters were $\alpha=0.20$ $\mathrm{dB}/\mathrm{km}$ , $\beta_{2}=-21.6~\mathrm{ps}^{2}/\mathrm{km}$ , and $\gamma=1.30\mathrm{W^{-1}k m^{-1}}$ . A single polarization transmission was assumed. After downsampled to two samples/symbol, the signal underwent CD compensation, synchronization, and CD reloading. The perturbation vector $\mathbf{A}_{1}[L]$ and the nonlinear perturbation matrix $\mathbf{G}$ were then calculated in order to perform (11). The former was obtained from ${\bf A}_{1}\left[L\right]={\bf A}\left[L\right]-{\bf A}_{0}[L]$ , where $\mathbf{A}_{0}[L]$ comes from $\mathbf{D}_{0L}\mathbf{A}[0]$ . This CD matrix can be implemented as $\mathbf{D}_{z_{1}z_{2}}=$ $\mathbf{F}^{-1}\tilde{\mathbf{D}}_{z_{1}z_{2}}^{-}\mathbf{F}$ , where $\mathbf{F}$ is the discrete Fourier matrix, $\tilde{\mathbf{D}}_{z_{1}z_{2}}=$ $\mathrm{diag}(\exp(-\textstyle{\frac{j\beta_{2}}{2}}\omega_{0}^{2}(z_{2}-z_{1})),\ldots,\exp(-\textstyle{\frac{j\beta_{2}}{2}}\omega_{N-1}^{2}(z_{2}-\bar{z}_{1}\bar{)}))$ and $\omega_{n}$ is the angular frequency. $\mathbf{G}$ was calculated using (8) and (9) from the $\mathrm{Tx}$ signals $\mathbf{A}[0]$ . Here, the spatial granularity $\Delta z$ was uniformly set to $0.5\mathrm{~km}.4.2\mathrm{e}6$ samples were used for PPE, and the power profiles were averaged 50 times.  

Fig. 2(a) shows the simulated longitudinal power profiles for the $50{\cdot}\mathrm{km}\times3$ -span link. A 1.0-dB attenuation was inserted at $75~\mathrm{km}$ , and the launch power for each fiber span was set at 2, 4, and $0~\mathrm{dBm}$ to test the capability of estimating non-uniform optical power levels. Note that, for clarity, the absolute optical power $\dot{\hat{\mathbf{P}}}=\widehat{\eta^{\prime}}/\gamma$ is shown on the first vertical axis, assuming that $\gamma$ $(=1.30\mathrm{W}^{-1}\mathrm{km}^{-1})$ ) is known. The power profile of CM [6], [18] is also shown, for which the second vertical axis is used because CM does not estimate the true value of the signal power. The proposed linear LS (red) is close to the theoretical line (black dashed), providing a reliable estimation of physical link parameters, such as non-uniform fiber launch powers, fiber loss coefficients, the locations of loss anomalies, and amplifier gains. In contrast, the power profile estimated by CM (blue) shows a smoothed characteristic and limited spatial resolution due to the convolution effect. Although CM shows the tendency of the signal power variation, the estimated power deviates from the true power. Consequently, calibration methods, like those proposed in [21], are required for CM to correctly estimate the true physical parameters. Furthermore, CM exhibits a lower power level in the first span than in the third span despite that the true power in the first span is 2-dB higher than in the third span. A similar observation can be found in [32]. This discrepancy is attributed to the fact that CM is largely dependent on the modulation format, while LS is not, as discussed in Remark 2.  

Fig. 2(b) shows a magnified view around an inserted loss with various attenuation levels. The proposed linear LS accurately tracks these attenuation events, thus allowing their levels to be estimated. Notably, the method can detect an attenuation as tiny as $0.2~\mathrm{dB}$ , which is a typical splice or connector loss. These findings illustrate that linear least squares has the potential not only to test optical power levels but also to locate and estimate connector losses in a link, similar to OTDR.  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/e8396bc2a31b7051943f4e14f48e585d39da9e551ddc06f2b2df07283ba8f7cc.jpg)  
Fig. 3. Simulation results of PPE for $\Delta z=0.25$ and $0.20~\mathrm{km}$ . Excessively fine spatial granularity inhibits stable PPE. 16QAM 128 GBd signals and $\beta_{2}=-21.6\mathrm{\dot{ps}}^{2}/\mathrm{km}$ were used. No noise or distortion was added.  
%6%6%6
### F. Ill-Posedness and Limitations  

The simulation results demonstrate the effectiveness of the linear least squares for PPE. However, there exists a fundamental limit on its performance. Fig. 3 shows estimated power profiles with spatial granularities of $\Delta z=0.25$ and $0.2~\mathrm{km}$ , with no noise or distortion added. Although the estimation was stable at $\Delta z=0.25~\mathrm{km}$ or larger, the power profile collapsed at $\Delta z=0.2~\mathrm{km}$ , implying that there is an inherent limitation regarding stability. This instability arises because the least squares problem (10) becomes ill-posed with a finer $\Delta z$ .  

The ill-posedness of (10) is determined by the nonlinear perturbation matrix $\mathbf{G}$ , whose columns $_{_{g_{k}}}$ form a basis for the nonlinear perturbed signal vector $\mathbf{A}_{1}[L]$ . These columns are created by applying CD, the nonlinear operator, and residual CD to the Tx signals as shown in (9). When two of these columns are close to one another, the condition number of $\mathbf{G}$ grows, increasing the ill-posedness of the problem. For instance, when Δz is small, the linear independence of gk and gk+1 is weakened because they are generated by similar operations: CD $\mathbf{D}_{0z_{k}}$ and $\mathbf{D}_{0z_{k+1}}$ , the nonlinearity, and residual CD $\mathbf{D}_{z_{k}L}$ and $\mathbf{D}_{z_{k+1}L}$ . In such a scenario, the matrix $\mathbf{G}$ possesses a large condition number, making the estimation prone to failure. The physical understanding is that signal waveforms at two closely positioned points $z_{k}$ and $z_{k+1}$ are similar, and the fiber nonlinearities they excite (and thus the optical power) are difficult to distinguish at the $\mathbf{R}\mathbf{x}$ . Similarly, when the CD effect (fiber CD coefficients or signal bandwidth) is small, $\mathbf{\mathit{~\mathbf{~\mathit{~g~}~}}}_{k}$ and $g_{k+1}$ become more dependent, increasing the ill-posedness. In particular, the estimation fails in a dispersion managed (DM) link with dispersion compensating fibers. In a DM link, fibers with opposite-sign CD coefficients coexist, and several columns in G completely match because multiple positions in a link share the same accumulated CD. This leads to identical signal waveforms at these positions, and the excited nonlinearities cannot be distinguished. In such cases, the rank of $\mathbf{G}$ is reduced (the condition number is infinitely large), leading to failure of the least squares estimation.  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/5bc97e18d29443ea38dedb12a4e73bae47cfc21dccd3fd47789d23c399781687.jpg)  
Fig. 4. Condition number of nonlinear perturbation matrix G as function of $\frac{1}{\left|\beta_{2}\right|\mathrm{BW}^{2}\Delta z}$ (a) for various numbers of spatial points $K(=L/\Delta z)$ for a Gaussian signal format and (b) for various modulation formats with $K=300$ points. Insets in (a) are power profiles for $K=300$ $L=300\mathrm{km}$ and $\Delta z=1~\mathrm{km}$ ).  

### G. Achievable Spatial Resolution  

From the discussion above, the achievable spatial resolution can be determined. Fig. 4 plots the condition numbers of the matrix G obtained in simulations by varying related parameters. According to (8) and (9), $\mathbf{G}$ is dependent on the CD coefficients, link distance $L$ , Tx signal $\mathbf{A}[0]$ , and spatial granularity $\Delta z$ . Therefore, simulations were conducted on all possible combinations of the following parameters:  

CD coefficients $\beta_{2}\in\{-1,-2,...-41\}\mathrm{ps}^{2}/\mathrm{km}$ $(\beta_{2}\left(z\right)=c o n s t.$ . and $\beta_{3}$ $(z)=0$ were assumed) r Total distance $L\in\{75,300,1200\}\mathrm{km}$ 1 r Modulation format $M\in\mathrm{\{QPSK\}}$ , 16QAM, 64QAM, PCS64QAM $\mathrm{H}=4.347$ bits, code rate $=0.826$ [37]), Gaussian} r Signal bandwidth $\mathrm{BW}\in\{32,64,128,256\}$ GHz r Spatial granularity $\Delta z\in\{0.25,0.5,1,2\}$ km.  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/a59d126b8a1aeaa378a3116da88e7362a6e7bdbe6b8c52ce3e055a9df5a65491.jpg)  
Fig. 5. (a) Simulation results of PPE with two 1.0-dB attenuations located $500{\cdot}\mathrm{m}$ apart. (b) Differentiation of (a) for detection and localization of anomaly loss events. $\Delta z=0.25\mathrm{km}$ , 128-GBd signals, $\beta_{2}=-21.6~\mathrm{ps}^{2}/\mathrm{km}$ .  

Note that the Tx signal $\mathbf{A}[0]$ was shaped into a rectangular spectrum (the Nyquist limit), and thus, BW is equal to the signal symbol rate. Also, no noise or distortion was added in order to investigate a lower bound of the spatial resolution when PPE (insets in Fig. 4) was performed. The horizontal axis was chosen to be $\frac{1}{\left|\beta_{2}\right|\mathrm{BW}^{2}\Delta z}$ because the CD effect in the spatial step determines the condition number, as discussed in the previous subsection. Fig. 4(a) shows the condition number for various numbers of spatial points $\begin{array}{r}{K=\frac{L}{\Delta z},}\end{array}$ ) with the modulation format fixed to the Gaussian format, while Fig. 4(b) shows it for various modulation formats with $K$ fixed to 300. We found that all the curves almost form a unique line, which suggests that the horizontal axis |β2|BW2Δz is an effective metric to describe the evolution of the condition number across various modulation formats and spatial points. We also found that the number of spatial points $K$ and the modulation format slightly affect the condition number; however, they are not primary factors in determining the condition number within the range of stable estimation. As shown in the insets, the power profiles exhibit divergent characteristics as the condition number grows. The threshold of the condition number beyond which the PPE fails was approximately 104.3. Correspondingly, β2 B1W2Δz should satisfy the following inequality to ensure stable estimation:  

$$
\frac{1}{\left|\beta_{2}\right|\mathrm{BW}^{2}\Delta z}<12.84
$$  

In this work, the spatial resolution, denoted as SR, is defined as the minimal distance over which two consecutive power events can be distinguished. As shown in Fig. 5, at least three measurement points are required to distinguish two loss events, which implies that $\mathrm{SR}>2\Delta z_{l i m i t}$ with $\Delta z_{l i m i t}$ the achievable spatial granularity. Consequently, the lower bound of the spatial resolution of LS is expressed by transforming (12) as follows:  

$$
\begin{array}{r l}&{\mathrm{SR}>\frac{0.156}{\vert\beta_{2}\vert\mathrm{BW^{2}}}}\ &{\mathrm{(for~rectangular~spectrum.)}}\end{array}
$$  

Again, BW is equivalent to the signal symbol rate in the rectangular spectrum case. (13) implies that the achievable spatial resolution is improved by increasing the fiber CD coefficients or the signal symbol rate. For instance, SRs of 1.76, 0.44, and $0.11~\mathrm{km}$ are achieved for 64-, 128-, and 256-GBd signals, respectively, assuming $\beta_{2}=-21.6~\mathrm{ps}^{2}/\mathrm{km}$ . As a verification of (13), Fig. 5(a) shows the simulation results for power profiles with two consecutive 1-dB losses inserted $0.5\mathrm{km}$ apart. $\Delta z$ , the symbol rate $(={\mathrm{BW}})$ , and $\beta_{2}$ were set to $0.25\mathrm{km}$ , $128\mathrm{GBd}$ , and $\beta_{2}=-21.6~\mathrm{ps}^{2}/\mathrm{km}$ , respectively. Fig. 5(b) is the derivative of Fig. 5(a), $(\widehat{\gamma_{k}^{\prime}}-\widehat{\gamma_{k+1}^{\prime}})/\Delta z$ , whose peaks indicate the locations of the loss e
vents. For the linear LS, two peaks clearly appear, distinguishing two inserted losses with a spatial resolution of $0.5~\mathrm{km}$ . However, in the case of a finer $\Delta z$ such as $0.2~\mathrm{km}$ (corresponding $\mathrm{SR}=0.4\mathrm{km}$ ), the power profile collapses like in Fig. 3(blue). The spatial resolution matches the value calculated from (13), $\mathrm{SR}>0.44\mathrm{km}$ . For CMs, only a single peak appeared, indicating the spatial resolution is more limited. This is due to the convolution effect inherent in CMs, as discussed in Section II-C. Note that the simulation here assumed that the signal had a rectangular spectrum and $\Delta z_{k}$ was uniform. The extension to general spectra and non-uniform $\Delta z_{k}$ requires further analysis.  
%6%6%6
## III. EXPERIMENT  

### A. Experimental Setup  

The experimental verification was conducted under two conditions: (i) an ideal condition employing a single-channel transmission with high fiber launch power and (ii) practical conditions employing WDM with the optimal fiber launch power. The first scenario is ideal because PPE estimates the optical power by leveraging nonlinear SCI, and a high fiber launch power with less disturbance (i.e., cross channel interference, XCI) is preferred.  

Fig. 6 shows the experimental setup for the single-channel transmission. The modulation format was PCS 64QAM with a roll-off factor of 0.1. The symbol rate was 100 GBd. The frequency response of the transmitter was estimated in advance and compensated for in the ${\mathrm{Tx}}{\mathrm{DSP}}.$ The signal was emitted from a 4-ch 120-GSa/s arbitrary waveform generator (AWG), boosted by driver amplifiers and converted into optical signals with a dual-polarization IQ-modulator (IQM). Tx and $\operatorname{Rx}$ lasers had a $1\mathrm{-Hz}$ linewidth with a carrier frequency of $1547.31~\mathrm{nm}$ . After being amplified by an erbium-doped fiber amplifier (EDFA), the signal was launched into a $142.4\ –\mathrm{km}3$ -span standard singlemode fiber (SSMF) link with $\alpha=0.180~\mathrm{dB/km}$ , $\beta_{2}=-20.26$ $\mathrm{ps}^{2}/\mathrm{km}$ , and $\gamma=1.11\mathrm{W^{-1}k m^{-1}}$ . The fiber launch power was set to $15\mathrm{dBm/ch}$ . A variable optical attenuator (VOA) was inserted at $72.2~\mathrm{km}$ to emulate the fiber anomaly loss. At the receiver side, out-of-band amplified spontaneous emission (ASE) noise was filtered out by an optical bandpass filter (OBPF). The optical signals were detected by a $90^{\circ}$ hybrid, balanced photodetectors (BPDs), and a $256\mathrm{-GSa/s}$ digital sampling oscilloscope (DSO). In $\mathbf{R}\mathbf{x}$ DSP, resampling to 2 samples/symbol, CD compensation, frequency offset (FO) compensation, polarization demultiplexing, and carrier phase recovery (CPR) were applied. $\mathbf{A}[L]$ was then obtained by reloading the compensated CD after CPR. To perform the least squares estimation (11), a perturbation vector $\mathbf{A}_{1}[L]$ and a matrix $\mathbf{G}$ are required. These were computed from the transmitted signals $\mathbf{A}[0]$ , as described in Section II-E. In this experiment, we assumed that A[0] were known a priori. However, this does not mean that the PPE requires full pilot signals. This is because the transmitted signals can be recovered at the Rx through the standard demodulation process. All the function blocks in the $\mathbf{R}\mathbf{x}$ DSP were conducted at 2 samples/symbol. The spatial step size $\Delta z$ was uniformly set to $1~\mathrm{km}$ . Since this experiment used a dual-polarization transmission, the PPE algorithm was extended to the dual polarization case based on the Manakov equation, as described in Appendix A.  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/e2cf6d179f40440644f6f4881eeb211cb7d19c9edc0d86c9ad825f4ac2fbc2c9.jpg)  
Fig. 6. Experimental setup and DSP-function blocks for linear-least-squares based longitudinal PPE.  

The presence of noise, such as ASE noise, phase noise, the residual frequency offset, and XCI, degrades the performance of PPE. However, such stochastically varying impairments can be mitigated by increasing the number of samples used for PPE or by averaging the estimated power profiles. Details on these averaging numbers are described in each of the subsequent subsections.  

### B. Experimental Results Under Ideal Condition  

First, the proposed method was tested in an ideal condition of a single-channel transmission with a fiber launch power of 15 $\mathrm{dBm/ch}$ . Fig. 7 shows the estimated longitudinal power profile over a $142.4\ –\mathrm{km}3$ -span link with a 1.86-dB attenuation inserted at 72.2 km. 2.5e6 samples were used for PPE and 100 power profiles were averaged. OTDR loss profiles are also shown for reference. The power profiles reproduced the simulation results in the previous section for both the CM and proposed method.  

Although the CM captures the overall trend of the actual power, it deviates from the OTDR results and struggles to pinpoint the position of the loss anomaly. Thus, previous experimental demonstrations of CM [7], [8], [15], [21] relied on a normal state reference without any loss anomaly and monitored the deviations from this reference to locate loss events. In contrast, the results of the linear LS align closely with the OTDR results; the RMS error from OTDR is $0.18~\mathrm{dB}$ and the maximum absolute error is $0.57\mathrm{dB}$ . Consequently, the inserted loss anomaly was clearly detected without using any normal state reference. Note that measurement dead zones of $\pm1~\mathrm{km}$ from the fiber ends were excluded from the error calculation.  

To evaluate the detectable limit of the loss anomalies, the VOA level was varied from 0.18 to 0.77 and 1.36 dB. Fig. 8(a) presents a magnified view of the power profiles between 60 and $85\mathrm{km}$ , obtained by the linear LS. These power profiles matched the OTDR results across all VOA levels. Notably, the estimated power profiles were highly reproducible even when the VOA levels were varied, as can be seen from the powers from 60 km to $70~\mathrm{km}$ . To quantify the detectable limit, the tilts of the power profiles (i.e., inherent fiber losses) were subtracted from the power profiles, thereby revealing the amount of anomaly loss (Fig. 8(b)). Considering that the RMS error of the power profiles was $\sigma=0.18$ dB, the threshold for loss detection was set to $4\sigma$ $=4\times0.18~\mathrm{dB}=0.72$ dB. As the estimated power profile for a 0.77-dB loss anomaly (red) surpasses the 0.72-dB threshold, this 0.77-dB loss was effectively detected and localized. In addition, the amount of inserted loss can be estimated from Fig. 8(b) simply by averaging the estimated losses from the threshold-exceeding point $(74\mathrm{km})$ to the amplifier location (91 km). Fig. 8(c) shows the estimated loss as a function of the inserted loss. A total of 100 power profiles (without power profile averaging) were examined, and the estimated losses were highly stable with a standard deviation of $<0.03$ dB and a maximum error of $<0.35$ dB, thereby demonstrating a reliable estimation of loss anomalies.  

### C. Experimental Results Under Practical Conditions  

To investigate the performance of the proposed method under practical conditions, we conducted an additional experiment under WDM conditions with low fiber launch power. Fig. 9(a) shows the experimental setup. In this experiment, lasers with a $10{\mathrm{-kHz}}$ linewidth were used for both Tx and Rx. The link comprised three spans of $50\mathrm{-km~SSMF}$ , and WDM channels were emulated using an ASE source shaped by OBPFs. The channel under test (CUT) was set at $193.75\mathrm{THz}$ , and 20 adjacent WDM channels were arranged on a 125-GHz grid in the C band (Fig. 9(b)). As shown in Fig. 9(c), the optimal fiber launch power for the system was approximately 1.5 dBm/ch. 8.1e5 samples were used to compute the power profiles, and 50 profiles were averaged to enhance the SNR. We determined these quantities in such a way that the power profiles sufficiently achieved convergence. All other conditions remained consistent with the previous experiment.  

Fig. 10(a) presents the estimated power profiles under the WDM condition for fiber launch powers of 7.5 and $1.5\mathrm{dBm/ch}$ .  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/ec0416d11c4f614889a51c1abe4cbe0ee2b3de75f774034f720347dbbd6600de.jpg)  
Fig. 7. Experimental results of PPE with proposed linear least squares (red) and correlation method (CM, blue) for 3-span link with 1.86-dB attenuation inserted at $72.2\mathrm{km}$ .  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/ae5035784d479f9aa1037a9ac38043a32d9a299be821bb3a9f9f615fa729466d.jpg)  
Fig. 8. (a) Estimated power profiles from 60 to $85\mathrm{km}$ for various VOA levels. (b) Anomaly indication by subtracting tilt (i.e., inherent fiber loss) from the power profiles. Threshold for loss detection was set to $4\sigma=4\times0.18=0.72$ dB. (c) Estimated loss as a function of inserted loss (error bars with 100 power profiles).  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/65f7178d48b2facebbbefcf0e20c0e48731f793c3a50e48b32a2e04feaf1e142.jpg)  
Fig. 9. (a) Experimental setup for WDM transmission. (b) Transmitted WDM spectra. (c) Constellation SNR as a function of fiber launch power. System optimal launch power was approximately $1.5\mathrm{dBm/ch}$ .  
%6%6%6
A VOA for loss anomaly emulation was inserted at $70\mathrm{km}$ . At a launch power of $7.5\mathrm{dBm/ch}$ , a stable PPE was observed; however, the power profiles became noisier at the system optimal launch power ( $1.5~\mathrm{dBm/ch}$ ). In particular, the estimated powers in the latter half of the spans were unstable. This instability occurs because an insufficient optical power stimulates weak nonlinearity, which is easily disrupted by link noise and distortion. The “information” of such a weak nonlinearity produced in fibers is challenging to detect at the Rx. In this experiment, the averaging effect (i.e., the number of samples used for PPE and the power-profile averaging) was sufficient to eliminate stochastic noise, such as ASE noise and XCI. Static distortions such as transceiver imperfections were therefore the primary performance-limiting factor. Power profiles at even lower launch powers will experience more degradation.  

Nevertheless, the power profiles were still clear enough to locate the 1.2- and 2.5-dB attenuations, even at a launch power of $1.5\mathrm{-dBm/ch}$ . Fig. 10(b) shows an anomaly indication by subtracting tilts from the estimated power profiles at $1.5\mathrm{-dBm/ch}$ . Given that these power profiles contain more fluctuations compared with those under ideal conditions, we suggest an alternative method for detecting loss anomalies, where $\sigma$ is calculated as the RMS error from OTDR over locations prior to a loss event. For instance, $\sigma$ at $70\mathrm{km}$ was calculated as the RMS error from 51 to $69~\mathrm{km}$ and was found to be $0.20~\mathrm{dB}$ . Since the 1.2-dB attenuation level exceeded the $4\sigma$ threshold $(0.80~\mathrm{dB})$ , the loss event was successfully detected and located. The attenuation levels were estimated by taking the average from $71\mathrm{km}$ to $90\mathrm{km}$ , which resulted in $1.9\mathrm{dB}$ and $3.6\mathrm{dB}$ for the actual attenuations of $1.2\mathrm{dB}$ and 2.5 dB, respectively.  

![](https://cdn-mineru.openxlab.org.cn/extract/97d8a841-96e1-4991-95c3-f00c05b3f499/faa46a0a83e6753be457437d6ecf7983699c0079cabc317bcc33098241d167c6.jpg)  
Fig. 10. (a) Experimental results of estimated power profiles under WDM conditions with various attenuation levels inserted. (b) Anomaly indication by subtracting tilt (i.e., inherent fiber loss) from power profiles at launch power of $1.5\mathrm{dBm/ch}$ .  

We also found that to achieve $\sigma=0.5$ dB (corresponding to a loss anomaly of $2.0\mathrm{dB}.$ ) at $70~\mathrm{km}$ , approximately 5.0e4 and 4.0e5 samples in total were required for launch powers of 7.5 and $1.5\mathrm{dBm}$ , respectively. In scenarios with more noise, such as long-haul transmissions, a greater number of samples will be needed to maintain the same detection threshold. It can be inferred that a two-fold increase in stochastic noise doubles the samples required to detect the same loss anomaly. Therefore, in long-haul systems where optical noise is dominant, an OSNR reduction of $3\mathrm{dB}$ also doubles the required sample size.  

## IV. CONCLUSION  

We presented a linear least squares method for Rx-DSP-based fiber-longitudinal PPE, which estimates the true value of the nonlinear phase $\gamma^{\prime}(z)=\gamma(z)P(z)$ . We showed that the estimation of $\gamma^{\prime}(z)$ , which is typically considered a nonlinear least-square problem, can be reduced to a simple linear least-square problem under the first-order regular perturbation approximation. As a result, this method finds the global optimum of the least squares estimation, ensuring high measurement accuracy and spatial resolution. These characteristics were validated in both simulations and experiments.  

The simulations revealed that the method matches true power, which enables a precise estimation of physical parameters throughout a link, such as fiber launch power level, fiber loss coefficient, the amount and locations of loss anomalies, and amplifier gains. Even a 0.2-dB loss anomaly was successfully located.  

We discussed the fundamental performance limit of the leastsquares-based method in terms of the ill-posedness of the PPE. This ill-posedness, making PPE prone to failure, intensifies when the CD effect in a tested link is weak. This tendency was quantitatively evaluated by assessing the condition number of the nonlinear perturbation matrix G for various link parameters. Consequently, the achievable spatial resolution was shown to be proportional to $1/\beta_{2}\mathbf{B}\mathbf{W}^{2}$ .  

The method was experimentally validated under ideal conditions with a high fiber launch power and single-channel transmission. The estimated power profiles for $50\mathrm{km}\times3$ spans achieved an RMS error from OTDR of $0.18~\mathrm{dB}$ , successfully locating a loss anomaly as tiny as $0.77\mathrm{dB}$ , common in splice and connector losses. These results demonstrate that PPE operates similarly to OTDR at its maximum performance limit.  

Furthermore, the performance of PPE was investigated under practical system-optimal fiber launch power and the presence of WDM channels. Although the SNR of the power profiles decreases with a reduction in optical power due to insufficient fiber nonlinearity, the estimated profiles were still clear enough to locate loss anomalies even with system-optimal launch powers.  

The performance enhancement, an evaluation under long-haul transmissions, and the impact of noise and distortion require further studies and constitute the scope of future research.  

### APPENDIX A EXTENSION TO DUAL POLARIZATION  

In the case of dual polarization, one should consider interpolarization nonlinearity to correctly estimate the true value of $\gamma^{\prime}(z)$ . To do so, the least squares formulation in (10) should be based on the Manakov equation [38]. By vertically stacking the $\mathbf{X}-$ and y-polarization signal vectors, the cost function in (3) becomes:  

$$
I\simeq\left\Vert\left[\mathbf{A}_{x}\left[L\right]\right]-\left[\mathbf{A}_{x}^{r e f}\left[L\right]\right]\right\Vert^{2}
$$  

Then, both $\mathbf{A}_{x/y}$ and $\mathbf{A}_{x/y}^{r e f}$ are approximated by using RP1 such as $\mathbf{A}_{x/y}\left[L\right]=\mathbf{A}_{0,x/y}\left[L\right]+\mathbf{A}_{1,x/y}[L]$ , where ${\bf A}_{0,x/y}$ is a linear term, and ${\bf A}_{1,x/y}$ is a first-order nonlinear term. If we assume that ${\bf A}_{0,x/y}$ is well approximated by ${\bf A}_{0,x/y}^{r e f}$ using digital CD filters, ${\bf A}_{0,x/y}={\bf A}_{0,x/y}^{r e f}$ holds; then, the cost function is reduced to a comparison of the nonlinear terms only:  

$$
I\simeq\mathbb{E}\left[\left\Vert\left[\mathbf{A}_{1,x}\left[L\right]\right]-\left[\mathbf{A}_{1,x}^{r e f}\left[L\right]\right]\right\Vert^{2}\right]
$$  

By using RP1, ${\bf A}_{1,x/y}^{r e f}$ can be expressed in a matrix form such as ${\bf A}_{1,x}^{r e f}={\bf G}_{x}\:\gamma^{\prime}$ , where $\boldsymbol{\gamma}^{\prime}=\left[\boldsymbol{\gamma}_{0}^{\prime},\dots,\boldsymbol{\gamma}_{K-1}^{\prime}\right]^{T}$ . The $k$ -th  

column of $\mathbf{G}_{x/y}$ is  

$$
\begin{array}{r l}&{\left({\bf G}_{x/y}\right)_{k}=-j\Delta z{\bf D}_{z_{k}L}\left[\left({\bf A}_{0,x}^{\ast}\left[z_{k}\right]\odot{\bf A}_{0,x}\left[z_{k}\right]\right.\right.}\ &{\left.\left.+{\bf A}_{0,y}^{\ast}\left[z_{k}\right]\odot{\bf A}_{0,y}\left[z_{k}\right]-\frac{3}{2}\bar{P}\right)\odot{\bf A}_{0,x/y}\left[z_{k}\right]\right]}\end{array}
$$  

where $\odot$ denotes element-wise multiplication, and $\mathbf{A}_{0,x/y}\left[z_{k}\right]=\mathbf{D}_{0z_{k}}\mathbf{A}_{x/y}[0]$ . The cost function can further be transformed to  

$$
I\simeq\left\Vert\left[\mathbf{A}_{1,x}\right]-\left[\mathbf{G}_{x}\right]\boldsymbol{\gamma}^{\prime}\right\Vert^{2}.
$$  
%6%6%6
This can also be solved by linear least squares. By denoting $\mathbf{A}_{1}=\left[\mathbf{A}_{1,x}\right]$ and $\textbf{G}=\left[\mathbf{G}_{x}\right]$ = Gx , the real-valued solution is expressed similarly as (11):  

$$
\widehat{\gamma^{\prime}}=\left(\mathrm{Re}\left[{\bf G}^{\dagger}{\bf G}\right]\right)^{-1}\mathrm{Re}\left[{\bf G}^{\dagger}{\bf A}_{1}\right].
$$  

Note that, in this case, optical powers are estimated as $\hat{\pmb{P}}=$ ${\frac{9}{8}}{\frac{\widehat{\gamma^{\prime}}}{\gamma}}$  

### APPENDIX B DERIVATION OF (11)  

The cost function (10) is expanded as follows:  

$$
I=\|\mathbf{A}_{1}\|^{2}+\gamma^{'T}\mathbf{G}^{\dagger}\mathbf{G}\gamma^{\prime}-\gamma^{'T}\mathbf{G}^{\dagger}\mathbf{A}_{1}-\mathbf{A}_{1}^{\dagger}\mathbf{G}\gamma^{\prime}.
$$  

Differentiating (19) with respect to $\gamma^{\prime}$ yields  

$$
\begin{array}{r l}&{\frac{\partial I}{\partial\gamma^{\prime}}=\left(\mathbf{G}^{\dagger}\mathbf{G}+\left(\mathbf{G}^{\dagger}\mathbf{G}\right)^{T}\right)\gamma^{\prime}-\mathbf{G}^{\dagger}\mathbf{A}_{1}-\left(\mathbf{A}_{1}^{\dagger}\mathbf{G}\right)^{T}}\ &{=2\mathrm{Re}\left[\mathbf{G}^{\dagger}\mathbf{G}\right]\gamma^{\prime}-2\mathrm{Re}\left[\mathbf{G}^{\dagger}\mathbf{A}_{1}\right],}\end{array}
$$  

where formulas for a real vector $\mathbf{x}$ , such as $\begin{array}{r l}{{\frac{\partial}{\partial\mathbf{x}}}\mathbf{x}^{T}\mathbf{A}\mathbf{x}}&{{}=}\end{array}$ $(\mathbf{A}+\mathbf{A}^{\mathbf{T}})\mathbf{x}$ and $\begin{array}{r}{\frac{\partial}{\partial\mathbf{x}}\mathbf{x}^{T}\mathbf{a}=\frac{\partial}{\partial\mathbf{x}}\mathbf{a}^{T}\mathbf{x}=\mathbf{a}}\end{array}$ ∂ aT x = a, are used. Solving $\begin{array}{r}{\frac{\partial I}{\partial\eta^{\prime}}=0}\end{array}$ gives (11).  