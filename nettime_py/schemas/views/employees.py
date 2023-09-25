from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from ..base import Base


class DoAccess(BaseModel):
    total: bool
    offset_in: int = Field(default=0, alias="offsetIn")
    offset_out: int = Field(default=0, alias="offsetOut")


class Validity(BaseModel):
    start: Optional[datetime] = Field(default=None, alias="start")
    end: Optional[datetime] = Field(default=None, alias="end")


class ActiveDays(BaseModel):
    validity: Optional[List[Validity]] = Field(default=None, alias="validity")


class TimeType(BaseModel):
    id: int
    validity: Optional[Validity] = Field(default=None, alias="validity")


class AccessProfile(BaseModel):
    id: int
    validity: Optional[Validity] = Field(default=None, alias="validity")


class Department(BaseModel):
    id: int
    validity: Optional[Validity] = Field(default=None, alias="validity")


class YearDay(BaseModel):
    shifts: Optional[List[int]] = Field(default=None, alias="shifts")


class CalendarYear(BaseModel):
    year: Optional[int] = Field(default=None, alias="Year")
    days: Optional[Dict[str, YearDay]] = Field(default=None, alias="days")


class Cycle(BaseModel):
    start_date: Optional[datetime] = Field(default=None, alias="startDate")
    end_date: Optional[datetime] = Field(default=None, alias="sndDate")
    offset: Optional[int] = Field(default=None, alias="offset")
    cycle: Optional[int] = Field(default=None, alias="cycle")


class SubCalendar(Base):
    validity: Optional[Validity] = Field(default=None, alias="Validity")


class Calendar(Base):
    c_: Optional[str] = Field(default="", alias="c_")
    created: Optional[datetime] = Field(default=None, alias="created")
    modified: Optional[datetime] = Field(default=None, alias="modified")
    rev: Optional[int] = Field(default=None, alias="rev")
    years: Optional[List[CalendarYear]] = Field(default=None, alias="years")
    cycles: Optional[List[Cycle]] = Field(default=None, alias="Cycles")
    calendars: Optional[List[SubCalendar]] = Field(
        default=None,
        alias="Calendars"
    )
    nodes_source: Optional[List[Any]] = Field(default=None, alias="nodesSource")
    multi_name: Optional[Dict[str, str]] = Field(
        default=None,
        alias="multiName"
    )


class Source(Base):
    id: Optional[Union[int, str]] = Field(default=None, alias="id")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    type: Optional[str] = Field(default=None, alias="type")
    icon: Optional[str] = Field(default=None, alias="icon")
    description: Optional[str] = Field(default=None, alias="description")
    default: Optional[int] = Field(default=None, alias="default")
    device_type: Optional[str] = Field(default=None, alias="deviceType")
    has_element: Optional[bool] = Field(default=None, alias="hasElement")
    expr: Optional[str] = Field(default=None, alias="expr")
    allow: Optional[bool] = Field(default=None, alias="allow")
    children: Optional[List["Source"]] = Field(
        default=None,
        alias="children"
    )


class DataLabel(BaseModel):
    data: Optional[str] = Field(default=None, alias="data")
    label: Optional[str] = Field(default=None, alias="label")


class Language(DataLabel):
    ...


class GeoSource(DataLabel):
    ...


class NodeSource(DataLabel):
    ...

class InitialException(BaseModel):
    date: Optional[datetime] = Field(default=None, alias="date")
    deleted: Optional[bool] = Field(default=None, alias="deleted")
    basic: Optional[bool] = Field(default=None, alias="basic")
    has_ini_val: Optional[bool] = Field(default=None, alias="hasIniVal")
    ini_val: Optional[int] = Field(default=None, alias="iniVal")
    has_max_pos_tra: Optional[bool] = Field(
        default=None,
        alias="hasMaxPosTra"
    )
    has_max_neg_tra: Optional[bool] = Field(
        default=None,
        alias="hasMaxNegTra"
    )
    has_max_pos_val: Optional[bool] = Field(
        default=None,
        alias="hasMaxPosVal"
    )
    has_max_neg_val: Optional[bool] = Field(
        default=None,
        alias="hasMaxNegVal"
    )
    hasExpires: Optional[bool] = Field(default=None, alias="hasExpires")


class Initial(BaseModel):
    aritmetico: Optional[int] = Field(default=None, alias="aritmetico")
    exceptions: Optional[List[InitialException]] = Field(
        default=None,
        alias="exceptions"
    )


class InitialValue(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    initial: Optional[Initial] = Field(default=None, alias="initial")


class EnrollDevice(BaseModel):
    port: Optional[str] = Field(default=None, alias="port")
    num_2_enroll: Optional[int] = Field(default=None, alias="num2Enroll")
    num_enrolled: Optional[int] = Field(default=None, alias="numEnrolled")
    terminal: Optional[int] = Field(default=None, alias="terminal")


class Employee(Base):
    c_: str = Field(default="Persona", alias="c_")
    created: Optional[datetime] = Field(default=None, alias="created")
    change_password: Optional[bool] = Field(
        default=None,
        alias="changePassword"
    )
    first_WO_num_days: Optional[int] = Field(
        default=None,
        alias="firstWONumDays"
    )
    first_WO: Optional[int] = Field(default=None, alias="firstWO")
    first_WA_num_days: Optional[int] = Field(
        default=None,
        alias="firstWANumDays"
    )
    first_WA: Optional[int] = Field(default=None, alias="firstWA")
    first_TT__num_days: Optional[int] = Field(
        default=None,
        alias="firstTTNumDays"
    )
    first_TT: Optional[int] = Field(default=None, alias="firstTT")
    term_voice: Optional[bool] = Field(default=None, alias="termVoice")
    timeout_enroll_minutes: Optional[int] = Field(
        default=None,
        alias="timeoutEnrollMinutes"
    )
    timeout_enroll_date: Optional[datetime] = Field(
        default=None,
        alias="timeoutEnrollDate"
    )
    timeout_enroll: Optional[datetime] = Field(
        default=None,
        alias="timeout_enroll"
    )
    sex: Optional[int] = Field(default=None, alias="sex")
    visitas_recibir_visitas: Optional[bool] = Field(
        default=None,
        alias="Visitas.RecibirVisitas"
    )
    visitas_programar_visitas: Optional[bool] = Field(
        default=None,
        alias="Visitas.ProgramarVisitas"
    )
    ticket_email: Optional[bool] = Field(default=None, alias="ticketEmail")
    enroll_active: Optional[bool] = Field(default=None, alias="enrollActive")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    modified_by: Optional[str] = Field(default=None, alias="modifiedBy")
    birthdate: Optional[datetime] = Field(default=None, alias="birthdate")
    use_tasks_WE: Optional[bool] = Field(default=None, alias="useTasksWE")
    use_tasks_WO: Optional[bool] = Field(default=None, alias="useTasksWO")
    use_tasks_WA: Optional[bool] = Field(default=None, alias="useTasksWA")
    use_tasks: Optional[bool] = Field(default=None, alias="useTasks")
    proface_admin: Optional[bool] = Field(default=None, alias="ProfaceAdmin")
    remote_clocking_time_zone: Optional[str] = Field(
        default=None,
        alias="RemoteClockingTimeZone"
    )
    mobile_clocking: Optional[bool] = Field(
        default=None,
        alias="MobileClocking"
    )
    mobile_id: Optional[str] = Field(default=None, alias="mobileId")
    remote_clocking: Optional[bool] = Field(default=None, alias="RemoteClocking")
    portal_disable_password_change: Optional[bool] = Field(
        default=None,
        alias="Portal.DisablePasswordChange"
    )
    portal_disable_calendar: Optional[bool] = Field(
        default=None,
        alias="Portal.DisableCalendar"
    )
    portal_disable_plannings: Optional[bool] = Field(
        default=None,
        alias="Portal.DisablePlannings"
    )
    portal_disable_movimientos: Optional[bool] = Field(
        default=None,
        alias="Portal.DisableMovimientos"
    )
    portal_no_puede_editar: Optional[bool] = Field(
        default=None,
        alias="Portal.NoPuedeEditar"
    )
    portal_no_requiere_validacion_en_correccion: Optional[bool] = Field(
        default=None,
        alias="Portal.NoRequiereValidacionEnCorreccion"
    )
    portal_usa_portal: Optional[bool] = Field(
        default=None,
        alias="Portal.UsaPortal"
    )
    portal_change_language: Optional[bool] = Field(
        default=None,
        alias="Portal.ChangeLanguage"
    )
    portal_disable_vista_resumen: Optional[bool] = Field(
        default=None,
        alias="Portal.DisableVistaResumen"
    )
    modified: Optional[datetime] = Field(default=None, alias="modified")
    biolock: Optional[bool] = Field(default=None, alias="biolock")
    virtual_card: Optional[bool] = Field(default=None, alias="virtualCard")
    geolocalize: Optional[str] = Field(default=None, alias="geolocalize")
    offline: Optional[bool] = Field(default=None, alias="offline")
    total_docs: Optional[int] = Field(default=None, alias="totalDocs")
    rev: Optional[int] = Field(default=None, alias="rev")
    exboss: Optional[bool] = Field(default=None, alias="exboss")
    security_level: Optional[int] = Field(default=None, alias="securityLevel")
    html_portal: Optional[bool] = Field(default=None, alias="htmlPortal")
    inactive: Optional[bool] = Field(default=None, alias="inactive")
    pwd_cant_change: Optional[bool] = Field(default=None, alias="pwdCantChange")
    pwd_next_login: Optional[bool] = Field(default=None, alias="pwdNextLogin")
    pwd_expires: Optional[bool] = Field(default=None, alias="pwdExpires")
    pwd_retries: Optional[int] = Field(default=None, alias="pwdRetries")
    last_pwd_change: Optional[datetime] = Field(
        default=None,
        alias="lastPwdChange"
    )
    pin: Optional[int] = Field(default=None, alias="PIN")
    last_login: Optional[datetime] = Field(default=None, alias="lastLogin")
    town: Optional[str] = Field(default=None, alias="Town")
    num_fingers: Optional[int] = Field(default=None, alias="NumFingers")
    register_system_date: Optional[datetime] = Field(
        default=None,
        alias="RegisterSystemDate"
    )
    first_day_not_valid: Optional[datetime] = Field(
        default=None,
        alias="FirstDayNotValid"
    )
    company_code: Optional[str] = Field(default=None, alias="companyCode")
    employee_code: Optional[str] = Field(default=None, alias="employeeCode")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    name_employee: Optional[str] = Field(default=None, alias="nameEmployee")
    nif: Optional[str] = Field(default=None, alias="nif")
    current_login: Optional[datetime] = Field(default=None, alias="currentLogin")
    finger_IEVO1_enroll_date: Optional[datetime] = Field(
        default=None,
        alias="FingerIEVO1EnrollDate"
    )
    finger_IEVO2_enroll_date: Optional[datetime] = Field(
        default=None,
        alias="FingerIEVO2EnrollDate"
    )
    finger2_enroll_date: Optional[datetime] = Field(
        default=None,
        alias="Finger2EnrollDate"
    )
    finger1_enroll_date: Optional[datetime] = Field(
        default=None,
        alias="Finger1EnrollDate"
    )
    privacy_policy_accepted: Optional[bool] = Field(
        default=None,
        alias="privacyPolicyAccepted"
    )
    accept_all_readers: Optional[bool] = Field(
        default=None,
        alias="acceptAllReaders"
    )
    accept_all_TT: Optional[bool] = Field(default=None, alias="acceptAllTT")
    no_attendance: Optional[bool] = Field(default=None, alias="NoAttendance")
    privacy_policy_accepted_date: Optional[datetime] = Field(
        default=None,
        alias="privacyPolicyAcceptedDate"
    )
    photo: Optional[str] = Field(default=None, alias="Photo")
    bio_data_list: Optional[List[Any]] = Field(default=None, alias="bioDataList")
    remote_clocking_TZ: Optional[int] = Field(default=None, alias="RemoteClockingTZ")
    doAccess: Optional[DoAccess] = Field(default=None, alias="doAccess")
    time_types_employee: Optional[List[TimeType]] = Field(
        default=None,
        alias="TimeTypesEmployee"
    )
    departments: Optional[List[Department]] = Field(
        default=None,
        alias="Departments"
    )
    portal_plantilla_resultados: Optional[int] = Field(
        default=None,
        alias="Portal.PlantillaResultados"
    )
    calendar: Optional[Calendar] = Field(default=None, alias="Calendar")
    readers: Optional[List[int]] = Field(default=None, alias="Readers")
    cards: Optional[List[int]] = Field(default=None, alias="Cards")
    initial_values_list: Optional[List[InitialValue]] = Field(
        default=None,
        alias="initialValuesList"
    )
    source: Optional[List[Source]] = Field(default=None, alias="source")
    languages: Optional[List[Language]] = Field(default=None, alias="languages")
    node: Optional[int] = Field(default=None, alias="node")
    active_days: Optional[ActiveDays] = Field(default=None, alias="ActiveDays")
    enroll_devices: Optional[List[EnrollDevice]] = Field(
        default=None,
        alias="enrollDevices"
    )
    accesos_zona: Optional[int] = Field(default=None, alias="Accesos.Zona")
    accesos_perfiles: Optional[List[AccessProfile]] = Field(
        default=None,
        alias=""
    )
    geoloc_source: Optional[List[GeoSource]] = Field(
        default=None,
        alias="geolocSource"
    )
    nodes_source: Optional[List[NodeSource]] = Field(
        default=None,
        alias="nodesSource"
    )