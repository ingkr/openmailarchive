#
#  Copyright 2015 Ingmar Kroll <ingmar_kroll@web.de>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response


def index(request):
    context = {
        'heading': "OpenMailArchive",
    }
    return render(request, 'welcome.html', context)

