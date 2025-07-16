import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, TouchableOpacity } from 'react-native';
import { db } from '../database/config';

const TransactionList = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetchTransactions();
  }, []);

  const fetchTransactions = async () => {
    try {
      const transactionRef = db.collection('transactions');
      const transactions = await transactionRef.get();
      const transactionData = transactions.docs.map((doc) => doc.data());
      setTransactions(transactionData);
    } catch (error) {
      console.error('Error fetching transactions:', error);
    }
  };

  const renderItem = ({ item }) => {
    return (
      <TouchableOpacity>
        <View>
          <Text>{item.name}</Text>
          <Text>{item.amount}</Text>
          <Text>{item.date}</Text>
        </View>
      </TouchableOpacity>
    );
  };

  return (
    <View>
      <FlatList
        data={transactions}
        renderItem={renderItem}
        keyExtractor={(item) => item.id}
      />
    </View>
  );
};

export default TransactionList;
