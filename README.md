# Entropy CLI

This is the base project developed by Entropy Concept team to facilitate frontend development.

This repo comes with automated code generation and several libraries preinstalled.

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
   - Tests
3. More functionality will be added in the process of usage
