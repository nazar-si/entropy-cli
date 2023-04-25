import { NextPage } from "next";
import { PageParams } from "./page.types";

import style from "./style.module.css";

const Page: NextPage<PageParams> = ({ params, searchParams }) => {
  return <div className={style.page}>id</div>;
};
export default Page;
