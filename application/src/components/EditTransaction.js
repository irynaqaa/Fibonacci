import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Picker, DatePicker } from 'react-native';
import { db } from '../database/config';

const EditTransaction = ({ transactionId }) => {
  const [date, setDate] = useState('');
  const [amount, setAmount] = useState('');
  const [description, setDescription] = useState('');
  const [category, setCategory] = useState('');

  useEffect(() => {
    fetchTransaction();
  }, []);

  const fetchTransaction = async () => {
    try {
      const transactionRef = db.collection('transactions').doc(transactionId);
      const transaction = await transactionRef.get();
      const transactionData = transaction.data();
      setDate(transactionData.date);
      setAmount(transactionData.amount);
      setDescription(transactionData.description);
      setCategory(transactionData.category);
    } catch (error) {
      console.error('Error fetching transaction:', error);
    }
  };

  const handleDateChange = (date) => {
    setDate(date);
  };

  const handleAmountChange = (amount) => {
    setAmount(amount);
  };

  const handleDescriptionChange = (description) => {
    setDescription(description);
  };

  const handleCategoryChange = (category) => {
    setCategory(category);
  };

  const handleSubmit = () => {
    // Add validation for user input data
    if (!date || !amount || !description || !category) {
      alert('Please fill in all fields');
      return;
    }

    // Update transaction in database or storage
    console.log('Transaction updated:', { date, amount, description, category });
  };

  return (
    <View>
      <Text>Edit Transaction</Text>
      <DatePicker
        date={date}
        onDateChange={handleDateChange}
        placeholder='Select date'
      />
      <TextInput
        value={amount}
        onChangeText={handleAmountChange}
        placeholder='Enter amount'
        keyboardType='numeric'
      />
      <TextInput
        value={description}
        onChangeText={handleDescriptionChange}
        placeholder='Enter description'
      />
      <Picker
        selectedValue={category}
        onValueChange={handleCategoryChange}
      >
        <Picker.Item label='Select category' value='' />
        <Picker.Item label='Food' value='food' />
        <Picker.Item label='Transportation' value='transportation' />
        <Picker.Item label='Entertainment' value='entertainment' />
      </Picker>
      <Button title='Submit' onPress={handleSubmit} />
    </View>
  );
};

export default EditTransaction;
