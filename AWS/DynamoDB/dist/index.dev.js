"use strict";

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

//Database connections
var AWS = require("aws-sdk"); // AWS.config.update({
//   region: "local",
//   endpoint: "http://localhost:8000",
// });


var docClient = new AWS.DynamoDB.DocumentClient();

var UpdateItemFromTable = function UpdateItemFromTable(_ref) {
  var params = _ref.params;
  return new Promise(function (resolve, reject) {
    docClient.update(params, function (err, data) {
      if (err) {
        resolve(false);
      } else {
        resolve(data);
      }
    });
  });
};

var GetFromTable = function GetFromTable(_ref2) {
  var params = _ref2.params;
  return new Promise(function (resolve, reject) {
    docClient.get(params, function (err, data) {
      if (err) {
        resolve(_defineProperty({
          err: "Something Went Wrong!"
        }, "err", err));
      } else {
        resolve(data);
      }
    });
  });
};

var PutItemToTable = function PutItemToTable(_ref3) {
  var params = _ref3.params;
  return new Promise(function (resolve, reject) {
    docClient.put(params, function (err, data) {
      if (err) {
        resolve(false);
      } else {
        resolve(true);
      }
    });
  });
};