module.exports = {
    extends: ["airbnb-typescript", "react-app"],
    parserOptions: {
        project: './tsconfig.json'
    },
    env: {
        commonjs: true,
        browser: true
    },
    rules: {
        quotes: ["error", "double"],
        "@typescript-eslint/quotes": ["error", "double"],
        "object-curly-spacing": "off",
        "@typescript-eslint/indent": ["error", 4],
        "react/jsx-indent-props": ["error", 4],
        "react/jsx-indent": ["error", 4],
        "@typescript-eslint/lines-between-class-members": ["error", "always", { "exceptAfterSingleLine": true }],
        "react/jsx-tag-spacing": ["error", {
            "closingSlash": "never",
            "beforeSelfClosing": "never",
            "afterOpening": "never",
            "beforeClosing": "allow"
        }],
        "@typescript-eslint/no-use-before-define": "off",
        "max-len": ["error", 120],
        "class-methods-use-this": "off"
    }
};