import React, { useState, useEffect } from 'react';
import { View, Text, Button } from 'react-native';
import FingerprintScanner from 'react-native-fingerprint-scanner';

const BiometricAuthentication = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    FingerprintScanner.isSensorAvailable()
      .then((available) => {
        if (available) {
          FingerprintScanner.authenticate({
            onAttempt: () => console.log('onAttempt'),
            onAuthenticationFailed: () => console.log('onAuthenticationFailed'),
            onAuthenticationSucceeded: () => {
              console.log('onAuthenticationSucceeded');
              setIsAuthenticated(true);
            },
          });
        } else {
          console.log('Biometric sensor is not available');
        }
      })
      .catch((error) => {
        console.error('Error checking biometric availability:', error);
      });
  }, []);

  return (
    <View>
      <Text>Biometric Authentication</Text>
      {isAuthenticated ? (
        <Text>Authenticated successfully</Text>
      ) : (
        <Button title="Authenticate" onPress={() => {}} />
      )}
    </View>
  );
};

export default BiometricAuthentication;
