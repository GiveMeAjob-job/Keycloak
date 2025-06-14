'use client';
import { useTheme } from './theme-provider';

export default function ThemeToggle() {
  const { theme, toggle } = useTheme();
  return (
    <button onClick={toggle} className="p-2 text-sm">
      {theme === 'dark' ? 'Light' : 'Dark'}
    </button>
  );
}
