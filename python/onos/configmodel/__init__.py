# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/configmodel/registry.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


class GetStateMode(betterproto.Enum):
    NONE = 0
    OP_STATE = 1
    EXPLICIT_RO_PATHS = 2
    EXPLICIT_RO_PATHS_EXPAND_WILDCARDS = 3


@dataclass(eq=False, repr=False)
class ConfigModel(betterproto.Message):
    name: str = betterproto.string_field(1)
    version: str = betterproto.string_field(2)
    modules: List["ConfigModule"] = betterproto.message_field(3)
    files: Dict[str, str] = betterproto.map_field(
        4, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    get_state_mode: "GetStateMode" = betterproto.enum_field(5)


@dataclass(eq=False, repr=False)
class ConfigModule(betterproto.Message):
    name: str = betterproto.string_field(1)
    file: str = betterproto.string_field(2)
    revision: str = betterproto.string_field(3)
    organization: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class GetModelRequest(betterproto.Message):
    name: str = betterproto.string_field(1)
    version: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetModelResponse(betterproto.Message):
    model: "ConfigModel" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ListModelsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ListModelsResponse(betterproto.Message):
    models: List["ConfigModel"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class PushModelRequest(betterproto.Message):
    model: "ConfigModel" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class PushModelResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class DeleteModelRequest(betterproto.Message):
    name: str = betterproto.string_field(1)
    version: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class DeleteModelResponse(betterproto.Message):
    pass


class ConfigModelRegistryServiceStub(betterproto.ServiceStub):
    async def get_model(
        self, *, name: str = "", version: str = ""
    ) -> "GetModelResponse":

        request = GetModelRequest()
        request.name = name
        request.version = version

        return await self._unary_unary(
            "/onos.configmodel.ConfigModelRegistryService/GetModel",
            request,
            GetModelResponse,
        )

    async def list_models(self) -> "ListModelsResponse":

        request = ListModelsRequest()

        return await self._unary_unary(
            "/onos.configmodel.ConfigModelRegistryService/ListModels",
            request,
            ListModelsResponse,
        )

    async def push_model(self, *, model: "ConfigModel" = None) -> "PushModelResponse":

        request = PushModelRequest()
        if model is not None:
            request.model = model

        return await self._unary_unary(
            "/onos.configmodel.ConfigModelRegistryService/PushModel",
            request,
            PushModelResponse,
        )

    async def delete_model(
        self, *, name: str = "", version: str = ""
    ) -> "DeleteModelResponse":

        request = DeleteModelRequest()
        request.name = name
        request.version = version

        return await self._unary_unary(
            "/onos.configmodel.ConfigModelRegistryService/DeleteModel",
            request,
            DeleteModelResponse,
        )


class ConfigModelRegistryServiceBase(ServiceBase):
    async def get_model(self, name: str, version: str) -> "GetModelResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def list_models(self) -> "ListModelsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def push_model(self, model: "ConfigModel") -> "PushModelResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def delete_model(self, name: str, version: str) -> "DeleteModelResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_model(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "name": request.name,
            "version": request.version,
        }

        response = await self.get_model(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_list_models(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.list_models(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_push_model(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "model": request.model,
        }

        response = await self.push_model(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_delete_model(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "name": request.name,
            "version": request.version,
        }

        response = await self.delete_model(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/onos.configmodel.ConfigModelRegistryService/GetModel": grpclib.const.Handler(
                self.__rpc_get_model,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetModelRequest,
                GetModelResponse,
            ),
            "/onos.configmodel.ConfigModelRegistryService/ListModels": grpclib.const.Handler(
                self.__rpc_list_models,
                grpclib.const.Cardinality.UNARY_UNARY,
                ListModelsRequest,
                ListModelsResponse,
            ),
            "/onos.configmodel.ConfigModelRegistryService/PushModel": grpclib.const.Handler(
                self.__rpc_push_model,
                grpclib.const.Cardinality.UNARY_UNARY,
                PushModelRequest,
                PushModelResponse,
            ),
            "/onos.configmodel.ConfigModelRegistryService/DeleteModel": grpclib.const.Handler(
                self.__rpc_delete_model,
                grpclib.const.Cardinality.UNARY_UNARY,
                DeleteModelRequest,
                DeleteModelResponse,
            ),
        }
