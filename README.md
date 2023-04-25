# Entropy CLI

This is the base project developed by Entropy Concept team to facilitate frontend development.

This repo comes with automated code generation and several libraries preinstalled.

## Getting started

To start working on this project you need to run following commands:

```bash
npm i
npm run prepare
```

## Base

This project uses following libraries by default:

1. **Next.js** - Metaframework for SSR
2. **React** - UI Framework
3. **Surreal UI** - Our components library
4. **Tailwind** - Styling classes
5. **SWR** - Light-weight library for fetch queries
6. **Testing** and **Linting** setups
7. **CI/CD** with Github Actions
8. **Zod** - Schema validation library
9. **Docker**
10. **Custom hooks**

## Commits

The following happens when commit is made:

1. Typescript test
   - You won't be able to make commit until all of the type errors are resolved
   - If you expect error to happen use command
   - `/* @ts-expect-error Error description*/ `
2. Linting check
   - Automatically finds problems in TS code
3. Formatting
   - So that code looks the same on every device
4. Build step after `git push` to ensure that server can be successfully build before push

### Commit rules

Every commit should start with a type:

```ts
<type>: commit message
```

For example

```bash
git commit -m 'fix: finally fixed this bug!'
```

Types of commits:

- **build** - build configuration change `next.config.js, tsconfig.json` etc.
- **chore** - routine work
- **ci** - changes in CI/CD
- **docs** - documentation change
- **feat** - feature added
- **fix** - bug fix
- **perf** - performance improvement
- **refactor** - refactoring of the code
- **revert** - reversion of changes
- **style** - style and cosmetic updates
- **test** - test added, edited etc.
- **trans** - some directory changes
- **security** - security updates
- **multi** - multiple updates

To add types or change commit process described above you may address [nazar-si](https://github.com/nazar-si) ([@katze](https://t.me/sciencekatze)). Types can be also changed directly in [commitlint.config.js](./commitlint.config.js).

## CLI

To run CLI you can use following commands:

```bash
npm run cli
```

to enter command line interface or

```bash
npm run cli -- <command> -args
```

to execute commands directly. To get help you can type `h` or `help`. Basic functions are:

1. Common libraries installation
   - **tabler-icons-react** : Icons library
   - **react-dnd** : Drag and Drop library
   - **react-cva** : Class value authority to manage styles
   - **classnames** : Manage classes conditionally
   - **react-motion** : Animations library
   - **react-hook-form** : Library to work with forms
2. Generate code:
   - Next.js pages
   - Types
   - React components
   - API
   - Redux
   - Tests
3. More functionality will be added in the process of usage

## Structural Guidelines

The structure of the project is following:

```bash
┌ ○ /
├ ○ .husky   : Commits settings
├ ○ app/api  : API pages
├ ○ app      : Application pages
├ ○ hooks    : All the general hooks
├ ○ redux    : Redux stores
└ ○ features : Features with own hooks, logic etc.
```
