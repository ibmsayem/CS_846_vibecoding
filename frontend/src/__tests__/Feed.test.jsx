import { render, screen } from '@testing-library/react';
import Feed from '../pages/Feed';

test('renders Global Feed heading', () => {
  render(<Feed />);
  const heading = screen.getByText(/Global Feed/i);
  expect(heading).toBeInTheDocument();
});
