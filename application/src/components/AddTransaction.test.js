import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react-native';
import AddTransaction from './AddTransaction';

describe('AddTransaction', () => {
  it('should render correctly', () => {
    const tree = render(<AddTransaction />);
    expect(tree).toMatchSnapshot();
  });

  it('should handle form submission', () => {
    const { getByPlaceholderText, getByText } = render(<AddTransaction />);
    const nameInput = getByPlaceholderText('Transaction Name');
    const amountInput = getByPlaceholderText('Transaction Amount');
    const typeInput = getByPlaceholderText('Transaction Type');
    const dateInput = getByPlaceholderText('Transaction Date');
    const submitButton = getByText('Submit');

    fireEvent.changeText(nameInput, 'Test Transaction');
    fireEvent.changeText(amountInput, '100');
    fireEvent.changeText(typeInput, 'income');
    fireEvent.changeText(dateInput, '2022-01-01');
    fireEvent.press(submitButton);

    waitFor(() => expect(console.log).toHaveBeenCalledTimes(1));
  });
});