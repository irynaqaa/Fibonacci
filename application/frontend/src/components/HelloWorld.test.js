import React from 'react';
import ReactDOM from 'react-dom';
import HelloWorld from './HelloWorld';

it('renders correctly', () => {
  const div = document.createElement('div');
  ReactDOM.render(<HelloWorld />, div);
  expect(div.innerHTML).toContain('Hello World!');
});
