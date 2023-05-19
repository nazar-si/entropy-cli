# Entropy CLI

![](./coverage/badge-branches.svg)
![](./coverage/badge-functions.svg)
![](./coverage/badge-lines.svg)
![](./coverage/badge-statements.svg)

This is the base project developed by [nazar-si](https://github.com/nazar-si) for [Entropy Concept team](https://github.com/EntropyConcept) to facilitate frontend development.

This repo comes with automated code generation CLI written in Python and several libraries preinstalled.

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
3. **Zustand** - State management
4. **Surreal UI** - Our components library
5. **Tailwind** - Styling classes
6. **SWR** - Light-weight library for fetch queries
7. **Testing** and **Linting** setups
   - **EsLint**
   - **Jest**
   - **React Testing Library**
   - **Playwright**
8. **CI/CD** with Github Actions
9. **Zod** - Schema validation library
10. **Docker**
11. **Custom hooks**

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
- **branch** - branch manipulation

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
   - Zustand
   - Tests
3. More functionality will be added in the process of usage

### Page generation
```bash
npm run cli -- create page -<flag1> -<flag2> ...
```
or shorter
```bash
npm run cli -- c p -<flag><flag>...
```
Following flags are present:
```
-d - dynamic route
-a - catch-all route
-A - optional catch-all route
-g - group route
-i - put everything inside (index) folder
-e - generate error page
-l - generate layout file
-s - do not generate style file
-f - add default fetch functions 
```
For example, to create Next.js dynamic route with Layout and Error page with prewritten fetching fountions one may use following command:
```bash
npm run cli -- c p path/page_name -dlef
```
## Structural Guidelines

The structure of the project is following:

```bash
┌ ○ /
├ ○ .husky   : Commits settings
├ ○ app/api  : API pages
├ ○ app      : Application pages
├ ○ hooks    : All the general hooks
├ ○ state    : Zustand stores
├ ○ features : Features with own hooks, logic etc.
├ ○ e2e      : E2E tests for Playwright
├ ○ tests    : Tests
├ ○ ui       : All UI components
└ ○ test-results : Results of test for Playwright
```
