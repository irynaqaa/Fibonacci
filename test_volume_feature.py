import pytest
from application.noisy_input_API import analyze_frequency_spectrum


def test_flat_mode():
    """
    Test to ensure the system can be set to flat mode.
    """
    result = analyze_frequency_spectrum(set_mode='flat')
    assert result['mode'] == 'flat', "Failed to set flat mode"


def test_volume_rtc_commands():
    """
    Test to send volume RTC commands and verify the response.
    """
    response = analyze_frequency_spectrum(send_command='volume_up')
    assert response['volume'] > 0, "Volume should be greater than 0"


def test_output_spectrum():
    """
    Test to check the output spectrum for expected results within audible range.
    """
    spectrum = analyze_frequency_spectrum()
    assert all(20 <= freq <= 20000 for freq in spectrum['frequencies']), \
        "Frequencies should be within the audible range (20 Hz to 20,000 Hz)"


@pytest.mark.parametrize("input_signal, expected_output", [
    ("signal_1", "expected_output_1"),
    ("signal_2", "expected_output_2"),
])
def test_signal_processing(input_signal, expected_output):
    """
    Test to verify the output for various input signals.
    """
    output = analyze_frequency_spectrum(input_signal=input_signal)
    assert output['result'] == expected_output, \
        f"Output for {input_signal} did not match expected output"
