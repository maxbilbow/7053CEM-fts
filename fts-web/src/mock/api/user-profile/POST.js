const DATA = require("./GET.json");
const _ = require("lodash");

module.exports = (req, res) => {
    console.log(req.body)
    const profile = _.get(req.body, "data.attributes.profile");
    if (profile) {
        Object.assign(DATA, profile);
    }
    console.log("PROFILE:", profile);
    res.status(200).json({
        data: {
            attributes: {

            }
        }
    });
};