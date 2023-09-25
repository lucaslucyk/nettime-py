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
    num_fingers: Optional[int] = Field(default=None, alias="NumFingers")
    time_types_employee: Optional[str] = Field(
        default=None,
        alias="TimeTypesEmployee"
    )
    readers: Optional[List[int]] = Field(default=None, alias="Readers")
    town: Optional[str] = Field(default=None, alias="Town")
    province: Optional[str] = Field(default=None, alias="Province")
    postal_code: Optional[str] = Field(default=None, alias="PostalCode")
    birth_date: Optional[datetime] = Field(default=None, alias="birthdate")
    register_system_date: Optional[datetime] = Field(
        default=None, alias="RegisterSystemDate"
    )
    active_days: Optional[str] = Field(
        default=None,
        alias="ActiveDays",
        description="Antiquity"
    )
    persona_dias_activos: Optional[str] = Field(
        default=None,
        alias="Persona.DiasActivos"
    )
    departments: Optional[List[EmployeeDepartment]] = Field(
        default=None,
        alias="Departments"
    )
    calendar: Optional[int] = Field(default=None, alias="Calendar")
    portal_no_requiere_validacion_en_correccion: Optional[bool] = Field(
        default=None,
        alias="Portal.NoRequiereValidacionEnCorreccion"
    )
    portal_no_puede_editar: Optional[bool] = Field(
        default=None,
        alias="Portal.NoPuedeEditar"
    )
    portal_usa_portal: Optional[bool] = Field(
        default=None,
        alias="Portal.UsaPortal"
    )
    portal_plantilla_resultados: Optional[int] = Field(
        default=None,
        alias="Portal.PlantillaResultados"
    )
    portal_disable_movimientos: Optional[bool] = Field(
        default=None,
        alias="Portal.DisableMovimientos"
    )
    portal_disable_vista_resumen: Optional[bool] = Field(
        default=None,
        alias="Portal.DisableVistaResumen"
    )

    persona_presente: Optional[Present] = Field(
        default=None,
        alias="Persona.Presente"
    )
    is_present: Optional[bool] = Field(default=None, alias="IsPresent")
    persona_departaments: Optional[str] = Field(
        default=None,
        alias="Persona.Departaments"
    )
    photo: Optional[str] = Field(default=None, alias="Photo")
    persona_clockings: Optional[str] = Field(
        default=None,
        alias="Persona.Clockings"
    )
    dni_apellidos_nombre: Optional[str] = Field(
        default=None,
        alias="DNI_Apellidos_Nombre"
    )
    apellidos_nombre: Optional[str] = Field(
        default=None,
        alias="Apellidos_Nombre"
    )
    persona_anomalia: Optional[str] = Field(
        default=None,
        alias="Persona.Anomalia"
    )
    persona_jornada: Optional[str] = Field(
        default=None,
        alias="Persona.Jornada"
    )
    persona_calendario: Optional[str] = Field(
        default=None,
        alias="Persona.Calendario"
    )
    persona_calendario_base: Optional[str] = Field(
        default=None,
        alias="Persona.CalendarioBase"
    )
    persona_de_alta: Optional[bool] = Field(
        default=None,
        alias="Persona.DeAlta"
    )
    id_enroll: Optional[int] = Field(default=None, alias="idEnroll")
    enroll_active: Optional[int] = Field(default=None, alias="enrollActive")
    accesos_zona: Optional[int] = Field(
        default=None,
        alias="Accesos.Zona"
    )
    accesos_perfiles: Optional[str] = Field(
        default=None,
        alias="Accesos.Perfiles"
    )
    phone: Optional[str] = Field(default=None, alias="Phone")
    persona_cards: Optional[str] = Field(default=None, alias="Persona.Cards")

    employee_code: Optional[str] = Field(default=None, alias="employeeCode")
    company_code: Optional[str] = Field(default=None, alias="companyCode")
    mobile: Optional[str] = Field(default=None, alias="Mobile")
    personal_phone: Optional[str] = Field(default=None, alias="PersonalPhone")
    personal_mobile: Optional[str] = Field(default=None, alias="PersonalMobile")

    persona_horas_teoricas_semanales: Optional[int] = Field(
        default=None,
        alias="Persona.HorasTeoricasSemanales"
    )
    nodo_arbol: Optional[str] = Field(default=None, alias="nodoArbol")
    nif: Optional[str] = Field(default=None, alias="nif")
    last_marcaje: Optional[str] = Field(default=None, alias="LastMarcaje")
    last_marcaje_reader: Optional[str] = Field(
        default=None,
        alias="LastMarcajeReader"
    )
    exboss: Optional[bool] = Field(
        default=None,
        alias="exboss",
        description="Assigned to me"
    )
    persona_managers_action: Optional[str] = Field(
        default=None,
        alias="Persona.ManagersAction"
    )
    persona_valid_readers: Optional[str] = Field(
        default=None,
        alias="Persona.ValidReaders"
    )
    persona_planis_today: Optional[str] = Field(
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
    persona_first_clocking: Optional[str] = Field(
        default=None,
        alias="Persona.FirstClocking"
    )
    persona_last_clocking: Optional[str] = Field(
        default=None,
        alias="Persona.LastClocking"
    )
    persona_bio_data_enrolled: Optional[str] = Field(
        default=None,
        alias="Persona.BioDataEnrolled"
    )
    persona_total_docs: Optional[int] = Field(
        default=None,
        alias="Persona.totalDocs"
    )
    remote_clocking: Optional[bool] = Field(
        default=None,
        alias="RemoteClocking"
    )
    mobile_clocking: Optional[bool] = Field(
        default=None,
        alias="MobileClocking"
    )
    mobile_id: Optional[str] = Field(default=None, alias="mobileId")
    proface_admin: Optional[bool] = Field(default=None, alias="ProfaceAdmin")
