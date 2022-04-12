#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-keyring
Version  : 23.5.0
Release  : 115
URL      : https://files.pythonhosted.org/packages/22/2b/e840597838cc63f96926bd7daca67936031635cfe6c81ee12dc652bd2dce/keyring-23.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/22/2b/e840597838cc63f96926bd7daca67936031635cfe6c81ee12dc652bd2dce/keyring-23.5.0.tar.gz
Summary  : Store and access your passwords safely.
Group    : Development/Tools
License  : MIT
Requires: pypi-keyring-bin = %{version}-%{release}
Requires: pypi-keyring-license = %{version}-%{release}
Requires: pypi-keyring-python = %{version}-%{release}
Requires: pypi-keyring-python3 = %{version}-%{release}
Requires: pypi(secretstorage)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(jeepney)
BuildRequires : pypi(secretstorage)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)

%description
.. image:: https://img.shields.io/pypi/v/keyring.svg
:target: `PyPI link`_
.. image:: https://img.shields.io/pypi/pyversions/keyring.svg
:target: `PyPI link`_

%package bin
Summary: bin components for the pypi-keyring package.
Group: Binaries
Requires: pypi-keyring-license = %{version}-%{release}

%description bin
bin components for the pypi-keyring package.


%package license
Summary: license components for the pypi-keyring package.
Group: Default

%description license
license components for the pypi-keyring package.


%package python
Summary: python components for the pypi-keyring package.
Group: Default
Requires: pypi-keyring-python3 = %{version}-%{release}

%description python
python components for the pypi-keyring package.


%package python3
Summary: python3 components for the pypi-keyring package.
Group: Default
Requires: python3-core
Provides: pypi(keyring)
Requires: pypi(importlib_metadata)
Requires: pypi(jeepney)
Requires: pypi(secretstorage)

%description python3
python3 components for the pypi-keyring package.


%prep
%setup -q -n keyring-23.5.0
cd %{_builddir}/keyring-23.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649777144
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py ptr || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-keyring
cp %{_builddir}/keyring-23.5.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-keyring/8e6689d37f82d5617b7f7f7232c94024d41066d1
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keyring

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-keyring/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
