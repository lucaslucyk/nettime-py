from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from ..base import Base


class BlockMinute(BaseModel):
    start: Optional[int] = Field(default=None)
    end: Optional[int] = Field(default=None)


class Block(BaseModel):
    id: int
    color: Optional[str] = Field(default=None)
    type: int
    minutes: Optional[List[BlockMinute]] = Field(default=None, alias="Minutos")


class Present(BaseModel):
    today: Optional[bool] = Field(default=None, alias="Today")
    blocks: Optional[List[Block]] = Field(default=None, alias="Bloques")


class DepartmentValidity(BaseModel):
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    end_date: Optional[datetime] = Field(default=None, alias="EndDate")


class EmployeeDepartment(BaseModel):
    element: int = Field(default=None, alias="Elemento")
    validity: Optional[List[DepartmentValidity]] = Field(
        default=None, alias="Validez"
    )


class Employee(Base):
    last_name: Optional[str] = Field(default=None, alias="LastName")
    name_employee: Optional[str] = Field(default=None, alias="nameEmployee")
    no_attendance: Optional[bool] = Field(default=None, alias="NoAttendance")
    fingers_quantity: Optional[int] = Field(default=None, alias="NumFingers")

    # TODO: split by ; char
    timetypes: Optional[str] = Field(default=None, alias="TimeTypesEmployee")

    readers: Optional[List[int]] = Field(default=None, alias="Readers")
    town: Optional[str] = Field(default=None, alias="Town")
    province: Optional[str] = Field(default=None, alias="Province")
    postal_code: Optional[str] = Field(default=None, alias="PostalCode")

    birth_date: Optional[datetime] = Field(default=None, alias="birthdate")
    register_system_date: Optional[datetime] = Field(
        default=None, alias="RegisterSystemDate"
    )

    # TODO: Check to edit with periods
    active_days: Optional[str] = Field(
        default=None,
        alias="ActiveDays",
        description="Antiquity"
    )
    activedays: Optional[str] = Field(default=None, alias="Persona.DiasActivos")

    employee_departments: Optional[List[EmployeeDepartment]] = Field(
        default=None,
        alias="Departments"
    )

    calendar: Optional[int] = Field(default=None, alias="Calendar")
    portal_not_validation_required: Optional[bool] = Field(
        default=None,
        alias="Portal.NoRequiereValidacionEnCorreccion"
    )
    portal_can_not_edit: Optional[bool] = Field(
        default=None,
        alias="Portal.NoPuedeEditar"
    )
    portal_can_use: Optional[bool] = Field(
        default=None,
        alias="Portal.UsaPortal"
    )
    portal_results_template: Optional[int] = Field(
        default=None,
        alias="Portal.PlantillaResultados"
    )
    portal_disable_movs: Optional[bool] = Field(
        default=None,
        alias="Portal.DisableMovimientos"
    )
    portal_disable_resume_view: Optional[bool] = Field(
        default=None,
        alias="Portal.DisableVistaResumen"
    )

    present: Optional[Present] = Field(default=None, alias="Persona.Presente")
    is_present: Optional[bool] = Field(default=None, alias="IsPresent")
    departments: Optional[str] = Field(
        default=None,
        alias="Persona.Departaments"
    )
    photo: Optional[str] = Field(default=None, alias="Photo")
    clockings: Optional[str] = Field(default=None, alias="Persona.Clockings")
    dni_name_lastname: Optional[str] = Field(
        default=None,
        alias="DNI_Apellidos_Nombre"
    )
    name_lastname: Optional[str] = Field(default=None, alias="Apellidos_Nombre")
    anomaly: Optional[str] = Field(default=None, alias="Persona.Anomalia")
    shift: Optional[str] = Field(default=None, alias="Persona.Jornada")
    effective_calendar: Optional[str] = Field(
        default=None,
        alias="Persona.Calendario"
    )
    base_calendar: Optional[str] = Field(
        default=None,
        alias="Persona.CalendarioBase"
    )
    is_active: Optional[bool] = Field(default=None, alias="Persona.DeAlta")
    id_enroll: Optional[int] = Field(default=None, alias="idEnroll")
    enroll_active: Optional[int] = Field(default=None, alias="enrollActive")
    access_current_zone: Optional[int] = Field(
        default=None,
        alias="Accesos.Zona"
    )
    access_profiles: Optional[str] = Field(
        default=None,
        alias="Accesos.Perfiles"
    )
    phone: Optional[str] = Field(default=None, alias="Phone")
    cards: Optional[str] = Field(default=None, alias="Persona.Cards")

    employee_code: Optional[str] = Field(default=None, alias="employeeCode")
    company_code: Optional[str] = Field(default=None, alias="companyCode")
    professional_mobile: Optional[str] = Field(default=None, alias="Mobile")
    personal_phone: Optional[str] = Field(default=None, alias="PersonalPhone")
    personal_mobile: Optional[str] = Field(default=None, alias="PersonalMobile")

    weekly_theoretical_hours: Optional[int] = Field(
        default=None,
        alias="Persona.HorasTeoricasSemanales"
    )
    tree_node: Optional[str] = Field(default=None, alias="nodoArbol")
    nif: Optional[str] = Field(default=None, alias="nif")
    last_clocking: Optional[str] = Field(default=None, alias="LastMarcaje")
    last_clocking_reader: Optional[str] = Field(
        default=None,
        alias="LastMarcajeReader"
    )
    exboss: Optional[bool] = Field(default=None, description="Assigned to me")
    managers: Optional[str] = Field(
        default=None,
        alias="Persona.ManagersAction"
    )
    time_readers: Optional[str] = Field(
        default=None,
        alias="Persona.ValidReaders"
    )
    today_planning: Optional[str] = Field(
        default=None,
        alias="Persona.PlanisToday"
    )
    current_status: Optional[str] = Field(default=None, alias="CurrentStatus")
    current_status_wa: Optional[str] = Field(
        default=None,
        alias="CurrentStatusWA"
    )
    current_status_wo: Optional[str] = Field(
        default=None,
        alias="CurrentStatusWO"
    )
    first_day_clocking: Optional[str] = Field(
        default=None,
        alias="Persona.FirstClocking"
    )
    last_day_clocking: Optional[str] = Field(
        default=None,
        alias="Persona.LastClocking"
    )

    bio_data_enrolled: Optional[str] = Field(
        default=None,
        alias="Persona.BioDataEnrolled"
    )
    total_docs: Optional[int] = Field(default=None, alias="Persona.totalDocs")

    use_remote_clocking: Optional[bool] = Field(
        default=None,
        alias="RemoteClocking"
    )
    use_mobile_clocking: Optional[bool] = Field(
        default=None,
        alias="MobileClocking"
    )
    mobile_id: Optional[str] = Field(default=None, alias="mobileId")
    proface_admin: Optional[bool] = Field(default=None, alias="ProfaceAdmin")
