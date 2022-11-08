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
from uuid import uuid4
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# pylint: disable=no-name-in-module
from pydantic import BaseModel
# pylint: enable=no-name-in-module
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
    mealIncluded: bool
    hoursAdvance: float
    additionalMusic1: str
    additionalMusic2: str
    requestsAllow: bool
    purchaserName: str
    purchaserTelephone: str
    purchaserEmail: str

def nice_number_theorem(val: float, base: int = 5, round_down: bool = True):
    """Apply the Nice Number Theorem to find a Satisfactory Number."""
    val = base * round(val / base)
    if round_down and val > val:
        val -= base
    return int(val)

def travel_cost(distance: float, cost_per_mile: float = 2.0) -> float:
    """Evaluate the Total Cost Associated with Travel."""
    if distance > 25:
        distance -= 25 # Remove Charge for first 25 miles
        return nice_number_theorem(distance * cost_per_mile, round_down=True)
    else:
        return 0 # First 25 miles are free

def create_contract_dict(details: ContractForm):
    """Consume the Contract Form and Generate Missing Fields."""
    arrangements = details.dict()
    # Load Today's Date as the Date of Contracting
    arrangements["madeDay"] = datetime.now().strftime("%-m/%-d/%Y")
    # Calculate Travel Expense Based on Distance (Excluding first 25mi)
    arrangements["travelExpense"] = travel_cost(
        distance=details.distance,
        cost_per_mile=details.costPerMile
    )
    return arrangements

# Application Base
app = FastAPI()

TEMPLATES: Jinja2Templates = None


@app.on_event("startup")
async def startup_event():
    """Event that Only Runs When App is Starting"""
    # pylint: disable=global-statement
    global TEMPLATES
    # pylint: enable=global-statement
    # Mount the Static File Path
    app.mount("/static", StaticFiles(directory="static"), name="static")
    TEMPLATES = Jinja2Templates(directory="templates")


# Main Application Response
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Web Root."""
    return TEMPLATES.TemplateResponse(
        "index.html",
        {
            "request": request,
            "client_token": str(uuid4())
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
