(control:optimal)=
# Optimal control

* Deterministic/stochastic signals
* Full-state feedback, observer and full-state on observed state, output feedback

**Deterministic signals.**
* [Full-state feedback](control:optimal:full-state-fb), $\mathbf{u} = - \mathbf{K} \mathbf{x}$
* [Observer](control:optimal:observer), for state estimation
* [Full-state feed back on the observed state](control:controller-observer), $\mathbf{u} = - \mathbf{K} \mathbf{o}$
* [Output feedback](control:optimal:output-fb), $\mathbf{u} = - \mathbf{K} \mathbf{y}$

**Stochastic signals.**
* [Kalman filter](control:kalman), i.e. optimal observer w.r.t. white noise system exogenous input and measurement noise
