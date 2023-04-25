import { configureStore, ThunkAction, Action } from "@reduxjs/toolkit";
import baseSlice from "../slices/baseSlice";
// {{slices_import}}

export const store = configureStore({
  reducer: {
    baseReducer: baseSlice,
    // {{slices_reducer}}
  },
});

export type AppState = ReturnType<typeof store.getState>;

export type AppDispatch = typeof store.dispatch;

export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  AppState,
  unknown,
  Action<string>
>;
