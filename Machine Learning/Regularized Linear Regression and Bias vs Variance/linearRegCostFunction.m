function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples
n = size(X, 2);

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%

tot = X * theta - y;
sqtot = tot .^ 2;
J = sum(sqtot) * 1 / (2 * m);

reg = 0;
sqt = theta .^ 2;
for i = 2:n,
  reg += sqt(i); 
endfor

reg = reg * lambda / (2 * m);
J = J + reg;

for j = 1:n,
  temp = tot' * X(:, j);
  grad(j) = temp * 1 / m;
  if j > 1,
    grad(j) = grad(j) + lambda / m * theta(j);
  endif
endfor










% =========================================================================

grad = grad(:);

end
