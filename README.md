# varproridge
Code accompanying [*Data-Driven Polynomial Ridge Approximation using Variable Projection*, Hokanson and Constantine, 2018](https://epubs.siam.org/doi/abs/10.1137/17M1117690).

## Installation
Installation is possible via pip, which will in general look like this:
```
pip install git+https://github.com/NathanWycoff/varproridge.git
```

It may be necessary to add the '--user' flag depending on your environment.

## Example

As an illustrative example, we will observe data from a rank 1 quadratic function and recover the subspace corresponding to its range.


```
import numpy as np
from varproridge.ridge import PolynomialRidgeApproximation

# Problem setup: A P-dim function with only 1 important dimension
N = 30
P = 3
true_sub = np.random.normal(size=[P,1])
true_sub = true_sub / np.linalg.norm(true_sub)

f = lambda x: pow(float(true_sub.T.dot(x)), 2)

# Generate observed data
X = np.random.normal(size=[N,P])
y = [f(X[n,:]) for n in range(N)]

# Parameters for the Polynomial Ridge Approximation
sd = 1
deg = 3
n_init = 1

# Fit the PRA
pra = PolynomialRidgeApproximation(subspace_dimension = sd, degree = deg, n_init = n_init)
pra.fit(X, y)
est_sub = pra.U

# Next line gives error, 0 is perfect, 1 is orthogonal to the truth.
1 - abs(est_sub.T.dot(true_sub))
```
