import ThemeToggle from './components/ThemeToggle';
import LangSwitcher from './components/LangSwitcher';
import { useTranslation } from 'react-i18next';
import { useAuth } from './context/AuthProvider';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import ReviewEditor from './pages/ReviewEditor';
import Settings from './pages/Settings';

export default function App() {
  const { t } = useTranslation();
  const { user, signin, signout } = useAuth();
  return (
    <div className="p-4 space-y-4">
      <h1 className="text-2xl font-bold">{t('welcome')}</h1>
      <div className="flex gap-2">
        <ThemeToggle />
        <LangSwitcher />
      </div>
      <p className="text-sm">Project skeleton with Tailwind and DaisyUI.</p>
      {user ? (
        <button className="btn" onClick={signout}>Logout</button>
      ) : (
        <button className="btn" onClick={signin}>Login</button>
      )}
      <nav className="flex gap-2">
        <Link className="link" to="/">Home</Link>
        <Link className="link" to="/review/1">Review</Link>
        <Link className="link" to="/settings">Settings</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/review/:id" element={<ReviewEditor />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </div>
  );
}
