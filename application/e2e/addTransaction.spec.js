import { detox } from 'detox';
import { given } from '@detox/playground';
import { when } from '@detox/playground';
import { then } from '@detox/playground';

const { device, by, expect } = detox;

given('user is on add transaction screen')
  .when('user enters valid transaction data')
  .then('transaction is added successfully');

given('user is on add transaction screen')
  .when('user enters invalid transaction data')
  .then('error message is displayed');