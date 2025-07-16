import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react-native';
import EditTransaction from './EditTransaction';
import { db } from '../database/config';

const transaction = { id: 1, name: 'Transaction 1', amount: 100, type: 'income', date: '2022-01-01' };

describe('EditTransaction', () => {
  it('should render correctly', () => {
    const tree = render(<EditTransaction transaction={transaction} />);
    expect(tree).toMatchSnapshot();
  });

  it('should handle form submission', () => {
    const { getByPlaceholderText, getByText } = render(<EditTransaction transaction={transaction} />);
    const nameInput = getByPlaceholderText('Transaction Name');
    const amountInput = getByPlaceholderText('Transaction Amount');
    const typeInput = getByPlaceholderText('Transaction Type');
    const dateInput = getByPlaceholderText('Transaction Date');
    const submitButton = getByText('Update');

    fireEvent.changeText(nameInput, 'Updated Transaction');
    fireEvent.changeText(amountInput, '200');
    fireEvent.changeText(typeInput, 'expense');
    fireEvent.changeText(dateInput, '2022-01-02');
    fireEvent.press(submitButton);

    waitFor(() => expect(db.collection('transactions').doc(transaction.id).update).toHaveBeenCalledTimes(1));
  });
});