import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react-native';
import BiometricAuthentication from './BiometricAuthentication';

const authenticate = jest.fn();

describe('BiometricAuthentication', () => {
  it('should render correctly', () => {
    const tree = render(<BiometricAuthentication authenticate={authenticate} />);
    expect(tree).toMatchSnapshot();
  });

  it('should handle authentication', () => {
    const { getByText } = render(<BiometricAuthentication authenticate={authenticate} />);
    const authenticateButton = getByText('Authenticate');
    fireEvent.press(authenticateButton);
    waitFor(() => expect(authenticate).toHaveBeenCalledTimes(1));
  });
});