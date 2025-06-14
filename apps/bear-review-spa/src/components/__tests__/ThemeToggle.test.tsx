import { render, fireEvent } from '@testing-library/react';
import ThemeToggle from '../ThemeToggle';

describe('ThemeToggle', () => {
  it('toggles theme', () => {
    const { getByText } = render(<ThemeToggle />);
    const button = getByText(/Mode/i);
    fireEvent.click(button);
    expect(localStorage.getItem('theme')).not.toBeNull();
  });
});
