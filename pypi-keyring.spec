#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-keyring
Version  : 23.9.3
Release  : 130
URL      : https://files.pythonhosted.org/packages/2a/ef/28d3d5428108111dae4304a2ebec80d113aea9e78c939e25255425d486ff/keyring-23.9.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/2a/ef/28d3d5428108111dae4304a2ebec80d113aea9e78c939e25255425d486ff/keyring-23.9.3.tar.gz
Summary  : Store and access your passwords safely.
Group    : Development/Tools
License  : MIT Python-2.0
Requires: pypi-keyring-bin = %{version}-%{release}
Requires: pypi-keyring-license = %{version}-%{release}
Requires: pypi-keyring-python = %{version}-%{release}
Requires: pypi-keyring-python3 = %{version}-%{release}
Requires: pypi(secretstorage)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jaraco.classes)
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
Requires: pypi(jaraco.classes)
Requires: pypi(jeepney)
Requires: pypi(secretstorage)

%description python3
python3 components for the pypi-keyring package.


%prep
%setup -q -n keyring-23.9.3
cd %{_builddir}/keyring-23.9.3
pushd ..
cp -a keyring-23.9.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663600709
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
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py ptr || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-keyring
cp %{_builddir}/keyring-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-keyring/8e6689d37f82d5617b7f7f7232c94024d41066d1 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
