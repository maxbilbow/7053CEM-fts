
const express = require("express");
// @ts-ignore
const apiMocker = require("connect-api-mocker");
const serveStatic = require("serve-static");
const port = 9000;
const app = express();
console.log(__dirname);

app.use("/api", apiMocker("src/mock/api"));
app.use(serveStatic(`${__dirname}/../../build`))
console.log(`Mock API Server is up and running at: http://localhost:${port}`);
app.listen(port);