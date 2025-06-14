import { create } from 'zustand';

interface UIState {
  sidebar: boolean;
  toggleSidebar: () => void;
}

export const useUIStore = create<UIState>((set) => ({
  sidebar: false,
  toggleSidebar: () => set((s) => ({ sidebar: !s.sidebar })),
}));
