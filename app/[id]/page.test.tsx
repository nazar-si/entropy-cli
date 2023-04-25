import React from "react";
import { render } from "@testing-library/react";
import "@testing-library/jest-dom";
import Page from "./page";
import style from "./style.module.css";

describe("Page test", () => {
  it("Should render", () => {
    const { container } = render(
      <Page params={{ id: "1" }} searchParams={{}} />
    );
    expect(container).toBeInTheDocument();
    expect(container.firstChild).toHaveClass(style.page);
    expect(container.firstChild).toHaveTextContent("id");
  });
});
