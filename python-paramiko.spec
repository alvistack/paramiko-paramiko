# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
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

%global debug_package %{nil}

Name: python-paramiko
Epoch: 100
Version: 2.10.3
Release: 1%{?dist}
BuildArch: noarch
Summary: Native Python SSHv2 protocol library
License: LGPL-2.1-only
URL: https://github.com/paramiko/paramiko/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
"Paramiko" is a combination of the Esperanto words for "paranoid" and
"friend". It's a module for Python 2.7/3.4+ that implements the SSH2
protocol for secure (encrypted and authenticated) connections to remote
machines. Unlike SSL (aka TLS), SSH2 protocol does not require
hierarchical certificates signed by a powerful central authority. You
may know SSH2 as the protocol that replaced Telnet and rsh for secure
access to remote shells, but the protocol also includes the ability to
open arbitrary channels to remote services across the encrypted tunnel
(this is how SFTP works, for example).

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-paramiko
Summary: Native Python SSHv2 protocol library
Requires: python3
Requires: python3-bcrypt >= 3.1.3
Requires: python3-cryptography >= 2.5
Requires: python3-pynacl >= 1.0.1
Provides: python3-paramiko = %{epoch}:%{version}-%{release}
Provides: python3dist(paramiko) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-paramiko = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(paramiko) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-paramiko = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(paramiko) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-paramiko
"Paramiko" is a combination of the Esperanto words for "paranoid" and
"friend". It's a module for Python 2.7/3.4+ that implements the SSH2
protocol for secure (encrypted and authenticated) connections to remote
machines. Unlike SSL (aka TLS), SSH2 protocol does not require
hierarchical certificates signed by a powerful central authority. You
may know SSH2 as the protocol that replaced Telnet and rsh for secure
access to remote shells, but the protocol also includes the ability to
open arbitrary channels to remote services across the encrypted tunnel
(this is how SFTP works, for example).

%files -n python%{python3_version_nodots}-paramiko
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-paramiko
Summary: Native Python SSHv2 protocol library
Requires: python3
Requires: python3-bcrypt >= 3.1.3
Requires: python3-cryptography >= 2.5
Requires: python3-pynacl >= 1.0.1
Provides: python3-paramiko = %{epoch}:%{version}-%{release}
Provides: python3dist(paramiko) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-paramiko = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(paramiko) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-paramiko = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(paramiko) = %{epoch}:%{version}-%{release}

%description -n python3-paramiko
"Paramiko" is a combination of the Esperanto words for "paranoid" and
"friend". It's a module for Python 2.7/3.4+ that implements the SSH2
protocol for secure (encrypted and authenticated) connections to remote
machines. Unlike SSL (aka TLS), SSH2 protocol does not require
hierarchical certificates signed by a powerful central authority. You
may know SSH2 as the protocol that replaced Telnet and rsh for secure
access to remote shells, but the protocol also includes the ability to
open arbitrary channels to remote services across the encrypted tunnel
(this is how SFTP works, for example).

%files -n python3-paramiko
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
