from abc import ABC, abstractmethod
from typing import Any


class RPAAdapter(ABC):
    """Vendor-neutral contract for connecting automation runtimes to RPA-X."""

    @abstractmethod
    def health(self) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def get_run(self, run_id: str) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def retry(self, run_id: str, step_id: str | None = None) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def stop(self, run_id: str) -> dict[str, Any]:
        raise NotImplementedError
