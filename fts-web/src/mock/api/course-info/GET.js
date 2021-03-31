const DATA = require("../course-list/GET.json");
const _ = require("lodash");

module.exports = (req, res) => {

    console.log(req)
    res.status(200).json(DATA[req]);
};