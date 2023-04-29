import { create } from "zustand"

export interface State {
    count: number
}

const $countStore = create<State>(set => ({
    count: 0,
    add: () => set(s => ({ count: s.count + 1 }))
}))


export default $countStore 