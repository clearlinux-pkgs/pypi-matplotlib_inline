#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-matplotlib_inline
Version  : 0.1.3
Release  : 9
URL      : https://files.pythonhosted.org/packages/0f/98/838f4c57f7b2679eec038ad0abefd1acaeec35e635d4d7af215acd7d1bd2/matplotlib-inline-0.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/0f/98/838f4c57f7b2679eec038ad0abefd1acaeec35e635d4d7af215acd7d1bd2/matplotlib-inline-0.1.3.tar.gz
Summary  : Inline Matplotlib backend for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-matplotlib_inline-license = %{version}-%{release}
Requires: pypi-matplotlib_inline-python = %{version}-%{release}
Requires: pypi-matplotlib_inline-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(traitlets)

%description
# Matplotlib Inline Back-end for IPython and Jupyter
## Installation
With conda:

%package license
Summary: license components for the pypi-matplotlib_inline package.
Group: Default

%description license
license components for the pypi-matplotlib_inline package.


%package python
Summary: python components for the pypi-matplotlib_inline package.
Group: Default
Requires: pypi-matplotlib_inline-python3 = %{version}-%{release}

%description python
python components for the pypi-matplotlib_inline package.


%package python3
Summary: python3 components for the pypi-matplotlib_inline package.
Group: Default
Requires: python3-core
Provides: pypi(matplotlib_inline)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-matplotlib_inline package.


%prep
%setup -q -n matplotlib-inline-0.1.3
cd %{_builddir}/matplotlib-inline-0.1.3
pushd ..
cp -a matplotlib-inline-0.1.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656394453
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-matplotlib_inline
cp %{_builddir}/matplotlib-inline-0.1.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-matplotlib_inline/81d66775b4aa68e8154d6f3e381d9fb5cd0d8301
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-matplotlib_inline/81d66775b4aa68e8154d6f3e381d9fb5cd0d8301

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
