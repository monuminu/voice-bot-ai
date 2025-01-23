from abc import ABC, abstractmethod

from app.helpers.monitoring import tracer
from app.models.readiness import ReadinessEnum


class ICache(ABC):
    @abstractmethod
    @tracer.start_as_current_span("cache_readiness")
    async def readiness(self) -> ReadinessEnum:
        pass

    @abstractmethod
    @tracer.start_as_current_span("cache_get")
    async def get(self, key: str) -> bytes | None:
        pass

    @abstractmethod
    @tracer.start_as_current_span("cache_set")
    async def set(
        self,
        key: str,
        ttl_sec: int,
        value: str | bytes | None,
    ) -> bool:
        pass

    @abstractmethod
    @tracer.start_as_current_span("cache_delete")
    async def delete(self, key: str) -> bool:
        pass
