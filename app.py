from nova_act import NovaAct
from pydantic import BaseModel

class MedicalProblem(BaseModel):
    Problem: str

class MedicalProblemList(BaseModel):
    ProblemList: list[MedicalProblem]

with NovaAct(starting_page="https://demo.openemr.io/openemr/interface/login/login.php?site=default") as nova:
    nova.act("Log in to the OpenEMR demo site, using the username 'physician' and password 'physician'")
    nova.act("Click the 'Finder' buttom at the top of the page")
    nova.act("In the 'Search by Name' box, type in 'Belford'")
    nova.act("Select the first patient in the list")

    result = nova.act("Return the currently visible list of medical problems", schema=MedicalProblemList.model_json_schema())

    if not result.matches_schema:
        print(f"Invalid JSON {result=}")

    medical_problem_list = MedicalProblemList.model_validate(result.parsed_response)

    print(f"Medical Problem List: {medical_problem_list}")