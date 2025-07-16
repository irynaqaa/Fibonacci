import React, { useState, useEffect } from 'react';
import { openDatabase } from 'react-native-sqlite-storage';

const db = openDatabase({ name: 'expenseTracker.db', location: 'default' });

const Database = () => {
  const [transactions, setTransactions] = useState([]);
  const [categories, setCategories] = useState([]);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    db.transaction((tx) => {
      tx.executeSql(
        'CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL, category TEXT, date TEXT, description TEXT, type TEXT)'
      );
      tx.executeSql(
        'CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)'
      );
      tx.executeSql(
        'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)'
      );
    });
  }, []);

  const addTransaction = (transaction) => {
    db.transaction((tx) => {
      tx.executeSql('INSERT INTO transactions (amount, category, date, description, type) VALUES (?, ?, ?, ?, ?)', [
        transaction.amount,
        transaction.category,
        transaction.date,
        transaction.description,
        transaction.type
      ]);
    });
  };

  const addCategory = (category) => {
    db.transaction((tx) => {
      tx.executeSql('INSERT INTO categories (name) VALUES (?)', [category.name]);
    });
  };

  const addUser = (user) => {
    db.transaction((tx) => {
      tx.executeSql('INSERT INTO users (name, email) VALUES (?, ?)', [user.name, user.email]);
    });
  };

  const getTransactions = async () => {
    try {
      const results = await db.transaction((tx) => {
        tx.executeSql('SELECT * FROM transactions', []);
      });
      setTransactions(results);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
      <button onClick={() => addTransaction({ amount: 10.99, category: 'Food', date: '2022-01-01', description: 'Lunch', type: 'Expense' })}>Add Transaction</button>
      <button onClick={() => addCategory({ name: 'Transportation' })}>Add Category</button>
      <button onClick={() => addUser({ name: 'John Doe', email: 'john.doe@example.com' })}>Add User</button>
      <button onClick={getTransactions}>Get Transactions</button>
    <>
  );
};

export default Database;
