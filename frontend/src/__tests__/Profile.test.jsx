import { render, screen } from '@testing-library/react';
import Profile from '../pages/Profile';
import { MemoryRouter, Route, Routes } from 'react-router-dom';

test('renders loading for profile', () => {
  render(
    <MemoryRouter initialEntries={["/profile/testuser"]}>
      <Routes>
        <Route path="/profile/:username" element={<Profile />} />
      </Routes>
    </MemoryRouter>
  );
  expect(screen.getByText(/Loading/i)).toBeInTheDocument();
});
