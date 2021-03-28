const DATA = require("./GET.json");
const _ = require("lodash");

module.exports = (req, res) => {
    const idList = _.get(req.body, "data.attributes.idList", []);
    console.log(idList);
    console.log("ID LIST:", idList);
    const poiScoreList = _.filter(DATA, each => idList.includes(each.id));
    res.status(200).json({
        data: {
            attributes: {
                poiScoreList
            }
        }
    });
};