"""Guidance compatible OpenAI models; minor tweaks."""

from __future__ import annotations

from guidance.models import Model
from guidance.models._openai import (
    OpenAIAudioInterpreter,
    OpenAIImageInterpreter,
    OpenAIInterpreter,
)


class OpenAI(Model):
    """Guidance compatible OpenAI models with additional models."""

    def __init__(
        self, model: str, echo: bool = True, api_key: str | None = None, **kwargs
    ):
        """Initialize an OpenAI model object representing a specific model state.

        Args:
            model (str): The name of the OpenAI model to use (e.g., "gpt-4o-mini").
            echo (bool): If True, displays the final result of creating this model state
                as HTML in a notebook. Defaults to True.
            api_key (str | None): The OpenAI API key for remote requests, passed to the
                `openai.OpenAI` constructor. Defaults to None.
            **kwargs: Additional keyword arguments passed directly to the
                `openai.OpenAI` constructor. Commonly used arguments include
                `base_url` and `organization`.
        """

        if "audio-preview" in model:
            interpreter_cls = OpenAIAudioInterpreter
        elif (
            model.startswith("gpt-4o")
            or model.startswith("o1")
            or model.startswith("chatgpt-4o")  # Added the chatgpt variant
        ):
            interpreter_cls = OpenAIImageInterpreter
        else:
            interpreter_cls = OpenAIInterpreter

        super().__init__(
            interpreter=interpreter_cls(model, api_key=api_key, **kwargs), echo=echo
        )
