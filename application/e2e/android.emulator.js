export const config = {
  device: {
    type: 'emulator',
    deviceName: 'emulator-5554',
  },
  binaryPath: './node_modules/react-native/android/app/build/outputs/apk/debug/app-debug.apk',
  build: 'cd android && ./gradlew assembleDebug assembleAndroidTest -DtestBuildType=debug && cd ..',
  exec: {
    startup: 'adb -s emulator-5554 shell am start -n com.application/.MainActivity',
  },
  cleanup: 'adb -s emulator-5554 shell pm clear com.application',
  artifacts: {
    paths: ['./e2e/screenshots'],
    keepOnlyRecentArtifacts: true,
  },
};