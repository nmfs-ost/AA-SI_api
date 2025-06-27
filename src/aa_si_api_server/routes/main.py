from flask import Blueprint
from aalibrary.ices_ship_names import get_all_ices_ship_codes_and_names

bp = Blueprint("main", __name__)


@bp.route("/")
def hello():
    return "You've reached the API root route!\n"

@bp.route("/ship-names")
def get_survey_netcdf():
    return get_all_ices_ship_codes_and_names();

