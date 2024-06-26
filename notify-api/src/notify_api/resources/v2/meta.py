# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Meta information about the service.

Currently this only provides API versioning information
"""

from flask import Blueprint, jsonify

from notify_api.metadata import APP_VERSION, FLASK_VERSION

bp = Blueprint("Meta_v2", __name__, url_prefix="/meta")


@bp.route("/info")
def info():
    """Return a JSON object with meta information about the Service."""
    return jsonify(API=f"notify_api/{APP_VERSION}", FrameWork=f"{FLASK_VERSION}")
