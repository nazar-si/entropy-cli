import { NextPage } from "next";
import { PageParams } from "./page.types";

import style from "./style.module.css";

const Page: NextPage<PageParams> = ({ params }) => {
  return <div className={style.page}>{params.id}</div>;
};
export default Page;
