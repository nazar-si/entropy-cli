import { create } from "zustand";

export interface Actions {
  add: () => void;
}
export interface State {
  count: number;
}

type StoreType = State & Actions;

const $countStore = create<StoreType>((set) => ({
  count: 0,
  add: () => set((s) => ({ count: s.count + 1 })),
}));

export default $countStore;
