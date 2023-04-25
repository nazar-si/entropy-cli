//:
import { LayoutProps } from "./page.types";
//(styles){
import style from "./style.module.css";
//}
//(!dynamic){
export default function Layout({children}: LayoutProps){
//}
//(dynamic){
export default function Layout({children, params, searchParams}: LayoutProps){
//}
  return (
//(styles){
    <div className={style.layout}>
//}
//(!styles){
    <div>
//}
      {children}
    </div>
  );
}