#[path="newton.rs"]
mod newton;
use newton::mathops;

#[path="index.rs"]
mod index;
use index::mathfuns;

#[allow(dead_code)]
#[allow(unused_variables)]
#[allow(unused_imports)]

/**

`einstein::quantum`

Module for scientific purposes: quantum mechanics

Provides essential quantum functions as next:

- `inverse_qubit`
  
  Improve a basic hadamard's gate for a qubit or a list of qubits
  that fulfill an order: n=\[-1, 1\]
  
- `bidimension`
  
  Bidimensional functions
  
  Introduce: Psi function, Gamma function
*/
pub mod quantum {
    use super::mathops::{self, Sin, Cosin};
    use super::mathfuns::{self, E, PI, sqrt, fact, logn};
}

#[allow(dead_code)]
#[allow(unused_variables)]
#[allow(unused_imports)]
/**
`einstein::astro`

Module made for astrophysics 

*/
pub mod astro {
    use super::mathops::{self, Sin, Cosin, IntegralDefined, FindFactor};
}