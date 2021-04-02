/**
 * @param {any} attributes
 */
function successResponse(attributes) {
    return {
        data: {
            attributes
        }
    };
}

module.exports = {
    successResponse
};