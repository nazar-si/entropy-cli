//:layout
import React from "react"
//:dynamic
export type PageParams = {
    params: { {{page_name}}: string };
    searchParams: { [key: string]: string | string[] | undefined };
}
//:error
export type ErrorPage = {
    error: Error;
    reset: () => void 
}
//:layout
export type LayoutProps = {
    children: React.ReactNode
//(dynamic){
    params: { {{page_name}}: string };
    searchParams: { [key: string]: string | string[] | undefined };
//}
}
//:fetch
export type RequestType = {

}
export type DataType = {
    
}