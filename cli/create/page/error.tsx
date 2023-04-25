//:
"use client";
import { useEffect } from "react";
import { ErrorPage } from "./page.types";

export default function Error({ error, reset }: ErrorPage) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}
