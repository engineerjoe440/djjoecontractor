################################################################################
"""
DJ JOE Website Contract Form Filler
-----------------------------------

(c) 2022 - Stanley Solutions - Joe Stanley

This application serves the React frontend required to provide form-filling
capabilities for DJ Joe Contracts.
"""
################################################################################

# Requirements
from datetime import datetime
from uuid import uuid5
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fillpdf import fillpdfs

HOURLY_CONTRACT_PATH = "" # TODO
FIXED_CONTRACT_PATH = "" # TODO

class ContractForm(BaseModel):
    """Contract Form Fields"""
    typeOfEngagement: str
    maidenName: str
    groomName: str
    nameOfVenue: str
    venueAddress: str
    check1stFloor: bool
    check2ndFloor: bool
    checkStairs: bool
    checkElevator: bool
    checkOther: bool
    accessOther: str
    distance: float
    costPerMile: float
    dateOfEngagement: str
    startingTime: str
    hourlyWage: str
    flatFee1: str
    flatFee2: str
    flatRate1: float
    flatRate2: float
    deposit: float
    depositDue: datetime
    finalDue: datetime
    additionalAgreements: str
    mealYes: bool
    mealNo: bool
    hoursAdvance: float
    additionalMusic1: str
    additionalMusic2: str
    requestsAllowYes: bool
    requestsAllowNo: bool
    purchaserName: str
    purchaserTelephone: str
    purchaserEmail: str

def nice_number_theorem(x: float, base: int = 5, round_down: bool = True):
    """Apply the Nice Number Theorem to find a Satisfactory Number."""
    val = base * round(x / base)
    if round_down and val > x:
        val -= base
    return int(val)

def travel_cost(distance: float, costPerMile: float = 2.0) -> float:
    """Evaluate the Total Cost Associated with Travel."""
    if distance > 25:
        distance -= 25 # Remove Charge for first 25 miles
        return nice_number_theorem(distance * costPerMile, round_down=True)
    else:
        return 0 # First 25 miles are free

def create_contract_dict(details: ContractForm):
    """Consume the Contract Form and Generate Missing Fields."""
    arangements = details.dict()
    # Load Today's Date as the Date of Contracting
    arangements["madeDay"] = datetime.now().strftime("%-m/%-d/%Y")
    # Calculate Travel Expense Based on Distance (Excluding first 25mi)
    arangements["travelExpense"] = travel_cost(
        distance=details.distance,
        costPerMile=details.costPerMile
    )
    return arangements

# Application Base
app = FastAPI()

TEMPLATES: Jinja2Templates = None


@app.on_event("startup")
async def startup_event():
    """Event that Only Runs When App is Starting"""
    global TEMPLATES
    # Mount the Static File Path
    app.mount("/static", StaticFiles(directory="static"), name="static")
    TEMPLATES = Jinja2Templates(directory="templates")


# Main Application Response
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return TEMPLATES.TemplateResponse(
        "index.html",
        {
            "request": request,
            "client_token": str(uuid5())
        },
    )

@app.post("/api/v1/contract/hourly")
async def hourly_contract(details: ContractForm):
    """Fill Out an Hourly Contract."""
    try:
        fillpdfs.write_fillable_pdf(
            input_pdf_path = HOURLY_CONTRACT_PATH,
            output_pdf_path = "",
            data_dict = create_contract_dict(details),
            flatten = True,
        )
        return True
    except Exception:
        return False

@app.post("/api/v1/contract/fixed")
async def fixed_contract(details: ContractForm):
    """Fill Out an Fixed Contract."""
    try:
        fillpdfs.write_fillable_pdf(
            input_pdf_path = FIXED_CONTRACT_PATH,
            output_pdf_path = "",
            data_dict = create_contract_dict(details),
            flatten = True,
        )
        return True
    except Exception:
        return False

# END
