import { detox } from 'detox';
import { given } from '@detox/playground';
import { when } from '@detox/playground';
import { then } from '@detox/playground';

const { device, by, expect } = detox;
given('user is on transaction list screen')
  .when('user adds a new transaction')
  .then('new transaction is displayed in the list');

given('user is on transaction list screen')
  .when('user edits a transaction')
  .then('transaction is updated in the list');

given('user is on transaction list screen')
  .when('user deletes a transaction')
  .then('transaction is removed from the list');