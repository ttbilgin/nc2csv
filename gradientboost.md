Sure, I will try to explain the mathematical fundamentals of the Gradient Boosted Tree method using equations and formulas in LaTeX format. Here is a brief overview:

- The goal of the Gradient Boosted Tree method is to find a function $F(x)$ that minimizes a given loss function $L(y, F(x))$, where $y$ is the true label and $x$ is the input vector.
- The function $F(x)$ is represented as an additive expansion of $M$ base functions $h_m(x)$, which are usually regression trees. That is, $$F(x) = \sum_{m=1}^M h_m(x)$$
- The base functions $h_m(x)$ are learned in a greedy, stagewise manner, by fitting the negative gradient of the loss function at each iteration. That is, $$h_m(x) = \arg\min_h \sum_{i=1}^N L(y_i, F_{m-1}(x_i) + h(x_i))$$ where $F_{m-1}(x) = \sum_{k=1}^{m-1} h_k(x)$ is the function learned at the previous iteration.
- The final function $F(x)$ is obtained by adding a shrinkage factor $\nu$ to each base function, which controls the learning rate and reduces overfitting. That is, $$F(x) = \sum_{m=1}^M \nu h_m(x)$$

For more details, you can refer to the original paper⁴ or some other resources¹²³. I hope this helps. 😊

Kaynak: Bing ile konuşma, 22.01.2024
(1) Greedy function approximation: A gradient boosting machine.. https://projecteuclid.org/journals/annals-of-statistics/volume-29/issue-5/Greedy-function-approximation-A-gradient-boosting-machine/10.1214/aos/1013203451.full.
(2) An Introduction to Gradient Boosting Decision Trees. https://www.machinelearningplus.com/machine-learning/an-introduction-to-gradient-boosting-decision-trees/.
(3) Introduction to Boosted Trees — xgboost 2.0.3 documentation. https://xgboost.readthedocs.io/en/stable/tutorials/model.html.
(4) XGBoost Mathematics Explained. A walk-through of the Gradient Boosted .... https://dimleve.medium.com/xgboost-mathematics-explained-58262530904a.
(5) Greedy Function Approximation: A Gradient Boosting Machine. https://biostat.jhsph.edu/~mmccall/articles/friedman_1999.pdf.
(6) Greedy function approximation a gradient boosting machine. https://www.cse.cuhk.edu.hk/irwin.king/_media/presentations/2001_greedy_function_approximation_a_gradient_boosting_machine.pdf.
(7) undefined. https://doi.org/10.1214/aos/1013203451.
(8) undefined. https://github.com/dmlc/xgboost%29.
