import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { UserManager, User } from 'oidc-client-ts';

const config = {
  authority: 'http://localhost:8080/realms/unified-apps-realm',
  client_id: 'bear-review-spa',
  redirect_uri: `${window.location.origin}/callback`,
  silent_redirect_uri: `${window.location.origin}/auth-silent.html`,
  response_type: 'code',
  scope: 'openid profile',
};

const mgr = new UserManager(config);

interface AuthContextProps {
  user: User | null;
  signin: () => Promise<void>;
  signout: () => Promise<void>;
}

const AuthContext = createContext<AuthContextProps | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    mgr.getUser().then(setUser).catch(() => null);
  }, []);

  const signin = async () => {
    await mgr.signinRedirect();
  };

  const signout = async () => {
    await mgr.signoutRedirect();
  };

  return (
    <AuthContext.Provider value={{ user, signin, signout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('AuthProvider missing');
  return ctx;
};
