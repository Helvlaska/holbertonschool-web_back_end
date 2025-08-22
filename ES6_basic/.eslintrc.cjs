// ES6_basic/.eslintrc.cjs
module.exports = {
  root: true,
  env: { es2021: true, node: true, jest: true },
  parserOptions: { ecmaVersion: 'latest', sourceType: 'module' },
  extends: ['eslint:recommended'],
  rules: {
    'no-var': 'error',
    'prefer-const': 'warn',
    'no-unused-vars': ['warn', { argsIgnorePattern: '^_' }]
  },
};
