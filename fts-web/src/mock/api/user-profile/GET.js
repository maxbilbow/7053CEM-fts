const DATA = require("./GET.json");
const _ = require("lodash");

module.exports = (req, res) => {
    res.status(200).json(DATA);
};