import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react-native';
import TransactionList from './TransactionList';
import { db } from '../database/config';

const transactions = [
  { id: 1, name: 'Transaction 1', amount: 100, type: 'income', date: '2022-01-01' },
  { id: 2, name: 'Transaction 2', amount: 200, type: 'expense', date: '2022-01-02' },
];

describe('TransactionList', () => {
  it('should render correctly', () => {
    const tree = render(<TransactionList transactions={transactions} />);
    expect(tree).toMatchSnapshot();
  });

  it('should handle transaction deletion', () => {
    const { getByText } = render(<TransactionList transactions={transactions} />);
    const deleteButton = getByText('Delete');
    fireEvent.press(deleteButton);
    waitFor(() => expect(db.collection('transactions').doc(transactions[0].id).delete).toHaveBeenCalledTimes(1));
  });
});