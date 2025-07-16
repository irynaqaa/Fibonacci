import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Home from './components/Home';
import AddTransaction from './components/AddTransaction';
import TransactionList from './components/TransactionList';
import EditTransaction from './components/EditTransaction';
import BiometricAuthentication from './components/BiometricAuthentication';

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={Home} />
        <Stack.Screen name="AddTransaction" component={AddTransaction} />
        <Stack.Screen name="TransactionList" component={TransactionList} />
        <Stack.Screen name="EditTransaction" component={EditTransaction} />
        <Stack.Screen name="BiometricAuthentication" component={BiometricAuthentication} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
