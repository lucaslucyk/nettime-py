from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from traitlets import default
from .base import Base


class SentidoActuacion(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="Description")


class Operativa(BaseModel):
    identify: Optional[str] = Field(default=None, alias="identify")
    nivel: Optional[int] = Field(default=None, alias="nivel")


class ActuacionDef(BaseModel):
    zumbido: Optional[int] = Field(default=None, alias="Zumbido")
    leds: Optional[int] = Field(default=None, alias="Leds")
    mute: Optional[bool] = Field(default=None, alias="mute")
    reles: Optional[List[int]] = Field(default=None, alias="reles")


class AvailableRele(BaseModel):
    pos_rele: Optional[int] = Field(default=None, alias="posRele")
    description: Optional[str] = Field(default=None, alias="Description")
    available: Optional[bool] = Field(default=None, alias="available")
    unavailable_desc: Optional[str] = Field(
        default=None, alias="unavailableDesc"
    )


class AvailablePortOrKeyboard(BaseModel):
    port: Optional[str] = Field(default=None, alias="port")
    description: Optional[str] = Field(default=None, alias="Description")
    device_id: Optional[int] = Field(default=None, alias="deviceId")
    identify: Optional[bool] = Field(default=None, alias="identify")
    verify: Optional[bool] = Field(default=None, alias="verify")


class DataLabel(BaseModel):
    data: Optional[str] = Field(default=None, alias="data")
    label: Optional[str] = Field(default=None, alias="label")


class IdDescription(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="description")


class Reader(Base):
    new_photo_config: Optional[bool] = Field(
        default=None, alias="newPhotoConfig"
    )
    auto_ticket: Optional[bool] = Field(default=None, alias="autoTicket")
    event_task: Optional[bool] = Field(default=None, alias="eventTask")
    card_format: Optional[str] = Field(default=None, alias="cardFormat")
    color: Optional[str] = Field(default=None, alias="color")
    internal_name: Optional[str] = Field(default=None, alias="internalName")
    motor: Optional[int] = Field(default=None, alias="motor")
    accesos_accesos: Optional[bool] = Field(
        default=None, alias="Accesos.Accesos"
    )
    profaceX_SN: Optional[str] = Field(default=None, alias="ProfaceXSN")
    work_activity: Optional[bool] = Field(default=None, alias="workActivity")
    work_order: Optional[bool] = Field(default=None, alias="workOrder")
    printer: Optional[str] = Field(default=None, alias="printer")
    visitas_visitas: Optional[bool] = Field(
        default=None, alias="Visitas.Visitas"
    )
    leds_buzz: Optional[int] = Field(default=None, alias="ledsBuzz")
    has_display: Optional[bool] = Field(default=None, alias="hasDisplay")
    photo_card: Optional[bool] = Field(default=None, alias="photoCard")
    photo_finger: Optional[bool] = Field(default=None, alias="photoFinger")
    photo_keyboard: Optional[bool] = Field(default=None, alias="photoKeyboard")
    number: Optional[int] = Field(default=None, alias="number")
    def_time_type: Optional[int] = Field(default=None, alias="defTimeType")
    forced_direction: Optional[int] = Field(
        default=None, alias="forcedDirection"
    )
    abrepuertas: Optional[bool] = Field(default=None, alias="abrepuertas")
    sentido_actuacion: Optional[int] = Field(
        default=None, alias="sentidoActuacion"
    )
    control_horario: Optional[bool] = Field(
        default=None, alias="controlHorario"
    )
    keyboard: Optional[str] = Field(default=None, alias="keyboard")
    principal: Optional[bool] = Field(default=None, alias="principal")
    terminal: Optional[int] = Field(default=None, alias="terminal")
    sentidos_de_actuacion: Optional[List[SentidoActuacion]] = Field(
        default=None, alias="sentidosDeActuacion"
    )
    card_formats: Optional[List[Union[str, None]]] = Field(
        default=None, alias="cardFormats"
    )
    operativas: Optional[List[Operativa]] = Field(
        default=None, alias="operativas"
    )
    actuacion: Optional[Dict[str, ActuacionDef]] = Field(
        default=None, alias="Actuacion"
    )
    available_reles: Optional[List[AvailableRele]] = Field(
        default=None, alias="availableReles"
    )
    available_keyboards: Optional[List[AvailablePortOrKeyboard]] = Field(
        default=None, alias="availableKeyboards"
    )
    available_ports: Optional[List[AvailablePortOrKeyboard]] = Field(
        default=None, alias="availablePorts"
    )
    forced_direction_source: Optional[List[DataLabel]] = Field(
        default=None, alias="forcedDirectionSource"
    )
    available_motors: Optional[List[Any]] = Field(
        default=None, alias="availableMotors"
    )
    available_leds: Optional[List[IdDescription]] = Field(
        default=None, alias="availableLeds"
    )
    nodes_source: Optional[List[DataLabel]] = Field(
        default=None, alias="nodesSource"
    )
    available_printers: Optional[List[Any]] = Field(
        default=None, alias="availablePrinters"
    )
    sentido_de_paso: Optional[str] = Field(default=None, alias="sentidoDePaso")
    control_tareas: Optional[str] = Field(default=None, alias="controlTareas")
