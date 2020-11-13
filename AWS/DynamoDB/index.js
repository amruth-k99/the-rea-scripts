//Database connections
const AWS = require("aws-sdk");
// AWS.config.update({
//   region: "local",
//   endpoint: "http://localhost:8000",
// });
var docClient = new AWS.DynamoDB.DocumentClient();




const UpdateItemFromTable = ({ params }) => {
  return new Promise((resolve, reject) => {
    docClient.update(params, function (err, data) {
      if (err) {
        resolve(false);
      } else {
        resolve(data);
      }
    });
  });
};
const GetFromTable = ({ params }) => {
  return new Promise((resolve, reject) => {
    docClient.get(params, function (err, data) {
      if (err) {
        resolve({ err: "Something Went Wrong!", err });
      } else {
        resolve(data);
      }
    });
  });
};
const PutItemToTable = ({ params }) => {
  return new Promise((resolve, reject) => {
    docClient.put(params, function (err, data) {
      if (err) {
        resolve(false);
      } else {
        resolve(true);
      }
    });
  });
};
