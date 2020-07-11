import flask

from pypi_org.infrastructure import permissions
from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import cms_service
from pypi_org.viewmodels.cms.request_viewmodel import RequestViewModel
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint('admin', __name__, template_folder='templates')


@blueprint.route('/admin')
@response(template_file='admin/index.html')
@permissions.admin
def index():
    vm = ViewModelBase()
    return vm.to_dict()
