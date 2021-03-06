from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from pypi.viewmodels.cms.cms_request_viewmodel import CmsRequestViewModel


@view_config(route_name='cms_request')  # , renderer='pypi:templates/home/index.pt')
def cms_request(request: Request):
    vm = CmsRequestViewModel(request)
    if vm.page:
        return Response(body=f'Title: {vm.page.get("title")}...')

    if vm.redirect:
        return HTTPFound(vm.redirect_url)

    raise HTTPNotFound()
