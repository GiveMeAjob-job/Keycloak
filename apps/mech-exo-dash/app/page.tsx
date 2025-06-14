import ThemeToggle from '../components/theme-toggle';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-4">
      <h1 className="text-2xl">Mech-Exo Dashboard</h1>
      <ThemeToggle />
    </main>
  );
}
