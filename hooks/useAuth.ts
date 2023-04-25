import useSWR from "swr";

const BASE = {
  POST: {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Cache-Control": "no-store",
    },
  },
};
async function fetcher({ url, email, password }: { [index: string]: string }) {
  const payload = {
    ...BASE.POST,
    body: JSON.stringify({ email, password }),
  };
  return fetch(url, payload).then((res) => res.json());
}

interface IUser {
  id: number;
  name: string;
  email: string;
}

interface AuthResponse {
  token: string;
  user: IUser;
}

const useAuth = (email: string, password: string) => {
  const { data, error } = useSWR<AuthResponse>((url: string) =>
    fetcher({ url, email, password })
  );
  if (data?.token) localStorage.setItem("token", data.token);
  return {
    user: data?.user,
    loading: !error && !data,
    error,
  };
};

const { user, loading, error } = useAuth("email", "password");
console.log(user);
