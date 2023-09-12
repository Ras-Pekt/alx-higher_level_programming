#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let listLen = list.length - 1;

  while (listLen >= 0) {
    newList.push(list[listLen]);
    listLen--;
  }
  return newList;
};
