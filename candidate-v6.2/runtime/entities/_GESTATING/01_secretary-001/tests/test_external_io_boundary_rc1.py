import pytest

from src.secretary import DirectExternalIOForbidden, Secretary001


class MustNotBeCalled:
    def __getattr__(self, name):
        raise AssertionError(f"entity tried to call an external adapter: {name}")


def test_entity_cannot_chain_drive_read_to_telegram_send():
    secretary = Secretary001(execution_resolution="R1")
    with pytest.raises(DirectExternalIOForbidden, match="registered"):
        secretary.send_latest_archived_letter_to_telegram(
            root_approved=True,
            drive_client=MustNotBeCalled(),
            telegram_opener=MustNotBeCalled(),
        )
