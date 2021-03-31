const DATA = require("./GET.json");
const _ = require("lodash");

module.exports = (req, res) => {
    const in24Hours = new Date(new Date().toString())
    in24Hours.setDate(in24Hours.getDate() + 1.1)
    DATA[0].startTime = Number(in24Hours);

    const in12Hours = new Date(new Date().toString())
    in12Hours.setDate(in12Hours.getDate() + 0.5)
    DATA[1].startTime = Number(in12Hours);

    const yesterday = new Date(new Date().toString())
    yesterday.setDate(yesterday.getDate() - 1)
    DATA[2].startTime = Number(yesterday);

    const overAWeekAgo = new Date(new Date().toString())
    overAWeekAgo.setDate(overAWeekAgo.getDate() - 8)
    DATA[3].startTime = Number(overAWeekAgo);
    res.status(200).json(DATA);
};