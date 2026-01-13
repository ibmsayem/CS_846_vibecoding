import { render, screen } from '@testing-library/react';
import Register from '../pages/Register';

test('renders Register form', () => {
  render(<Register />);
  expect(screen.getByText(/Register/i)).toBeInTheDocument();
  expect(screen.getByPlaceholderText(/Username/i)).toBeInTheDocument();
  expect(screen.getByPlaceholderText(/Email/i)).toBeInTheDocument();
  expect(screen.getByPlaceholderText(/Password/i)).toBeInTheDocument();
});
