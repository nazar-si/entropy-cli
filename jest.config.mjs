import nextJest from "next/jest.js";

const createJestConfig = nextJest({
  dir: "./",
});

/** @type {import('jest').Config} */
const customJestConfig = {
  setupFilesAfterEnv: ["<rootDir>/jest.setup.js"],
  testEnvironment: "jest-environment-jsdom",
  coverageReporters: ["json-summary"],
  testPathIgnorePatterns: ["<rootDir>/e2e/"],
};

export default createJestConfig(customJestConfig);
