(control:intro)=
# Introduction to control methods

System behavior is treated in detailed in [System Theory](system-theory:intro) section. Control theory targets a desired behavior of the system, ensuring stability and performance (in terms of desired output, error, response velocity, input effort, robustness to noise and model uncertainty,...)

```{admonition} Links
:class: tip

* [Ordinary differential equations](ode:intro)
* [System theory](system-theory:intro)


```


```{dropdown} Table of contents
:open:

* Frequency domain control of linear systems
* State estimation and observer
* Optimal control
* System identification


```

```{dropdown} Features
:open:

**Domain.**
- Frequency domain for linear systems: root locus, [Nyquist criterion](ode:lti:stability-fb:siso:nyquist) and Bode criteria,...
- Time domain: [optimal control](control:optimal), robust optimal control,...

**Full-state, partial-state feedback.**
- Full-state feedback: the complete state of the system can be observed and used for the feedback
- Partial-state feedback

**Observers**, e.g. [Kalman filter](control:observer:kalman), tries to estimate the state of a system from its output. Later, this estimatio can be used for feedback.

**Model-based/model-free control.**

```
