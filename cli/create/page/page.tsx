//:dynamic
import { NextPage } from "next";
import { PageParams } from "./page.types";
//:!dynamic
import {NextPage} from "next";
//:
//(fetch){
import {RequestType, DataType} from "./page.types"
    
const getData:(req:RequestType)=>Promise<DataType> = async (req) => {
    const data = await (new Promise<DataType>(()=>null));
    return data
}
//}
//(styles){
import style from "./style.module.css"
//}
//(fetch){
{/* @ts-expect-error Async Server Component */}
//}
//:dynamic
//(!fetch){
const Page : NextPage<PageParams> = ({params,searchParams}) => {
//}
//(fetch){
const Page : NextPage<PageParams> = async ({params,searchParams}) => {
//}
//:!dynamic
//(!fetch){
const Page : NextPage = () => {
//}
//(fetch){
const Page : NextPage = async () => {
//}
//:
//(fetch){
    const data: DataType = await getData({});
//}
    return (
//(styles){
        <div className={style.page}>
//}
//(!styles){
        <div>
//}
            {{page_name}}
        </div>
    );
}
export default Page;