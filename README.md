# djjoecontractor

Contract Form Filler for DJJoe Website

### Frontend:

### Backend:
The backend is a Python/FastAPI server responsible for serving the static files
and accessing the sensitive information (private calendars) to make appropriate
queries relating to available dates.

### Linking frontend and backend (React/FastAPI):
With some minor modifications made to the FastAPI configuration,
[this guide on using Flask and React](https://blog.learningdollars.com/2019/11/29/how-to-serve-a-reactapp-with-a-flask-server/)
was used to develop the link between the two ecosystems.

## Rebuilding React Components for Serving

From the `frontend` directory, issue the following command:

```shell
npm run build
```

## Running Server for Development

From the `backend` directory, issue the following command:

```shell
uvicorn main:app --reload
```

## Forms

### Hourly Form

The Hourly Contract form contains the following fields:

```json
{
    "madeDay": "",
    "typeOfEngagement": "",
    "maidenName": "",
    "groomName": "",
    "nameOfVenue": "",
    "venueAddress": "",
    "check1stFloor": "Off",
    "check2ndFloor": "Off",
    "checkStairs": "Off",
    "checkElevator": "Off",
    "checkOther": "Off",
    "accessOther": "",
    "distance": "",
    "costPerMile": "",
    "travelExpense": "",
    "dateOfEngagement": "",
    "startingTime": "",
    "hourlyWage": "",
    "flatFee1": "",
    "flatFee2": "",
    "flatRate1": "",
    "flatRate2": "",
    "deposit": "",
    "depositDue": "",
    "finalDue": "",
    "additionalAgreements": "",
    "mealYes": "Off",
    "mealNo": "Off",
    "hoursAdvance": "",
    "additionalMusic1": "",
    "additionalMusic2": "",
    "requestsAllowYes": "Off",
    "requestsAllowNo": "Off",
    "purchaserName": "",
    "purchaserSignature": "",
    "djSignature": "",
    "purchaserTelephone": "",
    "purchaserEmail": ""
}
```