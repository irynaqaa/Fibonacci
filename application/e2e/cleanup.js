import { detox } from 'detox';
import { device } from 'detox';

beforeAll(async () => {
  await detox.init();
  await device.launchApp();
});

afterAll(async () => {
  await detox.cleanup();
});