#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from keystonemiddleware import auth_token

_NOAUTH_PATHS = ['/', '/versions', '/healthcheck']


class SkippingAuthProtocol(auth_token.AuthProtocol):
    """SkippingAuthProtocol to reach special endpoints

    Bypasses keystone authentication for special request paths, such
    as the api version discovery path.

    Note:
        SkippingAuthProtocol is lean customization
        of :py:class:`keystonemiddleware.auth_token.AuthProtocol`
        that disables keystone communication if the request path
        is in the _NOAUTH_PATHS list.

    """

    def process_request(self, request):
        path = request.path
        if path in _NOAUTH_PATHS:
            return None  # return NONE to reach actual logic

        return super(SkippingAuthProtocol, self).process_request(request)
