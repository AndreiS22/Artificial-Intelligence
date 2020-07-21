function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta


tot = 0;
reg = 0;
for i = 1:m,
  g = X(i, :);
  h = sigmoid(theta' * g');
  tot = tot - y(i) * log(h) - (1 - y(i)) * log(1 - h);
endfor
for i = 2:size(X, 2),
  reg = reg + theta(i) * theta(i);
endfor

J = 1 / m * tot + lambda / (2 * m) * reg;

for j = 1:size(X, 2),
  tot = 0;
  for i = 1:m,
    g = X(i, :);
    h = sigmoid(theta' * g');
    tot = tot + (h - y(i)) * X(i, j);
  endfor
  tot = 1 / m * tot;
  if j > 1,
    tot = tot + lambda / m * theta(j);
  endif
  grad(j) = tot; 
endfor



% =============================================================

end