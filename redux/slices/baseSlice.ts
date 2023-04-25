import { createSlice } from "@reduxjs/toolkit";

export type stateType = {
    [key: string]: any;
};

const initialState: stateType = {};

type reducersType = { action: () => void }


export const attributesSlice = createSlice<stateType, reducersType>({
    name: "attributesSlice",
    initialState,
    reducers: {
        action: () => null,
    },
});

export const attributesActions = attributesSlice.actions;
export default attributesSlice.reducer;
