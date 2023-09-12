#!/usr/bin/node

// converter returns a function
// the returned function takes an argument that is converted to the base

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
