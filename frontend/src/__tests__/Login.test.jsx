import { render, screen, fireEvent } from '@testing-library/react';
import Login from '../pages/Login';

test('renders Login form', () => {
  render(<Login />);
  expect(screen.getByText(/Login/i)).toBeInTheDocument();
  expect(screen.getByPlaceholderText(/Username/i)).toBeInTheDocument();
  expect(screen.getByPlaceholderText(/Password/i)).toBeInTheDocument();
});
