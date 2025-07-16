import React, { useState } from 'react';
import { View, TextInput, Button, Text } from 'react-native';
import CryptoJS from 'crypto-js';

const Encrypt = () => {
  const [text, setText] = useState('');
  const [encryptedText, setEncryptedText] = useState('');

  const handleEncrypt = () => {
    const encrypted = CryptoJS.AES.encrypt(text, 'secret key').toString();
    setEncryptedText(encrypted);
  };

  return (
    <View>
      <TextInput
        value={text}
        onChangeText={(text) => setText(text)}
        placeholder="Enter text to encrypt"
      />
      <Button title="Encrypt" onPress={handleEncrypt} />
      <Text>Encrypted Text: {encryptedText}</Text>
    </View>
  );
};

export default Encrypt;
