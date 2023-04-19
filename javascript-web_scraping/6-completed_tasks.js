#!/usr/bin/node
const request = require('request');

const Url = process.argv[2];

request(Url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 1;
        } else {
          completedTasks[todo.userId]++;
        }
      }
    });
    console.log(completedTasks);
  }
});
