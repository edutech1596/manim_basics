# Central place to pick and configure the TTS backend used by manim-voiceover
from typing import Literal

from manim_voiceover import VoiceoverScene

# Backends
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService
try:
    from manim_voiceover.services.azure import AzureService  # requires credentials
except Exception:
    AzureService = None
try:
    from manim_voiceover.services.edge import EdgeTTSService
except Exception:
    EdgeTTSService = None

BackendName = Literal["gtts", "edge", "azure", "record"]


def configure_voiceover(scene: VoiceoverScene, backend: BackendName = "gtts", *,
                        lang: str = "en", voice: str | None = None, rate: str | None = None,
                        pitch: str | None = None):
    """Attach a speech service to a VoiceoverScene.
    - backend: one of 'gtts' (simple), 'edge' (offline-ish), 'azure' (cloud), 'record' (manual VO).
    - lang: language code for GTTS or Edge (e.g., 'en', 'en-IN').
    - voice: voice name for Edge/Azure (e.g., 'en-US-AriaNeural').
    - rate, pitch: optional prosody (Edge/Azure).
    """
    if backend == "gtts":
        scene.set_speech_service(GTTSService(lang=lang))
        return

    if backend == "edge" and EdgeTTSService is not None:
        scene.set_speech_service(EdgeTTSService(voice=voice or "en-US-AriaNeural",
                                                rate=rate or "+0%", pitch=pitch or "+0Hz"))
        return

    if backend == "azure" and AzureService is not None:
        # Requires AZURE_SPEECH_KEY and AZURE_SPEECH_REGION env vars
        scene.set_speech_service(AzureService(voice=voice or "en-US-AriaNeural"))
        return

    if backend == "record":
        # Lets you record your own voice line-by-line with prompts
        scene.set_speech_service(RecorderService())
        return

    raise RuntimeError("Unsupported or unavailable backend: " + backend)


