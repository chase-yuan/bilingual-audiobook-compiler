from setuptools import setup


setup(
    name="bilingual-audiobook-compiler",
    version="1.0.0",
    description="Local-first interactive bilingual audiobook compiler. Bring your EPUB and audio, compile standalone Apple Books-grade offline readers in seconds.",
    py_modules=[
        "acoustic_backend",
        "acoustic_repair",
        "acoustic_whisper",
        "agy_linguistic_worker",
        "alignment_backend",
        "artifact_io",
        "audio_resolver",
        "chapter_locator",
        "chapter_metadata",
        "chapter_resolver",
        "content_profile",
        "contract_adapters",
        "dynamic_aligner",
        "extract_epub",
        "html_builder",
        "industrial_orchestrator",
        "intake_reconciler",
        "manifests",
        "mlx_acoustic_worker",
        "models",
        "pipeline",
        "quality_gate",
        "release_token",
        "run_manifest",
        "universal_runner",
        "validate_outputs",
        "whisperx_backend",
    ],
    python_requires=">=3.9",
    install_requires=[],
    extras_require={
        "acoustic": ["mlx-whisper"],
        "whisperx": ["whisperx"],
    },
    entry_points={
        "console_scripts": [
            "bilingual-compiler=universal_runner:main",
            "reader-compiler=universal_runner:main",
            "reader-validate=validate_outputs:main",
            "reader-quality-check=quality_gate:main",
        ]
    },
)
