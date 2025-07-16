import React, { useState } from 'react';
import { View, Text, TextInput, Picker, DatePicker } from 'react-native';

const AddTransaction = () => {
  const [date, setDate] = useState('');
  const [amount, setAmount] = useState('');
  const [description, setDescription] = useState('');
  const [category, setCategory] = useState('');

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

    // Add transaction to database or storage
    console.log('Transaction added:', { date, amount, description, category });
  };

  return (
    <View>
      <Text>Add Transaction</Text>
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

export default AddTransaction;
