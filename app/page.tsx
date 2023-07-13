import $countStore from "@/state/feature/countStore";

export default function Home() {
  return (
    <>
      <div className="">
        {$countStore((s) => s.count)}
        <button onClick={$countStore((s) => s.add)}></button>
      </div>
    </>
  );
}
